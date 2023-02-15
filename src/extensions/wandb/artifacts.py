import wandb

from os.path \
    import isdir


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


def upload_dataset_to_wandb():
    if isdir(
        get_path_to_training_dataset()
    ):
        if get_update_dateset_online():
            save_to_wandb()
    else:
        load_from_wandb()
