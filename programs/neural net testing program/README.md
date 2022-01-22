This directory includes several modules working together to simplify training some neural networks and then save and compare information about the training process.

# version 2.0

## What the program does
See the file `Bachelorthesis.pdf` for an outline.

## how to use the program
1. choose some possible values for each tunable parameter
   (see `dense_parameter_study_[...].py` files)
2. train model several times for every combination of the parameters chosen in 1. (this process is started in `dense_parameter_study_[...].py` files using the method `dense_parameter_study` in `dense_parameter_study.py`)
3. examine the results of the tests in two steps:
   1. summarize all results of the trained models and calculate averages of models that were trained multiple times. (using the methods `statistical_analysis_of_study` and `analyse_parameter_study` in `data_analysis.py`)
   2. Convert the results to latex tables. (using `show_all_results` in `result_ouput.py`)

## Notes
Most parts of the program are kept quite general, however some parts of the result output are specialized to the experiments performed for the thesis.

For example `vertical_best_worst_output.py` includes a method `get_param_setting_renaming` defining a dictionary that specifies some table entries to get replaced with other strings (mostly to add formatting or fix spelling).

The method `print_param_influcence_tables` in `result_output.py` assumes that the number of values for each parameter is always a factor of 6. This 6 should actually be the lowest common multiple of all numbers of values for the parameters.

It's likely that there are a few similar issues that require a bit of work before using this program for other studies. It is also possible to combine the steps 2. and 3.1 of the workflow described above (automatically start step 3.1 after 2.).

## Missing files

Reproducing the experiments requires the ChemEx dataset and code to read that data into python. Since I did not write that code myself or assemble the dataset, I am not including those here. Both the data and code to read it were provided to me by Franz Bethke.

The MNIST dataset used for the remaining experiments is included with Tensorflow and freely available online.