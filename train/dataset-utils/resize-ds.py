from PIL import Image
from resizeimage import resizeimage
import os

i= 0
for file in os.listdir("./dataset"):
    #Save output image
    outputImg = Image.open(r'./dataset/' + file)

    if(outputImg.size[0] >= 256 and outputImg.size[1] >= 256):
        outputImg = resizeimage.resize_cover(outputImg, [256, 256])
        outputImg.save('./dataset-new/' + str(i) + '.jpg', "JPEG")

        i = i + 1
    else:
        print(file)
    
    