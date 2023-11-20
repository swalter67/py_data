from load_image import ft_load
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import sys
import os



def main():

    try:
        path = sys.argv[1]
        if not path.lower().endswith(("jpg", "jpeg")):
            raise AssertionError("Only JPG and JPEG formats are supported.")
        if not os.path.exists(path):
            raise AssertionError("File not found:", path)


        im = Image.open(path)

        print(im.format, im.size, im.mode)

        im_rotate = im.rotate(90, expand=True)
        im_rotate = im_rotate.convert("L")
        in_rotate = im_rotate.show()
        in_rotate = im_rotate.crop((400, 100, 800, 600))


        plt.imshow(im_rotate)
        plt.axis("on")
        plt.show()

    except AssertionError as error:
        print(AssertionError.__name__ + ":", error)





if __name__ == "__main__":
    main()