from src.ai.domain_testing \
    import DomainTesting

from src.entropy.secure.setup_secure_random \
    import setup \
    as secure_randomizers

secure_randomizers()


def main():
    predictor = DomainTesting()


    predictor.done()


if __name__ == '__main__':
    main()
