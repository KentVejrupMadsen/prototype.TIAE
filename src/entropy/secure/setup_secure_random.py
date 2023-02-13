import random

random_generator = None


def set_randomizer(
        generator: random.SystemRandom
) -> None:
    global random_generator
    random_generator = generator


def get_randomizer() -> random.SystemRandom:
    global random_generator

    if random_generator is None:
        setup()

    return random_generator


def setup() -> None:
    global random_generator

    set_randomizer(
        random.SystemRandom()
    )


