from tensorflow.python.data \
    import AUTOTUNE

from configuration \
    import \
    getDataPath, \
    getValidationSize, \
    getImageSize, \
    getBatchSize, \
    getSpectrumLabel

from segmentation.temperary \
    import \
    set_training_dataset, \
    set_validation_dataset, \
    set_training_dataset_seed, \
    set_validation_dataset_seed, \
    set_categories

from keras.utils \
    import image_dataset_from_directory \
    as dataset_from_directory

from random \
    import SystemRandom


def setup_segmentation_dataset():
    train_seed = SystemRandom().randint(
        1,
        4294967295
    )
    set_training_dataset_seed(
        train_seed
    )

    validation_seed = SystemRandom().randint(
        1,
        4294967295
    )
    set_validation_dataset_seed(
        validation_seed
    )

    training_set = dataset_from_directory(
        getDataPath(),
        validation_split=getValidationSize(),
        subset='training',
        image_size=getImageSize(),
        batch_size=getBatchSize(),
        label_mode='categorical',
        seed=train_seed,
        color_mode=getSpectrumLabel(),
        crop_to_aspect_ratio=True,
        follow_links=True
    )

    set_categories(
        training_set.class_names
    )

    set_training_dataset(
        optimise_dataset(
            training_set
        )
    )

    validation_set = dataset_from_directory(
        getDataPath(),
        validation_split=getValidationSize(),
        subset='validation',
        image_size=getImageSize(),
        batch_size=getBatchSize(),
        seed=validation_seed,
        label_mode='categorical',
        color_mode=getSpectrumLabel(),
        crop_to_aspect_ratio=True,
        follow_links=True
    )

    set_validation_dataset(
        optimise_dataset(
            validation_set
        )
    )


def optimise_dataset(dataset):
    dataset.cache()
    dataset.shuffle(
        100
    )

    dataset.prefetch(
        buffer_size=AUTOTUNE
    )

    return dataset
