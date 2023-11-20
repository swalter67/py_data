from load_image import ft_load
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import sys
import os

def main():
    """
    Image Viewer

    This program opens and displays a grayscale version of a JPG or JPEG image specified by the user.
    It utilizes the Python Imaging Library (PIL) to load the image and Matplotlib for displaying it.

    Usage:
        python3 image_viewer.py <image_path>

    Parameters:
        <image_path> (str): The path to the JPG or JPEG image file to be viewed.

    Dependencies:
        - load_image module (imported as ft_load)
        - Matplotlib (imported as plt)
        - Python Imaging Library (PIL) (imported as Image)
        - NumPy (imported as np)
        - sys
        - os

    Example:
        python3 image_viewer.py path/to/your/image.jpg

    Notes:
        - Only JPG and JPEG formats are supported.
        - The image will be displayed in grayscale.
        - The Matplotlib imshow function is used for displaying the image.
        - The program handles assertions for file format and existence.

    Reference:
        - Matplotlib imshow documentation: https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.imshow.html
    """
    try:
        path = sys.argv[1]
        if not path.lower().endswith(("jpg", "jpeg")):
            raise AssertionError("Only JPG and JPEG formats are supported.")
        if not os.path.exists(path):
            raise AssertionError("File not found:", path)

        im = Image.open(path)
        if im is None:
            raise AssertionError("Failed to load image.")


        print(ft_load(path))
        #print(im.format, im.size, im.mode)

        
        zoom = im.crop((400, 100, 800, 600))
        zoom = zoom.save("zommed_img.jpg")
        

        # #zoom.show()
        # #https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.imshow.html
        plt.imshow(zoom, cmap='gray', vmin=0, vmax=255)
        plt.axis("on")
        plt.show()
    except AssertionError as error:
        print(AssertionError.__name__ + ":", error)


if __name__ == "__main__":
    main()