from configuration.managers.utils \
    import loader_for_dictionary_setup

from configuration.globals \
    import get_repository_path


def is_zero(
        value: int
) -> bool:
    return value == 0


def is_str_empty(
        value: str
) -> bool:
    return is_zero(
        len(value)
    )


class DictionaryManager:
    def __init__(
            self,
            configuration_path: str = ''
    ):
        self.configuration_path = configuration_path
        self.dictionaries = []

        if is_str_empty(
                configuration_path
        ):
            self.configuration_path = get_repository_path()

    def __load__(self):
        self.dictionaries = loader_for_dictionary_setup(
            self.get_path()
        )

    def get_path(self) -> str:
        return self.configuration_path