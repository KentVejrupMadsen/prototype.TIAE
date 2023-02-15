from entropy.secure.setup_secure_random \
    import get_randomizer

from datetime \
    import date


def get_dictionary():
    return {}


def generate_case_name(
        environment: str = 'training'
):
    today = date.today()

    objects = get_dictionary()[
        environment
    ]

    size_of_objects = len(
        objects
    )
    last_element_index = size_of_objects - 1

    if size_of_objects == 1:
        return objects[last_element_index]

    r = get_randomizer()

    chosen = r.randint(
        0,
        last_element_index
    )

    return environment + ' : ' + \
           str(objects[chosen]) + ' : ' + \
           str(today.day) + ' - ' + \
           str(today.month)
