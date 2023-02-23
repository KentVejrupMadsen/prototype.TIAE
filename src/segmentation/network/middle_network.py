from keras.layers \
    import \
    Conv2D, \
    MaxPooling2D

from configuration \
    import get_color_spectrum

from segmentation.temperary \
    import \
    set_middle_network, \
    get_input_layer


def setup_middle_network():
    layer = None

    if not get_input_layer() is None:
        layer = make_input_to_middle_network(128)
        layer = MaxPooling2D()(layer)

        layer = make_middle_network(64, layer)

        layer = MaxPooling2D((4, 4))(layer)

        set_middle_network(layer)


def make_input_to_middle_network(
        height: int
):
    return Conv2D(
        height,
        get_color_spectrum(),
        padding='same',
        activation='relu'
    )(
        get_input_layer()
    )


def make_middle_network(
        height: int,
        last_layer
):
    return Conv2D(
        height,
        get_color_spectrum(),
        padding='same',
        activation='relu'
    )(
        last_layer
    )
