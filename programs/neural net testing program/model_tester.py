"""
this module implements functions for evaluating performance of trained neural networks
"""
from helper_functions import auto_use_multiprocessing

def test_model(model, test_data, batch_size=1000):
    """
    evaluate the performance of a given model based on given data.
    """
    use_multiprocessing = auto_use_multiprocessing()
    x_test, y_test = test_data
    test_scores = model.evaluate(x_test, y_test,
            batch_size=batch_size,
            use_multiprocessing=use_multiprocessing,
            verbose=0)
    return test_scores