import random

random_generator = None


def get_randomizer() -> random.SystemRandom:
    global random_generator

    if random_generator is None:
        setup()

    return random_generator


def setup() -> None:
    global random_generator
    random_generator = random.SystemRandom()


