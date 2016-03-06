__author__ = 'srlaxminaarayanan'
import io
import os
from PIL import Image
from connection import ClassifyImages as CI
path = '/Users/srlaxminaarayanan/Pictures'
imagePath = '/Users/srlaxminaarayanan/Pictures/images'


def ProcessResult(imagepath, result):
    with open("Output.txt", "w+") as text_file:
        text_file.write("file: %s \n classification: \n %s" % (imagepath, ', '.join(result)))


def ClassifyImages():


    for root,dirs,filenames in os.walk(imagePath):
        for file in filenames:
            if file != '.DS_Store':
                imagepath = os.path.join(imagePath,file)
                image = Image.open(imagepath)
                classify_images= CI()
                ProcessResult(imagepath,classify_images.classify_image(image))

if __name__ == '__main__':
    ClassifyImages()