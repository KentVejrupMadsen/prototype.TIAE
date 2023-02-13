from src.ai.domain_train \
    import DomainTraining

from src.entropy.secure.setup_secure_random \
    import setup

setup()


def main() -> None:
    domain = DomainTraining()
    domain.execute()
    domain.done()


if __name__ == '__main__':
    main()
