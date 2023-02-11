from src.misc.list_of_test_names \
    import get_dictionary \
    as test_dictionary

from src.misc.list_of_training_names \
    import get_dictionary \
    as training_dictionary

from src.misc.list_of_production_names \
    import get_dictionary \
    as production_dictionary


name_dictionary = \
    {
        'production': production_dictionary(),
        'test': test_dictionary(),
        'training': training_dictionary()
    }


def get_dictionary() -> dict:
    global name_dictionary
    return name_dictionary

