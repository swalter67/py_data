import numpy as np
from PIL import Image
import os


def ft_load(path: str) -> np.ndarray:
    """
    Image Loader

    This function loads an image file from the specified
    path using the Python Imaging Library (PIL) and
    returns the image as a NumPy array.

    Args:
        path (str): The path to the image file to be loaded.

    Returns:
        np.ndarray: A NumPy array representing the image.

    Raises:
        AssertionError: If the argument is not a string,
        if the file does not exist, or if the path is not a file.

    Prints:
        Information about the shape of the loaded image
        (height, width, and layers).

    Dependencies:
        - NumPy (imported as np)
        - Python Imaging Library (PIL) (imported as Image)

    Example:
        image_path = "path/to/your/image.jpeg"
        image_array = ft_load(image_path)
        Output:
            The shape of the image is: (height, width, layers)
        Returns:
            A NumPy array representing the loaded image.

    Note:
        Make sure to install the required dependencies before
        using this function:
        pip install numpy pillow
    """
    try:
        if not isinstance(path, str):
            raise AssertionError("Invalid argument type.")
        if not os.path.exists(path):
            raise AssertionError("File does not exist.")
        if not os.path.isfile(path):
            raise AssertionError("Path is not a file.")
        if not path.endswith((".jpeg", ".jpg")):
            raise AssertionError("File is not a JPEG or JPG image.")
        img = Image.open(path)
        print(f"ths shape of image is : {img.size[1]},\
            {img.size[0]}, {img.layers}")

        img_arr = np.array(img)
        return img_arr
    except AssertionError as error:
        print(AssertionError.__name__ + ":", error)
        return ""
