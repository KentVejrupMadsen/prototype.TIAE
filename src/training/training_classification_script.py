from keras.utils \
    import image_dataset_from_directory

from tensorflow.python.data \
    import AUTOTUNE

from src.callbacks.CallbackFactory \
    import CallbackFactory

from src.configuration \
    import \
    get_seed, \
    get_training_dataset, \
    get_validation_dataset, \
    set_training_dataset, \
    set_validation_dataset, \
    set_categories, \
    path_to_training_dataset, \
    get_validation_split, \
    get_image_size, \
    get_batch_size, \
    get_spectrum, \
    get_option_crop_aspect_ratio, \
    get_option_shuffle, \
    get_global_configuration, \
    get_categories

from src.training.classifying_model \
    import Classify

import wandb

model = None


def run():
    generate_datasets()
    generate_network()
    generate_train()


def generate_datasets():
    train_dataset = image_dataset_from_directory(
        path_to_training_dataset(),
        validation_split=get_validation_split(),
        subset='training',
        seed=get_seed(),
        image_size=get_image_size(),
        batch_size=get_batch_size(),
        color_mode=get_spectrum(),
        crop_to_aspect_ratio=get_option_crop_aspect_ratio(),
        shuffle=get_option_shuffle()
    )

    train_dataset.cache().prefetch(
        buffer_size=AUTOTUNE
    )

    set_training_dataset(
        train_dataset
    )

    set_categories(
        train_dataset.class_names
    )

    validation_dataset = image_dataset_from_directory(
        path_to_training_dataset(),
        validation_split=get_validation_split(),
        subset='validation',
        seed=get_seed(),
        image_size=get_image_size(),
        batch_size=get_batch_size(),
        color_mode=get_spectrum(),
        crop_to_aspect_ratio=get_option_crop_aspect_ratio(),
        shuffle=get_option_shuffle()
    )

    validation_dataset.cache().prefetch(
        buffer_size=AUTOTUNE
    )

    set_validation_dataset(
        validation_dataset
    )


def generate_network():
    global model
    model = Classify(
        training=get_training_dataset(),
        validation=get_validation_dataset()
    )


def generate_indexes(
        size_of_index: int
) -> list:
    r_values = []
    for i in range(0, size_of_index):
        r_values.append((i + 1))

    return r_values


def generate_train():
    factory = CallbackFactory(
        get_classify_model()
    )

    factory.append_early_stopper()
    factory.append_checkpoint()

    get_classify_model().fit_model()

    get_classify_model().save(
        get_global_configuration()['tf']['path']
    )

    history = get_classify_model().history

    val_loss = history.history['val_loss']
    val_acc = history.history['val_accuracy']

    accuracy = history.history['accuracy']
    loss = history.history['loss']

    wandb.log(
        {
            'classes':
                {
                    'labels': get_categories()
                },
            'history':
            {
                'values':
                    {
                        'accuracy':
                            {
                                'values': val_acc,
                            },
                        'loss':
                            {
                                'values': val_loss,
                            }
                    },

                'accuracy':
                    {
                        'values': accuracy,
                    },

                'loss':
                    {
                        'values': loss,
                    }
            },
        }
    )


def get_classify_model() -> Classify:
    global model
    return model