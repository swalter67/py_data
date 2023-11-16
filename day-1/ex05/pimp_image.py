from PIL import Image
import PIL.ImageOps 
import numpy as np
import sys
import os




def ft_invert(array):
    image = Image.open('landscape.jpg')

    inverted_image = PIL.ImageOps.invert(image)
    inverted_image.show()
    

def ft_red(array):  
    image_red = Image.open(array)
    red = image_red.convert("L")
    red= PIL.ImageOps.colorize(red, black="red", white="white")
    red.show()

def ft_green(array):
    image_green = Image.open(array)
    green = image_green.convert("L")
    green= PIL.ImageOps.colorize(green, black="green", white="white")
    green.show()

def ft_blue(array): 
    image_blue = Image.open(array)
    blue = image_blue.convert("L")
    blue= PIL.ImageOps.colorize(blue, black="blue", white="white")
    blue.show()
    

def ft_grey(array):
    image_grey = Image.open(array)
    grey = image_grey.convert("L")
    grey= PIL.ImageOps.colorize(grey, black="grey", white="white")
    grey.show()
    