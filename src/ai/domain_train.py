from src.misc.generate_case_name \
    import generate_case_name

from src.ai.training \
    import run \
    as classification_run

from src.extensions.wandb.artifacts \
    import load \
    as load_dataset


class DomainTraining:
    def __init__(self):
        generated_case_name = generate_case_name()



    def execute(self):
        load_dataset()
        self.test()

    def test(self):
        classification_run()


    def done(self):
        pass
