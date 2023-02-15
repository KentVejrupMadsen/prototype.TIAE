from entropy.secure.setup_secure_random \
    import get_randomizer

from configuration.counter \
    import Counter

current_run_seed = None
seed_accessed = Counter()

seed_min = 1
seed_max = 4294967295

seed_reset_boundary = 200

update_dataset_online = False
validation_split = 0.2

batch_size = 32

standard_image_size = (256, 256)
categories = None

validation_dataset = None
training_dataset = None


def get_training_dataset():
    global training_dataset
    return training_dataset


def set_training_dataset(
        values
):
    global training_dataset
    training_dataset = values


def get_validation_dataset():
    global validation_dataset
    return validation_dataset


def set_validation_dataset(
        values
):
    global validation_dataset
    validation_dataset = values


def get_categories():
    global categories
    return categories


def set_categories(
        values
):
    global categories
    categories = values


def get_standard_image_size() -> tuple:
    global standard_image_size
    return standard_image_size


def set_standard_image_size(
        value: tuple
) -> None:
    global standard_image_size
    standard_image_size = value


def get_batch_size() -> int:
    global batch_size
    return batch_size


def set_batch_size(value: int) -> None:
    global batch_size
    batch_size = value


def get_validation_split() -> float:
    global validation_split
    return validation_split


def set_validation_split(value: float) -> None:
    global validation_split
    validation_split = value


def get_update_dateset_online() -> bool:
    global update_dataset_online
    return update_dataset_online


def set_update_dataset_online(value: bool) -> None:
    global update_dataset_online
    update_dataset_online = value


def get_reset_boundary() -> int:
    global seed_reset_boundary
    return seed_reset_boundary


def set_reset_boundary(
        value: int
) -> None:
    global seed_reset_boundary
    seed_reset_boundary = value


def get_seed_min() -> int:
    global seed_min
    return seed_min


def set_seed_min(
        value: int
) -> None:
    global seed_min
    seed_min = value


def get_seed_max() -> int:
    global seed_max
    return seed_max


def set_seed_max(
        value: int
):
    global seed_max
    seed_max = value


def reset_seed() -> int:
    global current_run_seed

    current_run_seed = get_randomizer().randint(
        get_seed_min(),
        get_seed_max()
    )

    return current_run_seed


def get_seed() -> int:
    global \
        current_run_seed, \
        seed_accessed

    if current_run_seed is None:
        return reset_seed()
    else:
        seed_accessed.increment()

        if seed_accessed.pass_boundary(
                get_reset_boundary()
        ):
            reset_seed()

    return current_run_seed


def set_seed(
        value: int
) -> None:
    global current_run_seed
    current_run_seed = value


train_path = r'/mnt/c/Workspace/TIAE/datasets/training-set'


def get_path_to_training_dataset() -> str:
    global train_path
    return train_path


def set_path_to_training_dataset(
        value: str
) -> None:
    global train_path
    train_path = value


validate_path = None


def get_path_to_validation_dataset() -> str:
    global validate_path
    return validate_path


def set_path_to_validation_dataset(
        value: str
) -> None:
    global validate_path
    validate_path = value
