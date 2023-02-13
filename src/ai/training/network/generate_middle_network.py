from keras.layers import Dense, Flatten, MaxPooling2D, Conv2D

from src.state.configuration import get_image_height_size
from src.ai.training.classifying_model \
    import ClassifyModel

middle_layer_size = 6


def get_middle_layer_size() -> int:
    global middle_layer_size
    return middle_layer_size


def generate_middle_layer(
        model: ClassifyModel
):
        min_height = get_image_height_size()

        first_layer_in_mid = Conv2D(
            min_height,
            (3, 3),
            activation='relu',
            use_bias=False
        )

        model.middle_layer = first_layer_in_mid(
            model.input
        )

        model.middle_layer = MaxPooling2D(
            2,
            2
        )(
            model.middle_layer
        )

        next_layer_size = min_height / 2

        model.middle_layer = Conv2D(
            next_layer_size,
            (3, 3),
            activation='relu',
            use_bias=True
        )(model.middle_layer)

        model.middle_layer = MaxPooling2D(
            2, 2
        )(model.middle_layer)

        for i in range(
                0,
                get_middle_layer_size()
        ):
            model.middle_layer = Conv2D(
                min_height / 4,
                (3, 3),
                activation='relu',
                use_bias=True
            )(model.middle_layer)

        model.middle_layer = MaxPooling2D(
            2, 2
        )(
            model.middle_layer
        )

        model.middle_layer = Conv2D(
            min_height / 8,
            (3, 3),
            activation='relu',
            use_bias=True
        )(
            model.middle_layer
        )

        model.middle_layer = MaxPooling2D(
            2, 2
        )(
            model.middle_layer
        )

        model.middle_layer = Flatten()(
            model.middle_layer
        )

        model.middle_layer = Dense(
            128,
            activation='relu'
        )(model.middle_layer)
