batch_size = 32
standard_image_size = (256, 256)



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
