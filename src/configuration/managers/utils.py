from os.path \
    import \
    join, \
    exists, \
    isfile

import json

from configuration.managers.configuration \
    import Configuration

from configuration.managers.dictionary \
    import Dictionary

cache = None


def load_cache(
        configuration_path: str
) -> None:
    global cache

    result_path = join(
        configuration_path,
        '../../../configuration.json'
    )

    if exists(result_path) and \
       isfile(result_path) and \
            cache is None:
        f = open(result_path)
        data = json.load(f)
        f.close()

        cache = data


def loader_for_configuration_setup(
        configuration_path: str
) -> list:
    global cache

    result_variables = []

    load_cache(
        configuration_path
    )

    if has_data(cache):
        setup_configuration(
            cache,
            result_variables,
            configuration_path
        )

    return result_variables


def setup_configuration(
        values: dict,
        return_values: list,
        configuration_path: str
) -> list:
    if 'configuration' \
            in values:
        if 'include' \
                in values['configuration']:
            list_of_configuration_files_to_include = values['configuration']['include']

            print(
                'found configurations: ',
                list_of_configuration_files_to_include
            )

            for e in list_of_configuration_files_to_include:
                final = join(
                    configuration_path,
                    e
                )

                load_configurations(
                    final,
                    return_values
                )

    return return_values


def has_data(
        values: dict
) -> bool:
    if 'type' in values:
        if values['type'] == 'load':
            return True

    return False


def loader_for_dictionary_setup(
        configuration_path: str
) -> list:
    global cache

    result_variables = []

    load_cache(
        configuration_path
    )

    if has_data(cache):
        setup_dictionary(
            cache,
            result_variables,
            configuration_path
        )

    return result_variables


def setup_dictionary(
        data: dict,
        result_variables: list,
        configuration_path: str
):
    if 'configuration' in data:
        if 'dictionaries' in data['configuration']:
            dictionaries = data['configuration']['dictionaries']
            print('found dictionaries:', dictionaries)

            for e in dictionaries:
                final = join(
                    configuration_path,
                    e
                )

                load_dictionaries(
                    final,
                    result_variables
                )


def load_dictionaries(
        path_to_file: str,
        retValues: list
):
    dictionary = Dictionary(
        path_to_dictionary=path_to_file
    )

    retValues.append(
        dictionary
    )


def load_configurations(
        path_to_file: str,
        return_values: list
):
    configuration = Configuration(
            path_to_configuration=path_to_file
    )

    return_values.append(
        configuration
    )

