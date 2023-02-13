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

from src.logging.load_dataset \
    import load \
    as load_dataset

from src.logging.log \
    import log_values


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

    def execute(self):
        load_dataset()
        self.test()
        self.log_test_result()

    def test(self):
        classification_run()

    def log_test_result(self):
        log_values(
            'seed', get_seed()
        )
        log_values(
            'configuration',
            get_global_configuration()
        )

    def done(self):
        wandb_finished()
