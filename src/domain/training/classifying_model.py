from keras \
    import \
    Model

import os

from keras.losses \
    import SparseCategoricalCrossentropy

from keras.optimizers \
    import Adam

from src.domain.training.network.generate_middle_network \
    import generate_middle_layer

from src.domain.training.network.generate_in_out_network \
    import \
    generate_output, \
    generate_input


class ClassifyModel:
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

        self.callbacks = []

        self.__make_model()
        self.is_training = True

        self.epoch = 5,
        self.learning_rate = 0.002

        self.debug: bool = False
        self.expand: bool = True

    def __make_model(self):
        generate_input(self)
        generate_middle_layer(self)
        generate_output(self)

        self._make_model()

    def _compile(self):
        self.get_model().compile(
            optimizer=Adam(
                learning_rate=self.learning_rate
            ),

            loss=SparseCategoricalCrossentropy(
                from_logits=True,
            ),

            metrics=[
                'accuracy'
            ]
        )

    def fit_model(self):
        history = self.get_model().fit(
            self.get_train_set(),
            validation_data=self.get_validation_set(),
            epochs=self.epoch,
            callbacks=self.callbacks
        )

        self.history = history

    def _load_old_weights(self):
        path = '/mnt/checkpoint'

        is_dir = os.path.isdir(
            path
        )

        if is_dir:
            print('found checkpoint directory.')
            number_of_files_in_directory = len(
                os.listdir(
                    path
                )
            )

            if number_of_files_in_directory > 0:
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
            show_trainable=self.show_trainable(),
            expand_nested=self.expand
        )

        self._load_old_weights()

    def show_trainable(self):
        if self.debug:
            return True
        else:
            return False

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
