"""
this module implements methods for conducting parameter studies on neural networks.
The goal is to find out which parameters have the biggest impact on model performance and which values work well.
"""

import time
import itertools
from model_trainer import train_model
from model_tester import test_model
# from parameter_analysis import analyse_parameter_study # TODO implement analysis
import file_management as fm

def dense_parameter_study(
        neural_net_params,
        training_params,
        optimizer_params,
        dataset,
        verbose=2
        ):
    """
    Conduct a dense parameter study by training neural networks with all possible combinations of the given parameters.
    Then save and analyse the results.
    
    Every value in the input dictionaries may instead be a list containing the corresponding datatype. In that case a model is trained for each parameter given in that list

    inputs:
    -------
        neural_net_params - (dict) - parameters for neural network architecture
            dict should contain values for the following keys:
            - neurons_per_layer - (tuple) of (int)
            - input_shape - (int) or (tuple) of (int)
            - output_shape - (int) or (tuple) of (int)
            - activation_functions - (str) or (tuple) of (str)
            - last_activation_function - (str)
            - loss_function - (str)
            - layer_types - (str) # unused for now. only dense layers are used
        training_params - (dict) - parameters for training the models
            dict should contain values for the following keys:
            - training_data_percentage - (float)
            - number_of_epochs - (int)
            - batch_size - (int)
            - validation_split - (float)
            - number_of_repetitions - (int)
        optimizer_params - (dict) - parameters for optimizer
            - optimizer - (str) or optimizer instance
            # optional parameters for Adam optimizer:
            - learning_rate - (float)
            - epsilon - (float)
            - beta_1 - (float)
            - beta_2 - (float)
        dataset - (callable) - should be of shape (x_train, y_train), (x_test, y_test).
    """
    n_combinations = print_number_of_combinations(neural_net_params, training_params, optimizer_params)
    # split dataset
    train_data, test_data = dataset
    # prepare for experiments
    study_folder = fm.create_study_folder(neural_net_params, training_params, optimizer_params)
    repetitions = training_params["number_of_repetitions"]
    batch_folder_paths = list() # contains names of folders created during the experiments
    start_time = time.time()
    for i in range(repetitions):
        batch_folder_index = 0
        # reset the product generator
        product_generator, key_list = \
                param_cross_product(neural_net_params, training_params, optimizer_params)
        for param_list in product_generator:
            # create a dictionary containing all training parameters for a single model
            sub_training_params = {key:val for key,val in zip(key_list, param_list)}
            sub_optimizer_params = {key:sub_training_params[key] for key in optimizer_params}
            # create folder for saving the models and training information
            if i == 0:
                folder_path = fm.create_batch_folder(sub_training_params, sub_optimizer_params, study_folder=study_folder)
                batch_folder_paths.append(folder_path)
            sub_folders = (study_folder, batch_folder_paths[batch_folder_index])
            # train a model with the given parameters
            model_start_time = time.time()
            trained_model, history = train_model(
                    sub_training_params,
                    sub_optimizer_params,
                    train_data,
                    sub_folders=sub_folders,
                    verbose=verbose)
            # test model and save score
            test_scores = test_model(trained_model, test_data)
            # save training and test infomation
            history.add_test_scores(test_scores)
            fm.save_train_history(history, save_time=history.save_time, sub_folders=sub_folders)
            # ensure the next model is saved in the correct folder
            batch_folder_index += 1
            model_time = time.time() - model_start_time
            print(f"repetition {i+1}/{repetitions}, \ttrained model {batch_folder_index}/{n_combinations}, \ttrain time: {model_time}s")
        if verbose:
            print(f"finished training {n_combinations} models {i+1}/{repetitions} times.")
            print(f"time since start of parameter study: {time.time() - start_time}s")
    print("finished parameter study.")
    # analyse_parameter_study(study_folder)


def param_cross_product(
        neural_net_params,
        training_params,
        optimizer_params):
    """
    return a generator that outputs every combination of the given parameters

    inputs:
    -------
        see `dense_parameter_study`
    """
    input_lists = list(neural_net_params.values()) \
                + list(training_params.values()) \
                + list(optimizer_params.values())
    input_lists = [x if isinstance(x, list) else [x] for x in input_lists]
    key_list = list(neural_net_params.keys()) \
             + list(training_params.keys()) \
             + list(optimizer_params.keys())
    product_generator = itertools.product(*input_lists)
    return product_generator, key_list


def print_number_of_combinations(
        neural_net_params,
        training_params,
        optimizer_params,
        print_result=True):
    """
    return the number of different parameter combinations for the given inputs, not including number of training repetitions for the same set of parameters.

    inputs:
    -------
        see `dense_parameter_study`
        print_result - (bool) - whether or not to print the results to the console.
    """
    n_combinations = 1
    for value in neural_net_params.values():
        if isinstance(value, list):
            n_combinations *= len(value)
    for key, value in training_params.items():
        if key == "number_of_repetitions":
            continue
        if isinstance(value, list):
            n_combinations *= len(value)
    for value in optimizer_params.values():
        if isinstance(value, list):
            n_combinations *= len(value)
    if print_result:
        n_trains = training_params['number_of_repetitions']
        print("="*60)
        print(f"Models will be trained with {n_combinations} different parameter settings.")
        print(f"To estimate uncertainties, each model will be trained {n_trains} times.")
        print(f"Therefor {n_combinations*n_trains} models will be trained and tested.")
        print("="*60)
    return n_combinations
