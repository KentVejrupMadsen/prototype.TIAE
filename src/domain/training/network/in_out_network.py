from keras \
    import \
    Input

from keras.layers \
    import \
    Dense, \
    Rescaling

from src.domain.training.classifying_model \
    import ClassifyModel


def generate_input(
        input_model: ClassifyModel
):
    inp_layer = Input(
            shape=
            (
                256,
                256,
                4
            ),

            batch_size=32,
        )

    input_model.input = inp_layer
    input_model.input = Rescaling(
        1./255,
        input_shape=(
            256,
            256,
            4
        ),
        name='rescaling_input_layer'
        )(input_model.input)


def generate_output(
        output_model: ClassifyModel
):
    last_layer = Dense(
        4
    )(output_model.middle_layer)
    output_model.output = last_layer
