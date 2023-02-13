from configuration.globals \
    import setup

from configuration.manager \
    import ConfigurationManager

setup(__file__)


def main() -> None:
    config = ConfigurationManager()


if __name__ == '__main__':
    main()
