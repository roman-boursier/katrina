import os
import cv2
import numpy as np
from tqdm import tqdm


def image_to_canny(image):
    cv_image = None

    if isinstance(image, str):
        cv_image = cv2.imread(image)
    elif isinstance(image, np.ndarray):
        cv_image = image

    edges = cv2.Canny(cv_image, 100, 200)
    edges = 255 - edges

    return edges

def pix2pix_dataset(cv_image, cv_sketch):
    # cv_image = cv2.resize(cv_image, (256, 256))
    # cv_sketch = cv2.resize(cv_sketch, (256, 256))
    cv_image_h = np.hstack((cv_image, cv_sketch))
    return cv_image_h


def photos_sketch_to_pix2pix(path_image, path_sketch, path_output):
    if not os.path.exists(path_output):
        os.mkdir(path_output)
    path_output = os.path.join(path_output, 'train')
    if not os.path.exists(path_output):
        os.mkdir(path_output)

    files = os.listdir(path_image)

    for file in tqdm(files, total=len(files)):
        filename = file[:-4]
        path_file = os.path.join(path_image, file)
        if os.path.exists(path_file):
            width_files = [sketch_file for sketch_file in os.listdir(path_sketch) if sketch_file.startswith(filename)]
            if width_files is not None:
                cv_image = cv2.imread(path_file, cv2.IMREAD_COLOR)
                # cv_image = image_to_canny(cv_image)
                for sketch_file in width_files:
                    # cv_image = cv2.cvtColor(cv_image)
                    cv_sketch = cv2.imread(os.path.join(path_sketch, sketch_file), cv2.IMREAD_COLOR)
                    # cv_sketch = cv2.cvtColor(cv_sketch, cv2.COLOR_BGR2GRAY)
                    cv_pix2pix = pix2pix_dataset(cv_image, cv_sketch)
                    cv2.imwrite(os.path.join(path_output, sketch_file), cv_pix2pix)


# For tests if we don't have the ground truth
def create_blank_pix2pix (path_images, path_output):
    if not os.path.exists(path_output):
        os.mkdir(path_output)

    files = os.listdir(path_images)
    for file in files:
        path_file = os.path.join(path_images, file)
        cv_image = np.ones((256, 256, 3), np.uint8)
        cv_sketch = cv2.imread(os.path.join(path_file))
        cv_pix2pix = pix2pix_dataset(cv_image, cv_sketch)
        cv2.imwrite(os.path.join(path_output, file), cv_pix2pix)
