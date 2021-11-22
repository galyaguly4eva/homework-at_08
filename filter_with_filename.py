import numpy as np
from PIL import Image


def brightness_gray(arr, i, j, width_pixels):
    color = np.sum(arr[i: i + width_pixels, j: j + width_pixels]) // 3
    return int(color // width_pixels ** 2)


def transform_to_mosaic(arr, step, width_pixels):
    for i in range(0, len(arr), width_pixels):
        for j in range(0, len(arr[1]), width_pixels):
            avg_brightness = brightness_gray(arr, i, j, width_pixels)
            arr[i: i + width_pixels, j: j + width_pixels] = np.full(3, int(avg_brightness // step) * step)
    return arr


def main():
    image_file = Image.open("img2.jpg")
    arr = np.array(image_file)
    width_pixels = 10
    step = 50

    res = Image.fromarray(transform_to_mosaic(arr, step, width_pixels))
    res.save("res_new.jpg")


if __name__ == '__main__':
    main()
