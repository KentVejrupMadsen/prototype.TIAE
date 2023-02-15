
update_dataset_online = False


def get_update_dateset_online() -> bool:
    global update_dataset_online
    return update_dataset_online


def set_update_dataset_online(value: bool) -> None:
    global update_dataset_online
    update_dataset_online = value
