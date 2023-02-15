
from keras.layers \
    import \
    Dense, \
    Flatten, \
    MaxPooling2D, \
    Conv2D


def generate_middle_layer(
        model,

        kernel_size: tuple = (3, 3),
        pool_size: tuple = (2, 2),

        usage_of_bias: bool = True,
        usage_of_bias_on_first_layer: bool = False,

        start_size: int = 256,
        mid_size: int = 256,
        end_size: int = 256,

        model_depth: int = 2
):
    first_layer_in_mid = Conv2D(
        start_size,
        kernel_size,
        activation='relu',
        use_bias=usage_of_bias_on_first_layer
    )

    model.middle_layer = first_layer_in_mid(
        model.input
    )

    model.middle_layer = MaxPooling2D(pool_size)(
        model.middle_layer
    )

    next_layer_size = mid_size / 2

    model.middle_layer = Conv2D(
        next_layer_size,
        kernel_size,
        activation='relu',
        use_bias=usage_of_bias
    )(model.middle_layer)

    model.middle_layer = MaxPooling2D(
        pool_size)(model.middle_layer)

    for i in range(
            zero(),
            model_depth
    ):
        model.middle_layer = Conv2D(
            mid_size / 4,
            kernel_size,
            activation='relu',
            use_bias=usage_of_bias
        )(model.middle_layer)

    model.middle_layer = MaxPooling2D(
        pool_size)(model.middle_layer)

    model.middle_layer = Conv2D(
        mid_size / 8,
        kernel_size,
        activation='relu',
        use_bias=usage_of_bias
    )(
        model.middle_layer
    )

    model.middle_layer = MaxPooling2D(
        pool_size)(model.middle_layer)

    model.middle_layer = Flatten(
    )(model.middle_layer)

    model.middle_layer = Dense(
        end_size,
        activation='relu'
    )(model.middle_layer)


def zero() -> int:
    return 0
