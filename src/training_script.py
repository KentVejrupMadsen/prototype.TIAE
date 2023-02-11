from keras.utils \
    import image_dataset_from_directory

from tensorflow.python.data \
    import AUTOTUNE

from src.configuration \
    import \
    get_global_configuration, \
    get_seed, \
    get_training_dataset, \
    get_validation_dataset, \
    set_training_dataset, \
    set_validation_dataset, \
    set_categories


def run():
    generate_datasets()
    generate_network()
    generate_train()


def generate_datasets():
    train_dataset = image_dataset_from_directory(
        path_to_training_dataset(),
        validation_split=get_validation_split(),
        subset='training',
        seed=get_seed(),
        image_size=get_image_size(),
        batch_size=get_batch_size(),
        color_mode=get_spectrum(),
        crop_to_aspect_ratio=get_option_crop_aspect_ratio(),
        shuffle=get_option_shuffle()
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
        path_to_training_dataset(),
        validation_split=get_validation_split(),
        subset='validation',
        seed=get_seed(),
        image_size=get_image_size(),
        batch_size=get_batch_size(),
        color_mode=get_spectrum(),
        crop_to_aspect_ratio=get_option_crop_aspect_ratio(),
        shuffle=get_option_shuffle()
    )

    validation_dataset.cache().prefetch(
        buffer_size=AUTOTUNE
    )

    set_validation_dataset(
        validation_dataset
    )


def generate_network():
    pass


def generate_train():
    pass


def path_to_training_dataset() -> str:
    return get_global_configuration()['dataset']['train']['path']


def get_validation_split() -> float:
    return get_global_configuration()['training']['validation']


def get_image_size() -> tuple:
    width = get_global_configuration()['training']['image']['width']
    height = get_global_configuration()['training']['image']['height']

    return     \
        width,  \
        height


def get_batch_size() -> int:
    return get_global_configuration()['training']['batch_size']


def get_spectrum() -> str:
    return get_global_configuration()['training']['image']['spectrum']


def get_option_crop_aspect_ratio() -> bool:
    return get_global_configuration()['training']['image']['options']['keep_aspect_ratio']


def get_option_shuffle() -> bool:
    return get_global_configuration()['training']['image']['options']['shuffle']

