dataset_path: str = r'/mnt/c/Workspace/TIAE/datasets/training-set'
model_path: str = r'/tmp/segmentation_model.tf'


def get_data_path() -> str:
    global dataset_path
    return dataset_path


def get_model_path() -> str:
    global model_path
    return model_path
