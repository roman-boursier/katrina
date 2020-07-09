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


i = 186

for folder in os.listdir(basePath):

    inputImg = Image.open(basePath + "/" + folder + "/b.png")
    outputImg = Image.open(basePath + "/" + folder + "/" +folder + ".jpg.png", 'r')
    

    outputImg.save('dataset-final/output/' + str(i) + ".jpg", "JPEG")
    inputImg.save('dataset-final/input/' + str(i) + ".png")

    i = i +1

