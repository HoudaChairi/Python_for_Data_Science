from load_image import ft_load
import numpy as np
import matplotlib.pyplot as plt


def main():
    """
    This script loads an image, slices it to 400x400 pixels,
    converts it to grayscale, and transposes it.
    The result is displayed as a grayscale image.
    """
    img_loaded = ft_load("animal.jpeg")

    sliced_img = img_loaded[:400, :400, :1]

    print(f"The shape of image is: {sliced_img.shape}")
    print(sliced_img)

    img_2d = sliced_img.squeeze()

    rows = len(img_2d)
    cols = len(img_2d[0])

    transposed_img = np.array([
        [img_2d[i][j] for i in range(rows)]
        for j in range(cols)
        ])

    print(f"New shape after Transpose: {transposed_img.shape}")
    print(transposed_img)

    plt.imshow(transposed_img, cmap='gray')
    plt.axis('off')
    plt.show()


if __name__ == '__main__':
    main()
