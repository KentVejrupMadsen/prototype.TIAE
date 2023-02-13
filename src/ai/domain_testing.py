from wandb \
    import init \
    as wandb_init

from wandb \
    import finish \
    as wandb_finished


class DomainTesting:
    def __init__(self):
        wandb_init(
            'tiae',
            save_code=True,

            group='testing',
            tensorboard=True,

            tags=
            [
                'alpha',
                'notebook',
                'prediction',
                'testing',
                'nvidia-gpu'
            ],

            notes='domain used for testing the algorithms capacity for prediction certain categories.'
        )

    def done(self):
        wandb_finished()



