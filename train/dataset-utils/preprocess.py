# Convert pairs input/output images to numpy array

from PIL import Image
import os
from os import listdir
from numpy import asarray
from numpy import vstack
from keras.preprocessing.image import img_to_array
from keras.preprocessing.image import load_img
from numpy import savez_compressed

def load_images(size=(256,256)):
	src_list, tar_list = list(), list()
	inputPath = './ds-2-a/input/'
	targetPath = './ds-2-a/output/'

	for filename in listdir(inputPath):

        # Input images
		inputPix = load_img(inputPath + filename, target_size=size)
		inputPix = img_to_array(inputPix)
		inputPix = inputPix[:, :256]

        # Target images
		targetPix = load_img(targetPath + filename, target_size=size)
		targetPix = img_to_array(targetPix)
		targetPix = targetPix[:, :256]

		src_list.append(inputPix)
		tar_list.append(targetPix)

	return [asarray(src_list), asarray(tar_list)]
 
# load dataset
[src_images, tar_images] = load_images()
print('Loaded: ', src_images.shape, tar_images.shape)

# save as compressed numpy array
filename = 'dataset_256.npz'
savez_compressed(filename, src_images, tar_images)
print('Saved dataset: ', filename)