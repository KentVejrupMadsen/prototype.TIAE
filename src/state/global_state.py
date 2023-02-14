from src.entropy.secure.setup_secure_random \
    import get_randomizer

from src.configuration.counter \
    import Counter


current_run_seed = None
seed_accessed = Counter()


def reset_seed() -> int:
    global current_run_seed
    current_run_seed = get_randomizer().randint(
        1,
        4294967295
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

        if seed_accessed.pass_boundary(200):
            reset_seed()

    return current_run_seed


def set_seed(
        value: int
) -> None:
    global current_run_seed
    current_run_seed = value

