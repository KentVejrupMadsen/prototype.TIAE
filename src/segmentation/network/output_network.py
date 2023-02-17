from keras.layers \
    import GlobalAveragePooling2D, Dense

from segmentation.temperary \
    import \
    get_middle_network, \
    size_of_categories, \
    set_output_layer


def setup_output_layer():
    if not get_middle_network() is None:
        layer = GlobalAveragePooling2D()(
            get_middle_network()
        )

        layer = Dense(
            size_of_categories()
        )(layer)

        set_output_layer(layer)
