import os
import json
import base64
import io
import time
import requests
import torch
from torchvision.models.segmentation import fcn_resnet50, FCN_ResNet50_Weights
from torchvision import transforms
from torchvision.io.image import read_image


IMG2IMG_URL = 'http://127.0.0.1:7860/sdapi/v1/img2img'


def generate_request(b64image: str, prompt: str, **kwargs):
    """
    Generate a request object from the given input image and prompt.
    """
    return {
        'prompt': prompt,
        'init_images': [b64image],
        **kwargs
    }


def submit_post(url: str, data: dict):
    """
    Submit a POST request to the given URL with the given data.
    """
    return requests.post(url, data=json.dumps(data))


def _b64encode(x: bytes) -> str:
    return base64.b64encode(x).decode("utf-8")


def img2b64(img):
    """
    Convert a PIL image to a base64-encoded string.
    """
    buffered = io.BytesIO()
    img.save(buffered, format='PNG')
    return _b64encode(buffered.getvalue())


def convert_mask_to_bounding_box(mask, dilation: int = 16) -> torch.Tensor:
    """
    Convert a mask to its bounding box.
    """
    # Get indices of mask
    mask_indices = torch.nonzero(mask)

    # Get bounding box
    min_y, min_x = mask_indices.min(dim=0)[0]
    max_y, max_x = mask_indices.max(dim=0)[0]

    # Dilate mask
    min_y = int(max(0, min_y - dilation))
    min_x = int(max(0, min_x - dilation))
    max_y = int(min(mask.shape[0], max_y + dilation))
    max_x = int(min(mask.shape[1], max_x + dilation))

    # Set bounding box to 1
    mask[min_y:max_y, min_x:max_x] = 1
    return mask


def save_encoded_image(b64_image: str, output_path: str):
    """
    Save the given image to the given output path.
    """
    
    with open(output_path, "wb") as image_file:
        image_file.write(base64.b64decode(b64_image))


INPAINTING_FILL_METHODS = ['fill', 'original', 'latent_noise', 'latent_nothing']


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Inpaint instances of people using stable '
                                                 'diffusion.')
    parser.add_argument('img_path', type=str, help='Path to input image.')
    parser.add_argument('-o', '--output_path', type=str, default='inpaint-person.png',
                        help='Path to output image.')
    parser.add_argument('-p', '--prompt', type=str, default='',
                        help='Stable diffusion prompt to use.')
    parser.add_argument('-n', '--negative_prompt', type=str, default='person',
                        help='Stable diffusion negative prompt.')
    parser.add_argument('-W', '--width', type=int, default=768, help='Width of output image.')
    parser.add_argument('-H', '--height', type=int, default=768, help='Height of output image.')
    parser.add_argument('-s', '--steps', type=int, default=30, help='Number of diffusion steps.')
    parser.add_argument('-c', '--cfg_scale', type=int, default=8, help='Classifier free guidance '
                        'scale, i.e. how strongly the image should conform to prompt.')
    parser.add_argument('-S', '--sample_name', type=str, default='Euler a', help='Name of sampler '
                        'to use.')
    parser.add_argument('-d', '--denoising_strength', type=float, default=0.75, help='How much to '
                        'disregard original image.')
    parser.add_argument('-f', '--fill', type=str, default=INPAINTING_FILL_METHODS[0],
                        help='The fill method to use for inpainting.')
    parser.add_argument('-b', '--mask_blur', type=int, default=8, help='Blur radius of Gaussian '
                        'filter to apply to mask.')
    parser.add_argument('-B', '--bounding_box', action='store_true', help='Convert mask to '
                        'bounding box.')
    parser.add_argument('-D', '--bbox_dilation', type=float, default=16, help='Number of pixels '
                        'to dilate bounding box.')
    args = parser.parse_args()
    assert args.fill in INPAINTING_FILL_METHODS, \
        f'Fill method must be one of {INPAINTING_FILL_METHODS}.'

    # Load image
    img = read_image(args.img_path)

    # Load model
    weights = FCN_ResNet50_Weights.DEFAULT
    model = fcn_resnet50(weights=weights, progress=False)
    model = model.eval()

    # Run model
    input_tform = weights.transforms(resize_size=None)
    batch = torch.stack([input_tform(img)])
    output = model(batch)['out']

    # Apply softmax to outputs
    sem_class_to_idx = {cls: idx for (idx, cls) in enumerate(weights.meta['categories'])}
    normalized_mask = torch.nn.functional.softmax(output, dim=1)

    # Extract mask
    tensor_to_pil = transforms.ToPILImage()
    mask = normalized_mask[0, sem_class_to_idx['person']]
    mask = mask > 0.5

    # Convert mask to bounding box
    if args.bounding_box:
        mask = convert_mask_to_bounding_box(mask, dilation=args.bbox_dilation)

    # Convert images to base64
    img = tensor_to_pil(img.cpu())
    img_b64 = img2b64(img)
    mask = tensor_to_pil(mask.to(torch.float32).cpu())
    mask_b64 = img2b64(mask)

    # Run inpainting
    extra_options = {
        'width': args.width,
        'height': args.height,
        'steps': args.steps,
        'cfg_scale': args.cfg_scale,
        'sample_name': args.sample_name,
        'denoising_strength': args.denoising_strength,
        'mask_blur': args.mask_blur,
        'inpainting_fill': INPAINTING_FILL_METHODS.index(args.fill),
        'inpaint_full_res': False
    }
    request = generate_request(img_b64, prompt=args.prompt, mask=mask_b64,
                                negative_prompt=args.negative_prompt, **extra_options)
    start_time = time.time()
    response = submit_post(IMG2IMG_URL, request)
    end_time = time.time()
    print("程序执行了%f秒" % (end_time - start_time))

    output_img_b64 = response.json()['images'][0]

    # Save images
    save_encoded_image(output_img_b64, args.output_path)
    mask_path = os.path.join(os.path.dirname(args.output_path),
                             f'mask_{os.path.basename(args.output_path)}')
    save_encoded_image(mask_b64, mask_path)
