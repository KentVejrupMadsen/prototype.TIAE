from configuration.globals \
    import setup, get_repository_path, get_source_path

from configuration.manager \
    import ConfigurationManager


def main() -> None:
    setup(__file__)
    config = ConfigurationManager()


if __name__ == '__main__':
    main()
