__author__ = 'srlaxminaarayanan'
import io
import os
from PIL import Image
from connection import ClassifyImages as CI
import glob
path = '/Users/srlaxminaarayanan/Pictures'
imagePath = '/Users/srlaxminaarayanan/Pictures/images'


def ProcessResult(imagepath, result):
    if(os.path.exists("Output.txt")):
        with open("Output.txt", "a") as text_file:
            text_file.write("\n file: %s \n classification: \n %s \n" % (imagepath, ', '.join(result)))
    else:
        with open("Output.txt", "w+") as text_file:
            text_file.write("file: %s \n classification: \n %s" % (imagepath, ', '.join(result)))


def ClassifyImages():

    for file in glob.iglob(os.path.join(imagePath, "*.tif")):
        if file != '.DS_Store':
            imagepath = os.path.join(imagePath,file)
            image = Image.open(imagepath)
            classify_images= CI()
            ProcessResult(imagepath,classify_images.classify_image(image))

if __name__ == '__main__':
    ClassifyImages()