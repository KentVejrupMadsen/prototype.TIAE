import matplotlib.pyplot as plt
from keras.utils import save_img
from keras_cv.models import StableDiffusion

import time


def main():
    list_physical_devices('GPU')

    model = StableDiffusion(img_width=512, img_height=512)

    model.jit_compile = True

    images = model.text_to_image("a pyramid with a sun in the background", batch_size=1)

    plot(images)


def plot(images):
    counter = 0
    for image in images:
        counter = counter + 1

        save_img(
            str("/tmp/" + str(time.time_ns()) + "." + str(counter) + ".jpg"),
            image
        )


if __name__ == '__main__':
    main()
