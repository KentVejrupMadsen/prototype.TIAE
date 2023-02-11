from src.domain_train \
    import DomainTraining

from src.secure.setup_secure_random \
    import setup

setup()


def main() -> None:
    domain = DomainTraining()
    domain.test()
    domain.done()


if __name__ == '__main__':
    main()
