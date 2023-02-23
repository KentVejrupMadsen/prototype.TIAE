# Settings
epoch: int = 1
batch_size: int = 1

full_width_of_screen: int = 1280
full_height_of_screen: int = 720

width: int = int(full_width_of_screen / 4)
height: int = int(full_height_of_screen / 4)

spectrum_label: str = 'rgb'
spectrum: int = len(spectrum_label)

size: tuple = (width, height)
full: tuple = (width, height, spectrum)

validation_size: float = 0.5

load_old_weights: bool = True
max_output_labels: int = 100


# Accessors
def get_maximum_of_output_labels() -> int:
    global max_output_labels
    return max_output_labels


def set_maximum_of_output_labels(
        value: int
) -> None:
    global max_output_labels
    max_output_labels = value



def get_spectrum_label() -> str:
    global spectrum_label
    return spectrum_label


def get_epoch() -> int:
    global epoch
    return epoch


def get_batch_size() -> int:
    global batch_size
    return batch_size


def get_image_width() -> int:
    global width
    return width


def get_image_height() -> int:
    global height
    return height


def get_color_spectrum() -> int:
    global spectrum
    return spectrum


def get_image_size() -> tuple:
    global size
    return size


def get_full_size() -> tuple:
    global full
    return full


def get_validation_size() -> float:
    global validation_size
    return validation_size


def get_load_old_weigths() -> bool:
    global load_old_weights
    return load_old_weights
