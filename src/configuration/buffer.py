nvidia_gpu_memory_limit = 1024
use_gpu = True
logical_gpus = 2


def getUseGpu() -> bool:
    global use_gpu
    return use_gpu


def getLogicalGpus() -> int:
    global logical_gpus
    return logical_gpus


def getNvidiaGpuMemoryLimit() -> int:
    global nvidia_gpu_memory_limit
    return nvidia_gpu_memory_limit
