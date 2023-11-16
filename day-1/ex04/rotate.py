from load_image import ft_load
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import sys
import os

im = Image.open("animal.jpeg")

print(im.format, im.size, im.mode)

im_rotate = im.rotate(90, expand=True)
im_rotate = im_rotate.convert("L")
in_rotate = im_rotate.show()
in_rotate = im_rotate.crop((400, 100, 800, 600))


plt.imshow(im_rotate)
plt.axis("on")
plt.show()