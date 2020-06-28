# Create pairs input/output from multiple layers
# The first layer correspond to mountain sketch
# The others define the area where the trees are located. After we use google quick draw sketches to place tree drawing.

from PIL import Image
import numpy as np
import cv2
from quickdraw import QuickDrawData
from resizeimage import resizeimage
import math
import os
import shutil
from os import path 

basePath = './dataset'

def draw_edges(imagePath):
    img = cv2.imread(imagePath,0)
    edges = cv2.Canny(img,100,200)
    return cv2.bitwise_not(edges)

for file in os.listdir('dataset/output'):

    inputImage = draw_edges('dataset/output/' + file)
    cv2.imwrite('./dataset/input/'+ file, inputImage) 


