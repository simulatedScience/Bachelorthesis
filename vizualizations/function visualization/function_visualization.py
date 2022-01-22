"""
this module implements functions for visualizing mathematical functions used for machine learning.
"""
import numpy as np
import matplotlib.pyplot as plt

from activation_functions import *
from loss_functions import *

def plot_func(func, domain=[-5,5], color="#5588ff", xlabel="$x$"):
    """
    plot function `func` on the given domain
    """
    x = np.linspace(*domain, num=200, endpoint=True)
    y = func(x)
    plt.plot(x,y, color=color)
    plt.title(func.__name__)
    plt.ylabel("$f(x)$")
    plt.xlabel(xlabel)
    plt.show()

if __name__ == "__main__":
    for func in activation_functions:
        plot_func(func)
    for func in loss_functions:
        plot_func(func, xlabel=r"$y-\hat y$")