from PIL import Image
from matplotlib import pyplot

# select a sample of input images
n_samples = 3
imgPathArr = []

for i in range(1,4):
	j = []
	for k in range(1,10):
		j.append('./results/' + str(i) + '/' + str(k) + '.jpg')
	imgPathArr.append(j)
		

def plotRow(imgSrc):
    img = Image.open(imgSrc)
    pyplot.axis('off')
    pyplot.imshow(img, cmap='Greys_r')


for i in range(len(imgPathArr)):
	# plot real source images
	for i in range(n_samples):
		pyplot.subplot(3, n_samples, 1 + i)
		plotRow(imgPathArr[0][i])

	# plot generated target image
	for i in range(n_samples):
		pyplot.subplot(3, n_samples, 1 + n_samples + i)
		plotRow(imgPathArr[1][i])

	# plot real target image
	for i in range(n_samples):
		pyplot.subplot(3, n_samples, 1 + n_samples*2 + i)
		plotRow(imgPathArr[2][i])

	# save plot to file
	filename1 = 'plot_%06d.png'
	pyplot.savefig(filename1)
	pyplot.close()