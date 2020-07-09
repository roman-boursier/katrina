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

def getTree():
    qd = QuickDrawData()
    return qd.get_drawing("tree")

def convertToGray(im):
    fill_color = (255,255,255)  # your new background color
    im = im.convert("RGBA")   # it had mode P after DL it from OP
    if im.mode in ('RGBA', 'LA'):
        background = Image.new(im.mode[:-1], im.size, fill_color)
        background.paste(im, im.split()[-1]) # omit transparency
        im = background
    return im

def getBoundingRect(img):
    im = np.array(img) 

    im[im == 255] = 1
    im[im == 0] = 255
    im[im == 1] = 0

    im2 = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    ret,thresh = cv2.threshold(im2,0,1,0)
    contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    if(contours):
        cnt = contours[0]
        x,y,w,h = cv2.boundingRect(cnt)
        return (x,y,w,h)
    else:
        return False
    

def getAllTreesLayersFiles(folderName):
    treeFilePaths = []
    files = os.listdir(basePath + "/" + folderName)
    for name in files:
        if( (name != 'm.png') and (name != folderName + '.jpg.png')):
            treeFilePaths.append(name)

    return treeFilePaths


basePath = './dataset-preprocess'

for folder in os.listdir(basePath):
    
    treeFilePaths = getAllTreesLayersFiles(folder)
    
    #Create empty image
    backgroundFile = Image.open(basePath + "/" + folder + "/m.png")

    if(backgroundFile.size[0] >= 256 and backgroundFile.size[1] >= 256):
        new_im = Image.new('RGB', (backgroundFile.size[0],backgroundFile.size[1]),(255, 255, 255))
        #Background layer
        background = convertToGray(backgroundFile)
        new_im.paste(background, (0,0))

        for i in range(5):
            for treeFilePath in treeFilePaths:
                tree = getTree().image #Quick draw tree
                # Get x,y,w,h from tree layer
                img = convertToGray(Image.open(basePath + "/" + folder + "/" + treeFilePath))
                
                if(getBoundingRect(img)):
                    x,y,w,h = getBoundingRect(img)
                    center_coordinates = ( int((x + (x+w))/2), int((y + (y+h))/2))

                    # Resize quickdraw tree
                    newWidth = int((tree.size[0] * h) / tree.size[1])
                    tree = tree.resize((newWidth, h))

                    #Merge all layer
                    new_im.paste(tree,(center_coordinates[0],center_coordinates[1])) 


            #Save input image
            inputImg = resizeimage.resize_cover(new_im, [256, 256])
            inputImg = inputImg.convert('L')
            inputImg.save('dataset-final/input/' + folder + "-" + str(i) + ".jpg", "JPEG")

            #Save output image
            outputImg = Image.open("dataset/" + folder + ".jpg")
            outputImg = resizeimage.resize_cover(outputImg, [256, 256])
            outputImg.save('dataset-final/output/' + folder + "-" + str(i) + ".jpg", "JPEG")