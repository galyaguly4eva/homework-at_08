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


file_name = input("Введите имя файла, который надо преобразовать ")
res_name = input("Введите имя файла, куда надо сохранить измененную картинку ")
width_pixels = int(input("Введите размер мозаики "))
step = int(input("Введите количество градаций "))

img = Image.open(file_name)
arr = np.array(img)

arr = transform_to_mosaic(arr, step, width_pixels)

res = Image.fromarray(arr)
res.save(res_name)
