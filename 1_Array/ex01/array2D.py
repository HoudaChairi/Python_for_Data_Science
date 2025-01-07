import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """
        Slices a 2D list based on given start and end indices.

        Args:
            family (list): A 2D list to slice.
            start (int): Starting index (inclusive).
            end (int): Ending index (exclusive).

        Returns:
            list: A sliced 2D list.

        Prints:
            - Shape of the original and sliced arrays.
    """
    try:
        array = np.array(family)

        print(f"My shape is : {array.shape}")

        sliced_array = array[start:end]

        print(f"My new shape is : {sliced_array.shape}")

        return sliced_array.tolist()

    except AssertionError as e:
        print(f"AssertionError: {e}")
