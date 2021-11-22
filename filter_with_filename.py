import numpy as np
from PIL import Image


def brightness_gray(image, i, j, size):
    color = np.sum(image[i: i + size, j: j + size]) // 3
    return int(color // size ** 2)


def transform_to_mosaic(image, gradation_step, size):
    for i in range(0, len(image), size):
        for j in range(0, len(image[1]), size):
            avg_brightness = brightness_gray(image, i, j, size)
            image[i: i + size, j: j + size] = np.full(3, int(avg_brightness // gradation_step) * gradation_step)
    return image


def main():
    image_file = Image.open("img2.jpg")
    arr = np.array(image_file)
    width_pixels = 10
    step = 50

    res = Image.fromarray(transform_to_mosaic(arr, step, width_pixels))
    res.save("res_new.jpg")


if __name__ == '__main__':
    main()
