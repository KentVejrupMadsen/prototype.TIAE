from keras.callbacks \
    import \
    EarlyStopping, \
    ModelCheckpoint

from src.training.classifying_model \
    import ClassifyModel

from src.state.configuration \
    import get_global_configuration


class CallbackFactory:
    def __init__(
            self,
            model: ClassifyModel
    ):
        self.model = model

    def append_early_stopper(self):
        callback = EarlyStopping(
            monitor='val_loss',
            mode='min',
            verbose=1,
            patience=4
        )
        self.model.callbacks.append(
            callback
        )

    def append_checkpoint(self):
        callback = ModelCheckpoint(
            get_global_configuration()
            ['tf']
            ['checkpoint'],

            save_best_only=True,
            save_weights_only=False,

            monitor='val_accuracy',
            mode='max',

            verbose=1
        )

        self.model.callbacks.append(
            callback
        )

