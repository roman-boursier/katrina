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

# Load and prepare training images
def load_real_samples(filename):
	# load compressed arrays
	data = load(filename)
	# unpack arrays
	X1, X2 = data['arr_0'], data['arr_1']
	# scale from [0,255] to [-1,1]
	X1 = (X1 - 127.5) / 127.5
	X2 = (X2 - 127.5) / 127.5
	return [X1, X2]

# Plot input, genrated image and final image
def plot_images(src_img, gen_img, final_img):
	images = vstack((src_img, gen_img, final_img))

	# scale from [-1,1] to [0,1]
	images = (images + 1) / 2.0
	titles = ['Input', 'Generé', 'Transfert de style']
	# plot images row by row
	for i in range(len(images)):
		# define subplot
		pyplot.subplot(1, 3, 1 + i)
		# turn off axis
		pyplot.axis('off')
		# plot raw pixel data
		pyplot.imshow(images[i])
		# show title
		pyplot.title(titles[i])
	pyplot.savefig('test-10-b.jpg')
	pyplot.close()

# Load model
model = load_model('./model_008700.h5')

# Load input image
inputFile = sys.argv[1]

inputPix = load_img(inputFile, target_size=(256,256))
inputPix = img_to_array(inputPix)
inputPix = inputPix[:, :256]
inputPix = (inputPix - 127.5) / 127.5

# Generate output from model
y = asarray([inputPix])
gen_image = model.predict(y)

# Apply neural style transfert with deep ai api
im = gen_image.reshape((256,256,3))
im = (im + 1) / 2.0
matplotlib.image.imsave('generate-img.jpg', im)
r = requests.post(
    "https://api.deepai.org/api/CNNMRF",
    files={
        'content': open('generate-img.jpg', 'rb'),
        'style': open('styles/style-2.png', 'rb'),
    },
    headers={'api-key': '3298f659-e5c9-49be-954a-294d02934463'}
)
finalImgUrl = r.json().get('output_url')

with urllib.request.urlopen(finalImgUrl) as url:
    f = io.BytesIO(url.read())

finalImg = Image.open(f)
finalImg = finalImg.resize((256,256))
finalImg = img_to_array(finalImg)
finalImg = np.expand_dims(finalImg, axis=0)
finalImg = (finalImg - 127.5) / 127.5

# plot all three images
plot_images(y, gen_image, finalImg)