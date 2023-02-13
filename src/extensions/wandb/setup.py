import wandb


def wdb_setup():
    wandb.init(
        'training_test',
        name='',

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


def wdb_finish():
    wandb.finish()

