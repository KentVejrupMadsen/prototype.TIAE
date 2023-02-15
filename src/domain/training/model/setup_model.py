from domain.training.model.network.generate_in_out_network \
    import \
    generate_input, \
    generate_output

from domain.training.model.network.generate_middle_network \
    import generate_middle_layer


def setup_of_model(
        model
) -> None:
    generate_input(model)
    generate_middle_layer(model)
    generate_output(model)
