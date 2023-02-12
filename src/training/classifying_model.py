from keras \
    import  \
    Input,    \
    Model

from keras.layers \
    import \
    Conv2D, \
    Dense, \
    Dropout, \
    Flatten, \
    MaxPooling2D, \
    Rescaling

import os

from keras.losses \
    import SparseCategoricalCrossentropy
from keras.optimizers import Adam

from src.configuration \
    import \
    get_image_width_size, \
    get_image_height_size, \
    get_spectrum, \
    get_categories, \
    get_batch_size, \
    get_epochs, \
    get_seed, \
    get_global_configuration




class Classify:
    def __init__(
            self,
            training,
            validation
    ):
        self.model = None
        self.history = None
        self.input = None

        self.middle_layer = None
        self.output = None

        self.training = training
        self.validation = validation

        self.max_middle_layer = 6
        self.callbacks = []

        self.__make_model()
        self.is_training = True

    def __make_model(self):
        self.__make_input_layer()
        self.__make_mid_layer()
        self.__make_output_layer()
        self._make_model()

    def __make_input_layer(self):
        # Normalise input values
        inp = Input(
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
        self.input = inp
        self.input = Rescaling(
            1./255,
            input_shape=(
                get_image_width_size(),
                get_image_height_size(),
                len(
                    get_spectrum()
                )
            ),
            name='rescaling_layer'
        )(inp)

    def __make_mid_layer(self):
        min_height = get_image_height_size()

        first_layer_in_mid = Conv2D(
            min_height,
            (3, 3),
            activation='relu',
            use_bias=False
        )

        self.middle_layer = first_layer_in_mid(
            self.input
        )

        self.middle_layer = MaxPooling2D(
            2,
            2
        )(
            self.middle_layer
        )

        next_layer_size = min_height/2

        self.middle_layer = Conv2D(
            next_layer_size,
            (3, 3),
            activation='relu',
            use_bias=True
        )(self.middle_layer)

        self.middle_layer = MaxPooling2D(
            2, 2
        )(self.middle_layer)

        for i in range(
                0,
                self.max_middle_layer
        ):
            self.middle_layer = Conv2D(
                    min_height/4,
                    (3, 3),
                    activation='relu',
                    use_bias=True
            )(self.middle_layer)

        self.middle_layer = MaxPooling2D(
            2, 2
        )(
            self.middle_layer
        )

        self.middle_layer = Conv2D(
            min_height/8,
            (3, 3),
            activation='relu',
            use_bias=True
        )(
            self.middle_layer
        )

        self.middle_layer = MaxPooling2D(
            2, 2
        )(
            self.middle_layer
        )

        self.middle_layer = Flatten()(
            self.middle_layer
        )

        self.middle_layer = Dense(
            128,
            activation='relu'
        )(self.middle_layer)

    def __make_output_layer(self):
        last_layer = Dense(
            len(
                get_categories()
            ),
        )(
            self.middle_layer
        )

        self.output = last_layer

    def _compile(self):
        self.get_model().compile(
            optimizer=Adam(learning_rate=0.002),
            loss=SparseCategoricalCrossentropy(
                from_logits=True
            ),
            metrics=[
                'accuracy'
            ]
        )

    def fit_model(self):
        history = self.get_model().fit(
            self.get_train_set(),
            validation_data=self.get_validation_set(),
            epochs=get_epochs(),
            callbacks=self.callbacks
        )

        self.history = history

    def _load_old_weights(self):
        path = get_global_configuration()['tf']['checkpoint']

        is_dir = os.path.isdir(
            path
        )

        if is_dir:
            print('found checkpoint directory.')
            l = len(
                os.listdir(
                    path
                )
            )

            if l > 0:
                print('found checkpoint weights')

                self.load_saved_model(
                    path
                )

    def _make_model(self):
        self.model = Model(
            inputs=self.input,
            outputs=self.output,
            name='threat.identification'
        )

        self._compile()

        self.get_model().summary(
            show_trainable=True,
            expand_nested=True
        )

        self._load_old_weights()

    def save(
            self,
            path: str
    ):
        self.get_model().save(
            filepath=path,
            save_format='tf',
            include_optimizer=True,
            save_traces=False,
            overwrite=True
        )

    def load_saved_model(
            self,
            path: str
    ):
        print('trying to load weights file.')
        self.get_model().load_weights(
            filepath=path
        )

    def get_model(self) -> Model:
        return self.model

    def set_model(
            self,
            model: Model
    ):
        self.model = model

    def get_validation_set(self):
        return self.validation

    def get_train_set(self):
        return self.training



