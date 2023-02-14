from configuration.management.configuration_manager \
    import ConfigurationManager

from configuration.management.dictionary_manager \
    import DictionaryManager


# Singleton object. used globally
singleton_configuration_manager = None
singleton_dictionary_manager = None


def get_singleton_dictionary_manager() -> DictionaryManager:
    global singleton_dictionary_manager

    if is_singleton_dictionary_manager():
        set_singleton_dictionary_manager(
            DictionaryManager()
        )

    return singleton_dictionary_manager


def is_singleton_dictionary_manager() -> bool:
    global singleton_dictionary_manager

    if singleton_dictionary_manager is None:
        return True

    return False


def set_singleton_dictionary_manager(
        value: DictionaryManager
) -> None:
    global singleton_dictionary_manager
    singleton_dictionary_manager = value


def get_singleton_configuration_manager() -> ConfigurationManager:
    global singleton_configuration_manager

    if is_singleton_configuration_manager_null():
        set_singleton_configuration_manager(
            ConfigurationManager()
        )

    return singleton_configuration_manager


def set_singleton_configuration_manager(
        value: ConfigurationManager
) -> None:
    global singleton_configuration_manager
    singleton_configuration_manager = value


def is_singleton_configuration_manager_null() -> bool:
    global singleton_configuration_manager

    if singleton_configuration_manager is None:
        return True

    return False


