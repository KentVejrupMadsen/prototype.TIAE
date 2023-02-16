training_dataset = None
validation_dataset = None


def get_training_dataset():
    global training_dataset
    return training_dataset


def set_training_dataset(value):
    global training_dataset
    training_dataset = value


def get_validation_dataset():
    global validation_dataset
    return validation_dataset


def set_validation_dataset(var):
    global validation_dataset
    validation_dataset = var
