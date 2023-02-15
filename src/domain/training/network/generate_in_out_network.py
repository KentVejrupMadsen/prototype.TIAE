from keras \
    import \
    Input

from keras.layers \
    import \
    Dense, \
    Rescaling

from domain.training \
    import ClassifyModel


def generate_input(
        input_model: ClassifyModel,
        input_shape: tuple = (256, 256, 3),
        batch_size: int = 32,
        scale_factor: float = 1./255
):
    inp_layer = Input(
            shape=input_shape,
            batch_size=batch_size,
        )

    input_model.input = inp_layer
    input_model.input = Rescaling(
        scale_factor,
        input_shape=input_shape,
        name='rescaling_input_layer'
        )(input_model.input)


def generate_output(
        output_model: ClassifyModel,
        category_size: int = 4
):
    last_layer = Dense(
        category_size
    )(output_model.middle_layer)
    output_model.output = last_layer
