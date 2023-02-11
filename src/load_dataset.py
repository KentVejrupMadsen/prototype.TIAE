from src.configuration \
    import get_global_configuration

import os
import wandb


def get_train_path() -> str:
    return get_global_configuration()['dataset']['train']['path']


def get_update_state() -> bool:
    r = get_global_configuration()['dataset']['updatable']
    return r


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
        get_train_path()
    )

    wandb.log_artifact(
        dataset_train
    )


def load():
    if os.path.isdir(
        get_train_path()
    ):
        if get_update_state():
            save_to_wandb()
    else:
        load_from_wandb()

