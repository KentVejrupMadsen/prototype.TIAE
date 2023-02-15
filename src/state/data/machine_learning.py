from domain.training.model.classifying_model \
    import ClassifyModel

model = None


def get_classify_model() -> ClassifyModel:
    global model
    return model


def set_classify_model(
        cm: ClassifyModel
) -> None:
    global model
    model = cm
