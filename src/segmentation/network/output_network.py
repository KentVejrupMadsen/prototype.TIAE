from keras.layers \
    import \
    Dense, \
    Flatten

from configuration \
    import get_maximum_of_output_labels

from segmentation.temperary \
    import \
    get_middle_network, \
    size_of_categories, \
    set_output_layer


def setup_output_layer():
    if not get_middle_network() is None:
        flattened = Flatten()(
            get_middle_network()
        )

        layer = Dense(
            get_maximum_of_output_labels(),
            name='decision_layer',
            activation='softmax',
            use_bias=True
        )(
            flattened
        )

        layer = Dense(
            get_maximum_of_output_labels() / 2,
            name='prediction',
            use_bias=False,
            activation='sigmoid'
        )(layer)

        set_output_layer(layer)
