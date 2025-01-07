from load_image import ft_load
import matplotlib.pyplot as plt


def main():
    """
    Main function to load an image, slice the first 400x400 pixels,
    convert it to grayscale, and display it using matplotlib.
    """
    try:
        img_loaded = ft_load("animal.jpeg")

        print(img_loaded)

        sliced_img = img_loaded[:400, :400, :1]

        print(f"New shape after slicing: {sliced_img.shape}")
        print(sliced_img)

        plt.imshow(sliced_img.squeeze(), cmap='gray')
        plt.axis('off')
        plt.show()

    except AssertionError as e:
        print(f"AssertionError: {e}")


if __name__ == '__main__':
    main()
