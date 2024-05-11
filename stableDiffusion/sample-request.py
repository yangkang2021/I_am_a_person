import json
import base64
import time
import requests


def submit_post(url: str, data: dict):
    """
    Submit a POST request to the given URL with the given data.
    """
    return requests.post(url, data=json.dumps(data))


def save_encoded_image(b64_image: str, output_path: str):
    """
    Save the given image to the given output path.
    """
    with open(output_path, "wb") as image_file:
        image_file.write(base64.b64decode(b64_image))

if __name__ == '__main__':
    txt2img_url = 'http://127.0.0.1:7860/sdapi/v1/txt2img'
    data = {
        'prompt': 'A girl, walking in the forest, the sun fell on her body, (masterpiece:1,2), best quality, masterpiece, highres, original, extremely detailed wallpaper, perfect lighting,(extremely detailed CG:1.2), drawing, paintbrush, looking at viewer, close-up, upper body,'
        ,
        'negative_prompt': 'NSFW, (worst quality:2), (low quality:2), (normal quality:2), lowres, normal quality, ((monochrome)), ((grayscale)), skin spots, acnes, skin blemishes, age spot, (ugly:1.331), (duplicate:1.331), (morbid:1.21), (mutilated:1.21), (tranny:1.331), mutated hands, (poorly drawn hands:1.5), blurry, (bad anatomy:1.21), (bad proportions:1.331), extra limbs, (disfigured:1.331), (missing arms:1.331), (extra legs:1.331), (fused fingers:1.61051), (too many fingers:1.61051), (unclear eyes:1.331), lowers, bad hands, missing fingers, extra digit,bad hands, missing fingers, (((extra arms and legs))),'

    }

    start_time = time.time()
    response = submit_post(txt2img_url, data)
    end_time = time.time()
    print("程序执行了%f秒" % (end_time - start_time))

    save_encoded_image(response.json()['images'][0], 'dog.png')
