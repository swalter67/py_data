from load_image import ft_load
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import sys
import os

im = Image.open("animal.jpeg")

print(im.format, im.size, im.mode)

im = im.convert("L")




zoom = im.crop((400, 100, 800, 600))


zoom.show()


plt.imshow(zoom)
plt.axis("on")


plt.show()