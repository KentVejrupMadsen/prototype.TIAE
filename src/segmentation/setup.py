from configuration \
    import \
    getDataPath, \
    getValidationSize, \
    getImageSize, \
    getBatchSize

from segmentation.temperary \
    import \
    set_training_dataset, \
    set_validation_dataset

from keras.utils \
    import image_dataset_from_directory \
    as dataset_from_directory

from random \
    import SystemRandom


def setup_segmentation_dataset():
    train_seed = SystemRandom().randint(0, 4294967295)
    validation_seed = SystemRandom().randint(0, 4294967295)

    training_set = dataset_from_directory(
        getDataPath(),
        validation_split=getValidationSize(),
        subset='training',
        image_size=getImageSize(),
        batch_size=getBatchSize(),
        seed=train_seed
    )

    set_training_dataset(
        training_set
    )

    validation_set = dataset_from_directory(
        getDataPath(),
        validation_split=getValidationSize(),
        subset='validation',
        image_size=getImageSize(),
        batch_size=getBatchSize(),
        seed=validation_seed
    )

    set_validation_dataset(
        validation_set
    )
