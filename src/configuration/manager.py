from configuration.configuration \
    import Configuration

from configuration.utils \
    import \
    loader_for_configuration_setup, \
    loader_for_dictionary_setup

from configuration.globals \
    import get_repository_path


class ConfigurationManager:
    def __init__(
            self,
            configuration_path: str = get_repository_path()
    ):
        self.configuration_path = configuration_path
        self.configurations = [

        ]

        self.__debug()
        self.__load__()

    def __load__(self):
        loader_for_configuration_setup(
            self.get_path()
        )

        loader_for_dictionary_setup(
            self.get_path()
        )

    def create(
            self,
            path
    ) -> Configuration:
        newValue = Configuration(
            path
        )
        self.configurations.append(
            newValue
        )

        return newValue

    def get(
            self,
            idx
    ):
        return self.configurations[idx]

    def set(
            self,
            idx: int,
            value
    ):
        self.configurations[idx] = value

    def delete(
            self,
            idx
    ):
        self.configurations.pop(
            idx
        )

    def move(
            self,
            first_index,
            second_index
    ):
        first_model = self.configurations[
            first_index
        ]
        second_model = self.configurations[
            second_index
        ]

        self.set(
            first_index,
            second_model
        )

        self.set(
            second_index,
            first_model
        )

    def get_path(self) -> str:
        return self.configuration_path

    def set_path(
            self,
            value: str
    ) -> None:
        self.configuration_path = value

    def get_configurations(self) -> list:
        return self.configurations

    def set_configurations(
            self,
            value: list
    ) -> None:
        self.configurations = value

    def __debug(self):
        print('configuration.')

        if not (
                self.configuration_path is None
        ):
            print(
                'path:',
                self.configuration_path
            )

    def __sizeof__(self):
        return len(
            self.configurations
        )

    def __str__(self):
        return "configuration manager"


# Singleton object. used globally
singleton = None


def get_singleton() -> ConfigurationManager:
    global singleton

    if singleton is None:
        set_singleton(
            ConfigurationManager()
        )

    return singleton


def set_singleton(
        value: ConfigurationManager
) -> None:
    global singleton
    singleton = value

