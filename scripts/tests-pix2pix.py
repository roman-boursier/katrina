from keras.models import load_model
from numpy import load
from numpy import vstack
from matplotlib import pyplot
from numpy.random import randint
from numpy import expand_dims
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from numpy import asarray
import numpy as np
import matplotlib
import requests
import urllib.request
import io
from PIL import Image
import sys
import base64

basePath = '/content/drive/My Drive/Colab Notebooks/tests/'


# Load model
absToCtr = load_model(basePath + 'abs-hed.h5') #abs-to-ctr
ctrToHed = load_model(basePath + 'hed-pc.h5') #ctr-to-hed
# hedToPc = load_model(basePath + 'ds-6-a/' + 'model_011000.h5') #hed to pc

# Load input image
def predict(filename, model):
  inputPix = load_img(filename, target_size=(256,256))
  inputPix = img_to_array(inputPix)
  inputPix = inputPix[:, :256]
  inputPix = (inputPix - 127.5) / 127.5
  y = asarray([inputPix])
  gen_image = model.predict(y)
  im = gen_image.reshape((256,256,3))
  im = (im + 1) / 2.0

  return im



times = []
nbImg = []
g_loss_arr = []
num_train_arr = []
numEpoch = 1

inputPix = load_img(basePath + '/9.jpg', target_size=(256,256))
inputPix = img_to_array(inputPix)
inputPix = inputPix[:, :256]
inputPix = (inputPix - 127.5) / 127.5
y = asarray([inputPix])

import datetime

for i in range(1, 31):

  # pyplot.plot(num_train_arr, d_loss1_arr, label="d_loss1")
  # pyplot.plot(num_train_arr, d_loss2_arr, label="d_loss2")
  # pyplot.plot(num_train_arr, g_loss_arr, label="g_loss")
  a = datetime.datetime.now()
  for i in range(1, i + 1):
    absToCtr.predict(y)
    ctrToHed.predict(y)
  b = datetime.datetime.now()
  c = b - a

  times.append(c.microseconds)
  nbImg.append(i)
  #matplotlib.image.imsave(basePath + '' + str(i) + '-hed-pc.jpg', result)

# pyplot.plot(nbImg, timesGPU, label="gpu")
# pyplot.xlabel("nb img")
# pyplot.ylabel("times")
# pyplot.savefig(basePath + '/time-gpu.png', dpi=200)
# pyplot.close()

# pyplot.plot(nbImg, timesCPU, label="gpu")
# pyplot.xlabel("nb img")
# pyplot.ylabel("times")
# pyplot.savefig(basePath + '/time-cpu.png', dpi=200)
# pyplot.close()



# print(times)
# print(nbImg)