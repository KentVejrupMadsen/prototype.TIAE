from state.global_state \
    import \
    get_path_to_training_dataset, \
    get_update_dateset_online

import os
import wandb


def load_from_wandb():
    print(
        'loading from wandb.'
    )


def save_to_wandb():
    print(
        'saving state of dataset to wandb'
    )
    dataset_train = wandb.Artifact(
        'training',
        type='dataset'
    )

    dataset_train.add_dir(
        get_path_to_training_dataset()
    )

    wandb.log_artifact(
        dataset_train
    )


def load():
    if os.path.isdir(
        get_path_to_training_dataset()
    ):
        if get_update_dateset_online():
            save_to_wandb()
    else:
        load_from_wandb()
