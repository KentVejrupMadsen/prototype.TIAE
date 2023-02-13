from os.path \
    import \
    realpath, \
    dirname


class ConfigurationManager:
    def __init__(self):
        self.configuration_path = None
        self.get_script_location()

        self.__debug()

    def get_script_location(self):
        self.configuration_path = dirname(
            realpath(
                __file__
            )
        )

    def get_path(self) -> str:
        return self.configuration_path

    def set_path(
            self,
            value: str
    ) -> None:
        self.configuration_path = value

    def __debug(self):
        print('configuration.')

        if not (
                self.configuration_path is None
        ):
            print('path:', self.configuration_path)


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

