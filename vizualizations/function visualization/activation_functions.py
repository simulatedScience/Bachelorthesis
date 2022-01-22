import numpy as np

def relu(x):
    """
    source: tensorflow documentation
        https://www.tensorflow.org/api_docs/python/tf/keras/activations/relu
    """
    if isinstance(x, float):
        if x <= 0:
            return 0
        else:
            return x
    return np.array([relu(x_i) for x_i in x])

def sigmoid(x):
    """
    source: tensorflow documentation
        https://www.tensorflow.org/api_docs/python/tf/keras/activations/sigmoid
    """
    return 1 / (1 + np.exp(-x))

def linear(x):
    """
    source: tensorflow documentation
        https://www.tensorflow.org/api_docs/python/tf/keras/activations/linear
    """
    return x

def softmax(x):
    """
    source: tensorflow documentation
        https://www.tensorflow.org/api_docs/python/tf/keras/activations/softmax
    """
    return np.exp(x) / np.sum(np.exp(x))

activation_functions = [relu, sigmoid, linear, softmax]