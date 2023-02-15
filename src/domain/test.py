from wandb \
    import init \
    as wandb_init

from wandb \
    import finish \
    as wandb_finished

from execute_domain \
    import Execution


class Testing(
    Execution
):
    def __init__(self):
        super().__init__()
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

    def execute(self):
        pass

    def done(self):
        wandb_finished()
