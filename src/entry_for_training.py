from domain.train \
    import Training

from application \
    import Application


def main() -> None:
    app = Application(
        Training()
    )

    app.execute()
    app.clean()


if __name__ == '__main__':
    main()
