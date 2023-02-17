from keras.layers \
    import Conv2D

from configuration \
    import getColorSpectrum

from segmentation.temperary \
    import \
    get_middle_network, \
    set_middle_network, \
    get_input_layer


def setup_middle_network():
    layer = None

    if not get_input_layer() is None:
        layer = make_input_to_middle_network(64)

        set_middle_network(layer)


def make_input_to_middle_network(
        height: int
):
    return Conv2D(
        height,
        getColorSpectrum(),
        padding='same',
        activation='relu'
    )(
        get_input_layer()
    )
