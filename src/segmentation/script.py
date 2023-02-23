from keras \
    import Model

from keras.losses \
    import SparseCategoricalCrossentropy

from segmentation.setup \
    import setup_segmentation_dataset

from segmentation.network \
    import \
    setup_input_layer, \
    setup_output_layer, \
    setup_middle_network

from segmentation.temperary \
    import \
    get_output_layer, \
    get_input_layer, \
    set_model

from segmentation.training \
    import train


def create_model() -> None:
    setup_input_layer()
    setup_middle_network()
    setup_output_layer()

    model = Model(
        inputs=get_input_layer(),
        outputs=get_output_layer(),
        name='classify-example'
    )

    model.compile(
        optimizer='adam',

        loss=SparseCategoricalCrossentropy(
            from_logits=False
        ),

        metrics=['accuracy']
    )

    model.summary()

    set_model(model)


def run() -> None:
    setup_segmentation_dataset()
    create_model()
    train()
