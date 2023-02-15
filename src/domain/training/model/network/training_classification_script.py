from domain.training.callbacks \
    import CallbackFactory

from state \
    import \
    get_path_to_training_dataset, \
    get_validation_split, \
    get_seed, \
    get_standard_image_size, \
    get_batch_size, \
    set_training_dataset, \
    set_categories, \
    set_validation_dataset, \
    get_training_dataset, \
    get_validation_dataset

from domain.training.model.classifying_model \
    import ClassifyModel

from keras.utils \
    import image_dataset_from_directory

from tensorflow.python.data \
    import AUTOTUNE

from state.data.machine_learning \
    import \
    get_classify_model, \
    set_classify_model


def run():
    generate_datasets()
    generate_network()
    generate_train()


def generate_datasets():
    train_dataset = image_dataset_from_directory(
        get_path_to_training_dataset(),
        validation_split=get_validation_split(),
        subset='training',
        seed=get_seed(),
        image_size=get_standard_image_size(),
        batch_size=get_batch_size(),
        color_mode='rgba',
        crop_to_aspect_ratio=True,
        shuffle=True
    )

    train_dataset.cache().prefetch(
        buffer_size=AUTOTUNE
    )

    set_training_dataset(
        train_dataset
    )

    set_categories(
        train_dataset.class_names
    )

    validation_dataset = image_dataset_from_directory(
        get_path_to_training_dataset(),
        validation_split=get_validation_split(),
        subset='validation',
        seed=get_seed(),
        image_size=get_standard_image_size(),
        batch_size=get_batch_size(),
        color_mode='rgb',
        crop_to_aspect_ratio=True,
        shuffle=True
    )

    validation_dataset.cache().prefetch(
        buffer_size=AUTOTUNE
    )

    set_validation_dataset(
        validation_dataset
    )


def generate_network():
    model = ClassifyModel(
        training=get_training_dataset(),
        validation=get_validation_dataset()
    )

    set_classify_model(
        model
    )


def generate_indexes(
        size_of_index: int
) -> list:
    r_values = []

    for i in range(
            zero(),
            size_of_index
    ):
        r_values.append((i + one()))

    return r_values


def generate_train():
    factory = CallbackFactory(
        get_classify_model()
    )

    factory.append_early_stopper()
    factory.append_checkpoint('/tmp/checkpoint/')

    get_classify_model().fit_model()

    get_classify_model().save(
        '/tmp/model.tf/'
    )


def zero() -> int:
    return 0


def one() -> int:
    return 1
