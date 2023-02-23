nvidia_gpu_memory_limit = 3850

use_gpu = True
logical_gpus = 1


def get_use_gpu() -> bool:
    global use_gpu
    return use_gpu


def get_logical_gpus() -> int:
    global logical_gpus
    return logical_gpus


def get_nvidia_gpu_memory_limit() -> int:
    global nvidia_gpu_memory_limit
    return nvidia_gpu_memory_limit
