# example of loading a pix2pix model and using it for image to image translation
from keras.models import load_model
from numpy import load
from numpy import vstack
from matplotlib import pyplot
from numpy.random import randint
from numpy import expand_dims
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from numpy import asarray

# load and prepare training images
def load_real_samples(filename):
	# load compressed arrays
	data = load(filename)
	# unpack arrays
	X1, X2 = data['arr_0'], data['arr_1']
	# scale from [0,255] to [-1,1]
	X1 = (X1 - 127.5) / 127.5
	X2 = (X2 - 127.5) / 127.5
	return [X1, X2]

# plot source, generated and target images
def plot_images(src_img, gen_img):
	images = vstack((src_img, gen_img))
	# scale from [-1,1] to [0,1]
	images = (images + 1) / 2.0
	titles = ['Input', 'Generé']
	# plot images row by row
	for i in range(len(images)):
		# define subplot
		pyplot.subplot(1, 2, 1 + i)
		# turn off axis
		pyplot.axis('off')
		# plot raw pixel data
		pyplot.imshow(images[i])
		# show title
		pyplot.title(titles[i])
	pyplot.savefig('test-6.jpg')
	pyplot.close()

# load model
model = load_model('./model_007700.h5')

# Load input image and convert to numpy
inputPix = load_img('./tests/test-6.jpg', target_size=(256,256))
inputPix = img_to_array(inputPix)
inputPix = inputPix[:, :256]
inputPix = (inputPix - 127.5) / 127.5

y = asarray([inputPix])

# generate image from source
gen_image = model.predict(y)


# plot all three images
plot_images(y, gen_image)