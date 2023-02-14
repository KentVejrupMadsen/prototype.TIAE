from configuration.globals \
    import \
    setup

from configuration.managers \
    import get_singleton_configuration_manager

from configuration.managers \
    import get_singleton_dictionary_manager

from application \
    import Application


def load() -> None:
    cfg_manager = get_singleton_configuration_manager()
    dict_mng = get_singleton_dictionary_manager()


def main() -> None:
    setup(__file__)
    load()

    app = Application()


if __name__ == '__main__':
    main()
