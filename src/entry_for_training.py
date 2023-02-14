from configuration.globals \
    import setup, get_repository_path, get_source_path

from configuration.managers import get_singleton_configuration_manager


def main() -> None:
    setup(__file__)
    cfg_manager = get_singleton_configuration_manager()


if __name__ == '__main__':
    main()
