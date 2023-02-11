import json
import os

from os.path \
    import join

from src.secure.setup_secure_random \
    import get_randomizer

import sys

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
            sys.maxsize - 2
        )

        print(
            str(
                seed
            )
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
        'config.json'
    )

    open_file = open(path_to_config)

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


def get_categories():
    global categories
    return categories


def set_categories(value):
    global categories
    categories = value