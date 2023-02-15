validation_dataset = None


def get_validation_dataset():
    global validation_dataset
    return validation_dataset


def set_validation_dataset(
        values
):
    global validation_dataset
    validation_dataset = values


training_dataset = None


def get_training_dataset():
    global training_dataset
    return training_dataset


def set_training_dataset(
        values
):
    global training_dataset
    training_dataset = values
