import numpy as np

def logcosh(x):
    """
    source: tensorflow documentation
        https://www.tensorflow.org/api_docs/python/tf/keras/losses/LogCosh
    """
    return np.log((np.exp(x) + np.exp(-x))/2)

def mse(x):
    """
    source: tensorflow documentation
        https://www.tensorflow.org/api_docs/python/tf/keras/losses/MeanSquaredError
    """
    return x**2

def catcross(x):
    """
    source: tensorflow documentation
        https://www.tensorflow.org/api_docs/python/tf/keras/losses/CategoricalCrossentropy
    """
    return 

def mae(x):
    """
    source: tensorflow documentation
        https://www.tensorflow.org/api_docs/python/tf/keras/losses/MeanAbsoluteError
    """
    return np.abs(x)

loss_functions = [logcosh, mse, mae, catcross]