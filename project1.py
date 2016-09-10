#Author:  Brandon Avery
#Class:  CST-205
#Date:  9-9-16
#Abstract:  Image filter based on median of pixels from 9 images
#Github link:  https://github.com/branAve/CST205Proj1

#import statements
import os
import io
import PIL
from PIL import Image
from statistics import median

#open and load images
pic1 = Image.open("C:/Users/Brandon/Pictures/CST205proj1pics/1.png")
pic1.load()
pic2 = Image.open("C:/Users/Brandon/Pictures/CST205proj1pics/2.png")
pic2.load()
pic3 = Image.open("C:/Users/Brandon/Pictures/CST205proj1pics/3.png")
pic3.load()
pic4 = Image.open("C:/Users/Brandon/Pictures/CST205proj1pics/4.png")
pic4.load()
pic5 = Image.open("C:/Users/Brandon/Pictures/CST205proj1pics/5.png")
pic5.load()
pic6 = Image.open("C:/Users/Brandon/Pictures/CST205proj1pics/6.png")
pic6.load()
pic7 = Image.open("C:/Users/Brandon/Pictures/CST205proj1pics/7.png")
pic7.load()
pic8 = Image.open("C:/Users/Brandon/Pictures/CST205proj1pics/8.png")
pic8.load()
pic9 = Image.open("C:/Users/Brandon/Pictures/CST205proj1pics/9.png")
pic9.load()

#set variables
width=495
height=557

imgList = [pic1,pic2,pic3,pic4,pic5,pic6,pic7,pic8,pic9]

picFinal=Image.new("RGB",(width,height))
picFinaldata=picFinal.load()

#calculate median of each pixel location and assign it to new image
for x in range(0, width):
    for y in range(0,height):
        redPixel=[]
        greenPixel=[]
        bluePixel=[]
        for myImage in imgList:
            myRed, myGreen, myBlue = myImage.getpixel((x,y))
            redPixel.append(myRed)
            greenPixel.append(myGreen)
            bluePixel.append(myBlue)
        sorted(redPixel)
        sorted(greenPixel)
        sorted(bluePixel)

        picFinaldata[x,y]=(int(median(redPixel)),int(median(greenPixel)),int(median(bluePixel)))

#display picture
picFinal.show()


