import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='3'

import wandb

import setup_training

from setup_tensorflow \
    import setupTensorFlow

from __init__ \
    import TrainSegmentation

from segmentation.temperary import get_history, get_model

setupTensorFlow()


def main():
    wandb.init(
        project='tiae',
        entity='designermadsen',
        save_code=True
    )

    setup_training.clear_links()
    setup_training.make_symbolic_links()

    if not setup_training.is_train_empty():
        TrainSegmentation()

        parameters = get_history().params
        history = get_history().history

        wandb.config = parameters

        wandb.log({
            "model":
                {
                    "configuration": get_model().get_config()
                }
        })
    else:
        print(
            'training directory is empty.'
        )

    wandb.finish()


if __name__ == '__main__':
    main()
