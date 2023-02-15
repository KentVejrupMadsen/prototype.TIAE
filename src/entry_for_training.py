from configuration.globals \
    import \
    setup

from configuration.managers \
    import get_singleton_configuration_manager

from configuration.managers \
    import get_singleton_dictionary_manager

from application \
    import Application

from domain.train \
    import Training


def load() -> None:
    cfg_manager = get_singleton_configuration_manager()
    dict_mng = get_singleton_dictionary_manager()


def main() -> None:
    setup(__file__)
    load()

    app = Application(
        Training()
    )

    app.execute()
    app.clean()


if __name__ == '__main__':
    main()
