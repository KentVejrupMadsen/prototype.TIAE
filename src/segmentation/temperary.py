from keras \
    import Model

training_dataset = None
training_dataset_seed = None

validation_dataset = None
validation_dataset_seed = None

categories = None

input_layer = None
output_layer = None
middle_network = None

model = None

history = None


def get_history():
    global history
    return history


def set_history(
        value
):
    global history
    history = value


def get_categories():
    global categories
    return categories


def set_categories(
        value
):
    global categories
    categories = value


def size_of_categories() -> int:
    global categories
    return len(categories)


def get_model() -> Model:
    global model
    return model


def set_model(
        v: Model
):
    global model
    model = v


def get_input_layer():
    global input_layer
    return input_layer


def set_input_layer(
        v
):
    global input_layer
    input_layer = v


def get_output_layer():
    global output_layer
    return output_layer


def set_output_layer(
        v
):
    global output_layer
    output_layer = v


def get_middle_network():
    global middle_network
    return middle_network


def set_middle_network(
        v
):
    global middle_network
    middle_network = v


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
        var
):
    global validation_dataset
    validation_dataset = var


def get_training_dataset_seed() -> int:
    global training_dataset_seed
    return training_dataset_seed


def set_training_dataset_seed(
        value: int
) -> None:
    global training_dataset_seed
    training_dataset_seed = value


def get_validation_dataset_seed() -> int:
    global validation_dataset_seed
    return validation_dataset_seed


def set_validation_dataset_seed(
        value: int
) -> None:
    global validation_dataset_seed
    validation_dataset_seed = value
