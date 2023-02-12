from src.domain_train \
    import DomainTraining

from src.secure.setup_secure_random \
    import setup

import tensorflow

try:
    found_gpu = False
    for gpu in tensorflow.config.experimental.list_physical_devices(
            'GPU'
    ):
        tensorflow.config.experimental.set_memory_growth(
            device=gpu,
            enable=1
        )

        tensorflow.config.experimental.set_virtual_device_configuration(
            gpu,
            [tensorflow.config.experimental.VirtualDeviceConfiguration(
                memory_limit=4080
            )]
        )

        if not found_gpu:
            found_gpu = True

    if found_gpu:
        print('GPU Found')

except RuntimeError as re:
    print(re)


setup()


def main() -> None:
    domain = DomainTraining()
    domain.test()
    domain.done()


if __name__ == '__main__':
    main()
