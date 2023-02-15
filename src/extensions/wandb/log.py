import wandb


def log_values(
        key: str,
        values
) -> None:
    wandb.log(
        {
            key: values
        }
    )
