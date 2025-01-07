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
        if type(family) is not list:
            raise TypeError("Input must be a list.")
        if len(family) == 0:
            raise ValueError("List is empty.")

        for row in family:
            if type(row) is not list:
                raise TypeError("Each element of the list must be a list.")

        first_row_length = len(family[0])
        for row in family:
            if len(row) != first_row_length:
                raise ValueError("All inner lists must be of the same size.")

        array = np.array(family)

        print(f"My shape is : {array.shape}")

        sliced_array = array[start:end]

        print(f"My new shape is : {sliced_array.shape}")

        return sliced_array.tolist()

    except AssertionError as e:
        print(f"AssertionError: {e}")
