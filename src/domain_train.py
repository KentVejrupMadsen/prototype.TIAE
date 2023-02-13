import wandb

from wandb \
    import init \
    as wandb_init

from wandb \
    import finish \
    as wandb_finished

from src.misc.generate_case_name \
    import generate_case_name

from src.training.training_classification_script \
    import run \
    as classification_run


from src.state.configuration \
    import \
    get_global_configuration, \
    get_seed

from src.load_dataset \
    import load \
    as load_dataset


class DomainTraining:
    def __init__(self):
        generated_case_name = generate_case_name()

        wandb_init(
            'training_test',
            name=generated_case_name,

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

        wandb.log(
            {
                'configuration': get_global_configuration(),
                'seed': get_seed()
            }
        )

        load_dataset()

    def test(self):
        classification_run()

    def done(self):
        wandb_finished()


