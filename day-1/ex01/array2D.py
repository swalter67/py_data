import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """
    https://numpy.org/doc/stable/reference/arrays.html
    Slice Me
    This function slices a list of lists
    (representing a family of arrays) using specified start and end indices.
    Args:
        family (list): A list of lists (family of arrays) to be sliced.
        start (int): The starting index for slicing.
        end (int): The ending index for slicing.
    Returns:
        list: A sliced list of lists based on
        the specified start and end indices.
    Raises:
        AssertionError: If the input is not
        a list, or if start and end indices are not integers,
        or if the lists in the input have different sizes.
    Prints:
        Information about the shape of the
        original and sliced arrays using NumPy.
    Example:
        family = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        result = slice_me(family, 1, 2)
    Output:
        My shape is: (3, 3)
        My new shape is: (2, 3)
    Returns:
        [[4, 5, 6], [7, 8, 9]]
    """

    try:
        if not isinstance(family, list) or not isinstance(start, int)\
                or not isinstance(end, int):
            raise AssertionError("Input must be a list and 2 integer.")
        if not all(len(item) == len(family[0]) for item in family):
            raise AssertionError("Input list with different sizes.")
        print(f"My shape is : {np.array(family).shape}")
        print(f"My new shape is : {np.array(family)[start:end+1].shape}")
        return np.array(family)[start:end].tolist()
    except AssertionError as error:
        print("\033[31m", AssertionError.__name__ + ":", error, "\033[0m")
        return ""
