validation_split = 0.2


def get_validation_split() -> float:
    global validation_split
    return validation_split


def set_validation_split(
        value: float
) -> None:
    global validation_split
    validation_split = value
