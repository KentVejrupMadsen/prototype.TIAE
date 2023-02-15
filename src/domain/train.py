from extensions.wandb.artifacts \
    import upload_dataset_to_wandb \
    as upload_dataset_to_wandb

from domain.training.network.training_classification_script \
    import run

from execute_domain \
    import Execution


class Training(
    Execution
):
    def __init__(
            self
    ):
        super().__init__()

    def execute(self):
        upload_dataset_to_wandb()
        self.test()

    def test(self):
        run()

    def done(self):
        pass
