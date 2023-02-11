from wandb \
    import init \
    as wandb_init

from wandb \
    import finish \
    as wandb_finished


class DomainTraining:
    def __init__(self):
        wandb_init(
            'tiae',
            save_code=True,
            group='training',
            tensorboard=True,
            tags=
            [
                'alpha',
                'notebook',
                'training',
                'testing',
                'nvidia-gpu'
            ],
            notes='domain used for training the algorithm'
        )

    def done(self):
        wandb_finished()
