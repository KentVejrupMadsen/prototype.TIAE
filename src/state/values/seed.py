from configuration \
    import Counter

from entropy \
    import get_randomizer


current_run_seed = None
seed_accessed = Counter()

seed_min = 1
seed_max = 4294967295

seed_reset_boundary = 200


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


def get_reset_boundary() -> int:
    global seed_reset_boundary
    return seed_reset_boundary


def set_reset_boundary(
        value: int
) -> None:
    global seed_reset_boundary
    seed_reset_boundary = value
