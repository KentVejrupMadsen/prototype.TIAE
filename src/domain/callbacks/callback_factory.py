from keras.callbacks \
    import \
    EarlyStopping, \
    ModelCheckpoint

from src.domain.training.classifying_model \
    import ClassifyModel


class CallbackFactory:
    def __init__(
            self,
            model: ClassifyModel
    ):
        self.model = model

    def append_early_stopper(
            self,
            verbose: int = 1,
            patience: int = 4
    ):
        callback = EarlyStopping(
            monitor='val_loss',
            mode='min',
            verbose=verbose,
            patience=patience
        )

        self.model.callbacks.append(
            callback
        )

    def append_checkpoint(
            self,
            path_to_checkpoint: str,
            verbose: int = 0,
            save_best_only: bool = True,
            save_weights_only: bool = False,
    ):
        callback = ModelCheckpoint(
            path_to_checkpoint,

            save_best_only=save_best_only,
            save_weights_only=save_weights_only,

            monitor='val_accuracy',
            mode='max',

            verbose=verbose
        )

        self.model.callbacks.append(
            callback
        )
