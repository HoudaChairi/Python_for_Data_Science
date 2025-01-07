from PIL import Image
import numpy as np


def ft_load(path: str) -> np.ndarray:
    """
    Loads an image from the specified path, converts it to RGB format,
    prints its shape, and returns the pixel data as a NumPy array.

    Args:
        path (str): The file path to the image.

    Returns:
        np.ndarray: The image's pixel data in RGB format as a NumPy array.

    Raises:
        Exception: If there is an error opening or processing the image.
    """
    try:
        img = Image.open(path)

        img_rgb = img.convert('RGB')

        img_array = np.array(img_rgb)

        print(f"The shape of image is: {img_array.shape}")

        return img_array

    except AssertionError as e:
        print(f"AssertionError: {e}")
    except Exception as e:
        print(f"Error loading image: {e}")
