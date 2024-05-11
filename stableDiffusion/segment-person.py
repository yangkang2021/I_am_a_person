import torch
from torchvision.models.segmentation import fcn_resnet50, FCN_ResNet50_Weights
from torchvision.io.image import read_image
from torchvision.utils import draw_segmentation_masks
import matplotlib.pyplot as plt


if __name__ == '__main__':
    img_path = 'woman-on-trail.png'

    # Load model
    weights = FCN_ResNet50_Weights.DEFAULT
    model = fcn_resnet50(weights=weights, progress=False)
    model = model.eval()

    # Load image
    img = read_image(img_path)

    # Run model
    input_tform = weights.transforms(resize_size=None)
    batch = torch.stack([input_tform(img)])
    output = model(batch)['out']

    # Apply softmax to outputs
    sem_class_to_idx = {cls: idx for (idx, cls) in enumerate(weights.meta['categories'])}
    normalized_mask = torch.nn.functional.softmax(output, dim=1)

    # Show results
    class_idx = 1
    binary_masks = (normalized_mask.argmax(class_idx) == sem_class_to_idx['person'])
    img_masked = draw_segmentation_masks(img, masks=binary_masks, alpha=0.7)
    plt.imshow(img_masked.permute(1, 2, 0).numpy())
    plt.show()
