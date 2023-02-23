from keras.callbacks \
    import \
    EarlyStopping, \
    BackupAndRestore, \
    ReduceLROnPlateau
from keras.utils import array_to_img

from wandb.integration.keras \
    import WandbCallback

from configuration \
    import \
    get_epoch, \
    get_model_path

from segmentation.temperary \
    import \
    get_training_dataset, \
    get_validation_dataset, \
    get_model, \
    set_history

from os \
    import listdir

from os.path \
    import isdir


def train() -> None:
    callbacks = []

    callbacks.append(
        WandbCallback(
            save_model=False,
            save_weights_only=False,

            save_graph=True,

            log_weights=True,
            log_gradients=True,

            training_data=get_training_dataset(),
            validation_data=get_validation_dataset()
        )
    )

    callbacks.append(
        EarlyStopping(
            monitor='loss',
            patience=4,
            mode="auto"
        )
    )

    callbacks.append(
        BackupAndRestore(
            '/tmp/backup.tf',
            save_freq='epoch',
            delete_checkpoint=True,
            save_before_preemption=False
        )
    )

    callbacks.append(
        ReduceLROnPlateau(
            monitor='loss',
            factor=0.25,
            patience=2,
            min_lr=0.0015,
            verbose=1
        )
    )

    model = get_model()

    files_in = None

    if isdir(get_model_path()):
        files_in = listdir(
            get_model_path()
        )

    if not (files_in is None) and \
            not (len(files_in) == 0):
        model.load_weights(
            get_model_path()
        )

    history = model.fit(
        get_training_dataset(),
        validation_data=get_validation_dataset(),
        epochs=get_epoch(),
        callbacks=callbacks
    )

    print(get_model().get_output_at(0))

    set_history(
        history
    )

    model.save(
        get_model_path(),
        overwrite=True,
        save_format='tf'
    )
