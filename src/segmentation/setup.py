from tensorflow.python.data \
    import AUTOTUNE

from configuration \
    import \
    get_data_path, \
    get_validation_size, \
    get_image_size, \
    get_batch_size, \
    get_spectrum_label, \
    set_maximum_of_output_labels

from segmentation.temperary \
    import \
    set_training_dataset, \
    set_validation_dataset, \
    set_training_dataset_seed, \
    set_validation_dataset_seed, \
    set_categories, \
    get_training_dataset_seed, \
    get_validation_dataset_seed

from keras.utils \
    import image_dataset_from_directory \
    as dataset_from_directory

from random \
    import SystemRandom


def setup_seeds():
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


def setup_segmentation_dataset():
    setup_seeds()

    training_set = dataset_from_directory(
        get_data_path(),
        validation_split=get_validation_size(),
        subset='training',
        image_size=get_image_size(),
        batch_size=get_batch_size(),
        seed=get_training_dataset_seed(),
        color_mode=get_spectrum_label(),
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
        get_data_path(),
        validation_split=get_validation_size(),
        subset='validation',
        image_size=get_image_size(),
        batch_size=get_batch_size(),
        seed=get_validation_dataset_seed(),
        color_mode=get_spectrum_label(),
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
        250
    )

    dataset.prefetch(
        buffer_size=AUTOTUNE
    )

    return dataset
