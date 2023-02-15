from extensions.wandb.artifacts \
    import load \
    as load_dataset

from execute_domain \
    import Execution


class Training(
    Execution
):
    def __init__(self):
        super().__init__()

    def execute(self):
        load_dataset()
        self.test()

    def test(self):
        pass

    def done(self):
        pass
