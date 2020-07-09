from PIL import Image
from resizeimage import resizeimage
import os

i= 0
for file in os.listdir("./peinture_c_hd/"):
    #Save output image
    outputImg = Image.open(r'./peinture_c_hd/' + file)

    if(outputImg.size[0] >= 256 and outputImg.size[1] >= 256):
        outputImg = resizeimage.resize_cover(outputImg, [256, 256])
        try:
            outputImg.save('./pc-resized/' + str(i) + '.jpg', "JPEG")

            i = i + 1
        except:
            print("An exception occurred") 
    else:
        print(file)
    
    