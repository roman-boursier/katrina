from PIL import Image
import numpy as np
import cv2
from quickdraw import QuickDrawData
from resizeimage import resizeimage
import math
import os
import shutil
from os import path 
import cv2
import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import numpy as np
import cv2
import matplotlib
import numpy as np
import matplotlib.pyplot as plt

from scipy.interpolate import splprep, splev

def smoothCtr(contours):
    smoothened = []
    for contour in contours:
        x,y = contour.T
        # Convert from numpy arrays to normal arrays
        x = x.tolist()[0]
        y = y.tolist()[0]
        # https://docs.scipy.org/doc/scipy-0.14.0/reference/generated/scipy.interpolate.splprep.html
        tck, u = splprep([x,y], u=None, s=1.0, per=1)
        # https://docs.scipy.org/doc/numpy-1.10.1/reference/generated/numpy.linspace.html
        u_new = np.linspace(u.min(), u.max(), 25)
        # https://docs.scipy.org/doc/scipy-0.14.0/reference/generated/scipy.interpolate.splev.html
        x_new, y_new = splev(u_new, tck, der=0)
        # Convert it back to numpy format for opencv to be able to display it
        res_array = [[[int(i[0]), int(i[1])]] for i in zip(x_new,y_new)]
        smoothened.append(np.asarray(res_array, dtype=np.int32))
    
    return smoothened

def toContour(imagePath, nb):
    #Empty image
    ctr = np.zeros((256, 256, 3), np.uint8)
    ctr[:] = (255, 255, 255)

    image = cv2.imread(imagePath) 
    #gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 

    
    #gray = cv2.GaussianBlur(gray,(13,13), 0)
    kernel = np.ones((2,2), np.uint8)
    gray = cv2.erode(gray, kernel, iterations=1)

    ret, thresh = cv2.threshold(gray, 200, 255, 0)

    #contours, hierarchy = cv2.findContours(thresh, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)

    # for i in range(len(contours)):
    #     #hull = cv2.convexHull(contours[i])
    #     peri=cv2.arcLength(contours[i], closed=True) 
    #     dp = cv2.approxPolyDP(contours[i],  0.001 * peri, 5, True)
    #     cv2.drawContours(ctr, [dp], -1, (0, 0, 0), 2)

    
    # contours, hierarchy = cv2.findContours(thresh, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE) 
    # edges = cv2.Canny(thresh, 180,255)
    # edges = cv2.bitwise_not(edges)

    #cv2.drawContours(ctr, contours, -1, (0, 0, 0), 2)


    return thresh


def toPoint(imgPath, nb):
    img  =	cv2.imread(imgPath)
    gray =	cv2.cvtColor(img,	cv2.COLOR_BGR2GRAY)
    gray =	np.float32(gray)
    dst  =	cv2.cornerHarris(gray,	2,11, nb)
    img[dst>0.01 *	dst.max()]   =	[0,	0,	255]
    
    cv2.imshow(imgPath + '-' + str(random.Random()),	img)
    
    return img
    cv2.imshow(imgPath,	img)


BasePath = '../datasets/'
FullPath = BasePath + 'test/'
from PIL import Image 

import os.path

for file in os.listdir(FullPath):

    # toContour(BasePath + 'ds-10-abs/output/38.jpg', 0.012)

    #gray = cv2.bitwise_not(gray)
    #inputImage = draw_edges('./ds-7-a/' + file)
    
    #inputImage = cv2.imread('../datasets/ds-8-sketch-coutour/output/'+ file, cv2.COLOR_BGR2GRAY) 

     
    # if not os.path.exists(BasePath + 'ds-12-abs-hed/input/' + file) :
    #     os.remove(BasePath + 'ds-12-abs-hed/output/' + file)
    #     print(file)
    # else:
    inputImage = toContour(FullPath + file, 0.01)
    cv2.imwrite(BasePath + FullPath + file, inputImage)




