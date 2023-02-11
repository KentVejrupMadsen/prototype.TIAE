from src.misc.list_of_names \
    import get_dictionary

from src.secure.setup_secure_random \
    import get_randomizer

from datetime \
    import date


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


