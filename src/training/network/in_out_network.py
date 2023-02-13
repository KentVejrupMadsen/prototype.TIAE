from keras import Input
from keras.layers import Dense, Rescaling

from src.state.configuration \
    import \
    get_categories, \
    get_image_width_size, \
    get_image_height_size, \
    get_spectrum, \
    get_batch_size

from src.training.classifying_model \
    import ClassifyModel


def generate_input(
        input_model: ClassifyModel
):
    inp_layer = Input(
            shape=
            (
                get_image_width_size(),
                get_image_height_size(),
                len(
                    get_spectrum()
                )
            ),

            batch_size=get_batch_size(),
        )

    input_model.input = inp_layer
    input_model.input = Rescaling(
        1./255,
        input_shape=(
            get_image_width_size(),
            get_image_height_size(),

            len(
                get_spectrum()
            )
        ),
        name='rescaling_input_layer'
        )(input_model.input)


def generate_output(
        output_model: ClassifyModel
):
    last_layer = Dense(
        len(
            get_categories()
        )
    )(output_model.middle_layer)
    output_model.output = last_layer

