import os
from os \
    import \
    listdir, \
    symlink

from os.path \
    import \
    join, \
    isdir

train_path = r'/mnt/c/Workspace/TIAE/datasets/training-set'
batches_path = r'/mnt/c/Workspace/TIAE/datasets/batches'


def is_train_empty() -> bool:
    global batches_path

    list = listdir(batches_path)

    if len(list) == 0:
        return True
    else:
        return False


def make_symbolic_links():
    global \
        train_path, \
        batches_path

    found = listdir(batches_path)

    for dir in found:
        full_path_to_train = join(
            train_path,
            dir
        )

        full_path_to_batch = join(
            batches_path,
            dir
        )

        if isdir(full_path_to_batch):
            symlink(
                full_path_to_batch,
                full_path_to_train
            )


def clear_links():
    global train_path

    listed = listdir(train_path)

    for e in listed:
        fullpath = join(train_path, e)
        os.remove(fullpath)
