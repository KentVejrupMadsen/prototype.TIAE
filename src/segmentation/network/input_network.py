from keras import Input
from keras.layers \
    import Rescaling

from configuration \
    import \
    getImageWidth, \
    getImageHeight, \
    getColorSpectrum

from segmentation.temperary \
    import set_input_layer


def setup_input_layer():
    input = None

    input = make_input()
    input = make_scaling()(input)

    set_input_layer(
        input
    )


def make_scaling():
    rVal = Rescaling(
        1. / 255
    )

    return rVal


def make_input():
    return Input(
        shape=(
            getImageWidth(),
            getImageHeight(),
            getColorSpectrum()
        )
    )
