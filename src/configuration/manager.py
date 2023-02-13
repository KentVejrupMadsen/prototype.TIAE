class ConfigurationManager:
    def __init__(self):
        self.configuration_path = None
        self.configurations = []

        self.__debug()

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

