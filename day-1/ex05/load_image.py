import numpy as np
from PIL import Image
import os

def ft_load(path: str) -> np.ndarray:
    try:
        if not isinstance(path, str):
            raise AssertionError("Invalid argument type.")
        if not os.path.exists(path):
            raise AssertionError("File does not exist.")
        if not os.path.isfile(path):
            raise AssertionError("Path is not a file.")
        # if not path.endswith(".png"):
        #     raise AssertionError("File is not a PNG image.")
        img = Image.open(path)
        print(f"ths shape of image is : {img.size[1]}, {img.size[0]}, {img.layers}")
        img_arr = np.array(img)
        return img_arr
    except AssertionError as error:
        print(AssertionError.__name__ + ":", error)
        return ""