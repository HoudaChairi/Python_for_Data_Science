import numpy as np
import matplotlib.pyplot as plt


def ft_invert(array: np.ndarray) -> np.ndarray:
    """
    Inverts the colors of the input image array.

    Args:
        array (np.ndarray): The image array in RGB format.

    Returns:
        np.ndarray: The inverted image array.
    """
    arr = 255 - array
    return arr


def ft_red(array: np.ndarray) -> np.ndarray:
    """
    Applies a red filter to the input image array.

    Args:
        array (np.ndarray): The image array in RGB format.

    Returns:
        np.ndarray: The filtered image array with only red channel.
    """
    filtered = array.copy()
    filtered[:, :, 1:] = 0
    return filtered


def ft_green(array: np.ndarray) -> np.ndarray:
    """
    Applies a green filter to the input image array.

    Args:
        array (np.ndarray): The image array in RGB format.

    Returns:
        np.ndarray: The filtered image array with only green channel.
    """
    filtered = array.copy()
    filtered[:, :, [0, 2]] = 0
    return filtered


def ft_blue(array: np.ndarray) -> np.ndarray:
    """
    Applies a blue filter to the input image array.

    Args:
        array (np.ndarray): The image array in RGB format.

    Returns:
        np.ndarray: The filtered image array with only blue channel.
    """
    filtered = array.copy()
    filtered[:, :, :2] = 0
    return filtered


def ft_grey(array: np.ndarray) -> np.ndarray:
    """
    Converts the input image array to grayscale.

    Args:
        array (np.ndarray): The image array in RGB format.

    Returns:
        np.ndarray: The grayscale image array.
    """
    gray = np.dot(array[..., :3], [0.2989, 0.5870, 0.1140])
    arr = np.stack((gray, gray, gray), axis=-1).astype(np.uint8)
    return arr


def display_graph(array: np.ndarray):
    """
    Displays an image from a NumPy array.

    Parameters:
    array (np.ndarray): Image data as a NumPy array.

    Shows the image without axes using Matplotlib.
    """
    plt.imshow(array)
    plt.axis('off')
    plt.show()
