# Settings
epoch: int = 10
batch_size: int = 32

width: int = 512
height: int = 512

spectrum_label: str = 'rgba'
spectrum: int = len(spectrum_label)

size: tuple = (width, height)
full: tuple = (width, height, spectrum)

validation_size: float = 0.40

load_old_weights: bool = True


# Accessors
def getSpectrumLabel() -> str:
    global spectrum_label
    return spectrum_label


def getEpoch() -> int:
    global epoch
    return epoch


def getBatchSize() -> int:
    global batch_size
    return batch_size


def getImageWidth() -> int:
    global width
    return width


def getImageHeight() -> int:
    global height
    return height


def getColorSpectrum() -> int:
    global spectrum
    return spectrum


def getImageSize() -> tuple:
    global size
    return size


def getFullSize() -> tuple:
    global full
    return full


def getValidationSize() -> float:
    global validation_size
    return validation_size


def getLoadOldWeigths() -> bool:
    global load_old_weights
    return load_old_weights
