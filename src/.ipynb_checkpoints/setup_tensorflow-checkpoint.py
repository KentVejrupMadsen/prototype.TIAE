﻿from tensorflow.python.eager.context \
    import \
    set_log_device_placement, \
    LogicalDeviceConfiguration

from tensorflow.python.framework.config \
    import \
    get_visible_devices, \
    set_visible_devices, \
    set_logical_device_configuration, \
    list_logical_devices, \
    get_logical_device_configuration

from configuration \
    import \
    get_use_gpu, \
    get_nvidia_gpu_memory_limit, \
    get_logical_gpus

set_log_device_placement(False)

done: bool = False


def setupTensorFlow():
    print("running setup")

    try:
        for e in get_visible_devices():
            if e.device_type == 'GPU':
                setup_gpu(e)
            else:
                setup_cpu(e)

    except RuntimeError:
        print("error")


def setup_gpu(physicalDevice):
    global done

    if get_use_gpu():
        if not done:
            print(
                'found: ',
                str(physicalDevice.name)
            )
            logical_gpus = []

            for e in range(
                    0,
                    get_logical_gpus()
            ):
                generated = LogicalDeviceConfiguration(
                    memory_limit=get_nvidia_gpu_memory_limit()
                )

                print(
                    'current: ',
                    str(e + 1)
                )
                print(
                    'configuration: ',
                    str(generated)
                )

                logical_gpus.append(
                    generated
                )

            set_logical_device_configuration(
                physicalDevice,
                logical_gpus
            )

            print('setup of logical gpus')
        else:
            print('skipped: ', physicalDevice)


def setup_cpu(physicalDevice):
    global done

    if not get_use_gpu():
        if not done:
            print('found: ', physicalDevice)
        else:
            print('skipped: ', physicalDevice)