import json
import os

from os.path \
    import join

from src.secure.setup_secure_random \
    import get_randomizer

global_configuration = None
seed = 0

categories = None

training_dataset = None
validation_dataset = None


def get_training_dataset():
    global training_dataset
    return training_dataset


def set_training_dataset(
        value
):
    global training_dataset
    training_dataset = value


def get_validation_dataset():
    global validation_dataset
    return validation_dataset


def set_validation_dataset(
        value
):
    global validation_dataset
    validation_dataset = value


def get_seed() -> int:
    global seed

    if seed == 0:
        seed = get_randomizer().randint(
            1,
            4294967295
        )

    return seed


def set_seed(
        value: int
) -> None:
    global seed
    seed = value


def load_configuration():
    global global_configuration

    path_to_config = join(
        os.getcwd(),
        'configurations'
    )

    path_to_config = join(
        path_to_config,
        '../../configurations/config.json'
    )

    open_file = open(
        path_to_config
    )

    loaded_data = json.load(
        open_file
    )
    global_configuration = loaded_data

    open_file.close()


def get_global_configuration() -> dict:
    global global_configuration

    if global_configuration is None:
        load_configuration()

    return global_configuration


def get_epochs():
    return get_global_configuration()[
        'training'
    ][
        'epoch'
    ]


def get_categories():
    global categories
    return categories


def set_categories(
        value
):
    global categories
    categories = value


def path_to_training_dataset() -> str:
    return \
        join(
            get_global_configuration()['dataset']['root'],
            get_global_configuration()['dataset']['train']['path']
        )


def get_validation_split() -> float:
    return get_global_configuration()[
        'training'
    ][
        'validation'
    ]


def get_image_size() -> tuple:
    return     \
        get_image_width_size(),  \
        get_image_height_size()


def get_image_width_size() -> int:
    return get_global_configuration()[
        'training'
    ][
        'image'
    ][
        'width'
    ]


def get_image_height_size() -> int:
    return get_global_configuration()[
        'training'
    ][
        'image'
    ][
        'height'
    ]


def get_batch_size() -> int:
    return get_global_configuration()[
        'training'
    ][
        'batch_size'
    ]


def get_spectrum() -> str:
    return get_global_configuration()[
        'training'
    ][
        'image'
    ][
        'spectrum'
    ]


def get_option_crop_aspect_ratio() -> bool:
    return get_global_configuration()[
        'training'
    ][
        'image'
    ][
        'options'
    ][
        'keep_aspect_ratio'
    ]


def get_option_shuffle() -> bool:
    return get_global_configuration()[
        'training'
    ][
        'image'
    ][
        'options'
    ][
        'shuffle'
    ]


def get_train_path() -> str:
    return get_global_configuration()[
        'dataset'
    ][
        'train'
    ][
        'path'
    ]


def get_update_state() -> bool:
    r = get_global_configuration()[
        'dataset'
    ][
        'updatable'
    ]

    return r

