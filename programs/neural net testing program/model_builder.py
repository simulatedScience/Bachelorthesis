"""
a module for building tensorflow neural network models
"""
import tensorflow.keras as keras
from my_adam import my_Adam
from c_adam import cAdam
from c_adam_hat import cAdamHat
from fast_c_adam import fastcAdam


def make_model(model_params, optimizer_params):
    """
    build and compile a neural network using tensorflow and the given parameters
    """
    n_hidden_layers = len(model_params["neurons_per_layer"])
    activations, last_activation = set_activations(
        model_params["activation_functions"],
        n_hidden_layers,
        model_params["last_activation_function"])

    optimizer = set_optimizer(**optimizer_params)

    # build model layer by layer
    model = keras.Sequential()
    model.add(keras.layers.InputLayer(model_params["input_shape"]))
    if isinstance(model_params["input_shape"], (list, tuple)):
        model.add(keras.layers.Flatten())
    for n_neurons, activation in zip(model_params["neurons_per_layer"], activations):
        model.add(keras.layers.Dense(n_neurons, activation=activation))
    model.add(keras.layers.Dense(model_params["output_shape"],
                                 activation=last_activation))

    model.compile(optimizer=optimizer,
                  loss=model_params["loss_function"],
                  metrics=get_metrics(model_params["output_shape"]))
    return model


def set_activations(activations,
                    n_hidden_layers,
                    last_activation=None):
    """
    returns:
        (list) or (tuple) of (str) - list of `n_hidden_layers` activation functions
    """
    if isinstance(activations, str):
        if last_activation is None:
            return [activations]*n_hidden_layers, activations
        return [activations]*n_hidden_layers, last_activation

    if isinstance(activations, (list, tuple)):
        return activations, activations[-1]


def set_optimizer(optimizer, **params):
    """
    convert an optimizer name `optimizer` and it's parameters into a keras optimizer object.

    If `optimizer` is not a string, the return value is the input `optimizer`.
    This behavior allows other optimizers to be used easily

    inputs:
    -------
        optimizer - (str) - optimizer name, should be 'adam', 'my_adam' or 'sgd'
        params - (dict) - additional keyword arguments get passed to the optimizer call
    """
    if not isinstance(optimizer, str):
        return optimizer
    if optimizer.lower() == "adam":
        return keras.optimizers.Adam(**params)
    if optimizer.lower() == "my_adam":
        return my_Adam(**params)
    if optimizer.lower() == "c_adam":
        return cAdam(**params)
    if optimizer.lower() == "fast_c_adam":
        return fastcAdam(**params)
    if optimizer.lower() == "c_adam_hat":
        return cAdamHat(**params)
    elif optimizer.lower() == "sgd":
        return keras.optimizers.SGD(**params)


def get_metrics(output_shape):
    """
    determine which metrics to track
    if the output is a single number, no additional metrics are used,
    otherwise accuracy is tracked.
    """
    if isinstance(output_shape, int) and output_shape == 1:
        return []
    return ["accuracy"]
