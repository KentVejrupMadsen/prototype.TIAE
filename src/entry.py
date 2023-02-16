import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='3'

from setup_tensorflow \
    import setupTensorFlow

from __init__ \
    import TrainSegmentation

setupTensorFlow()


def main():
    TrainSegmentation()


if __name__ == '__main__':
    main()
