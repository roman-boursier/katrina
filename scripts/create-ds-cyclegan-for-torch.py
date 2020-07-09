# We preprocess dataset for pix2pix and CycleGan according https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix
# The dataset contains chinese painting downloaded from https://github.com/ychen93/Chinese-Painting-Dataset

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


def image_to_sketch(image):
    cv_image = None

    if isinstance(image, str):
        cv_image = cv2.imread(image)
    elif isinstance(image, np.ndarray):
        cv_image = image

    cv_image_gray = cv2.cvtColor(cv_image, cv2.COLOR_BGR2GRAY)
    # cv_image_gray = 255 - cv_image_gray
    cv_image_blur = cv2.GaussianBlur(cv_image_gray, ksize=(21, 21), sigmaX=0, sigmaY=0)
    cv_image_blend = cv2.divide(cv_image_gray, cv_image_blur, scale=256)
    cv_image_blend = cv2.cvtColor(cv_image_blend, cv2.COLOR_GRAY2BGR)

    return cv_image_blend


def chinese_painting_to_sketch(path_images_input, path_sketch_output):
    if not os.path.exists(path_images_input):
        raise FileNotFoundError
    if not os.path.exists(path_sketch_output):
        os.mkdir(path_sketch_output)

    paintings_imgs = [os.path.join(path_images_input, img_file) for img_file in os.listdir(path_images_input)]

    for img in tqdm(paintings_imgs):
        filename = os.path.basename(img)

        cv_image = cv2.imread(img)

        cv_image = image_to_sketch(cv_image)

        cv2.imwrite(os.path.join(path_sketch_output, filename), cv_image)


def sketchy_photo_to_sketch(path_photos_input, path_sketchs_input, path_photos_output, path_sketchs_output):
    if not os.path.exists(path_sketchs_output):
        os.mkdir(path_sketchs_output)
    if not os.path.exists(path_photos_output):
        os.mkdir(path_photos_output)

    for root, _, files in os.walk(path_photos_input):
        category = os.path.basename(root)
        for file in tqdm(files, total=len(files)):
            path_file = os.path.join(root, file)
            if os.path.exists(path_file):
                cv_image = cv2.imread(path_file)
                cv_image = image_to_sketch(cv_image)  # image_to_canny(cv_image)
                if not os.path.exists(os.path.join(path_photos_output, file)):
                    cv2.imwrite(os.path.join(path_photos_output, category + '_coco_' + file), cv_image)

    for root, _, files in os.walk(path_sketchs_input):
        category = os.path.basename(root)
        for file in tqdm(files, total=len(files)):
            path_file = os.path.join(root, file)
            if os.path.exists(path_file) and path_file.endswith("-1.png"):
                cv_image = cv2.imread(path_file)
                # cv_image = cv2.resize(cv_image, (64, 64))
                image_name = file[:-6] + '.png'
                cv2.imwrite(os.path.join(path_sketchs_output, category + '_coco_' + image_name), cv_image)


def photo_to_canny(path_photos_input, path_photos_output):
    if not os.path.exists(path_photos_output):
        os.mkdir(path_photos_output)

    for root, _, files in os.walk(path_photos_input):
        for file in tqdm(files, total=len(files)):
            path_file = os.path.join(root, file)
            if os.path.exists(path_file):
                cv_image = cv2.imread(path_file)
                cv_image = image_to_canny(cv_image)
                if not os.path.exists(os.path.join(path_photos_output, file)):
                    cv2.imwrite(os.path.join(path_photos_output, file), cv_image)


def photo_to_gray (path_input, path_output):
    if not os.path.exists(path_output):
        os.mkdir(path_output)

    for root, _, files in os.walk(path_input):
        for file in tqdm(files, total=len(files)):
            path_file = os.path.join(root, file)
            if os.path.exists(path_file):
                cv_image = cv2.imread(path_file, cv2.IMREAD_GRAYSCALE)
                cv2.imwrite(os.path.join(path_output, file), cv_image)


def resize(path_images, size=(256, 256)):
    i = 0
    for root, _, files in os.walk(path_images):
        for file in tqdm(files, total=len(files)):
            filename = file[:-4]
            path_file = os.path.join(root, file)
            cv_image = cv2.imread(path_file, cv2.IMREAD_COLOR)
            cv_image = cv2.resize(cv_image, size)
            cv2.imwrite(os.path.join(root, filename + str(i) + '_256.jpg'), cv_image)
            i += 1
