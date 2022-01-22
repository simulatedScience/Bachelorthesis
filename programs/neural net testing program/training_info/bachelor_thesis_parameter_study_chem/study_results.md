results for bachelor_thesis_parameter_study_chem
min list for metric: training_time
|              value | neurons_per_layer | input_shape | output_shape | activation_functions | last_activation_function | layer_types |      loss_function | training_data_percentage | number_of_epochs | validation_split | number_of_repetitions | optimizer | learning_rate | epsilon | beta_1 | beta_2 | batch_size |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1.9308330535888671 |      (20, 15, 10) |          36 |            1 |              sigmoid |                   linear |       dense | mean_squared_error |                        1 |               50 |              0.2 |                     5 |      adam |          0.01 |   1e-07 |    0.9 |  0.999 |      10000 |
| 1.9308330535888671 |             (32,) |          36 |            1 |              sigmoid |                   linear |       dense | mean_squared_error |                        1 |               50 |              0.2 |                     5 |      adam |          0.01 |   1e-07 |    0.9 |  0.999 |      10000 |
| 1.9308330535888671 |             (32,) |          36 |            1 |              sigmoid |                   linear |       dense |           log_cosh |                        1 |               50 |              0.2 |                     5 |      adam |          0.01 |   1e-07 |    0.9 |  0.999 |      10000 |
| 1.9308330535888671 |             (32,) |          36 |            1 |              sigmoid |                   linear |       dense | mean_squared_error |                        1 |              500 |              0.2 |                     5 |      adam |          0.01 |   1e-07 |    0.9 |  0.999 |      10000 |
| 1.9308330535888671 |             (32,) |          36 |            1 |              sigmoid |                   linear |       dense | mean_squared_error |                        1 |               50 |              0.2 |                     5 |      adam |         0.001 |   1e-07 |    0.9 |  0.999 |      10000 |

max list for metric: training_time
|             value | neurons_per_layer | input_shape | output_shape | activation_functions | last_activation_function | layer_types | loss_function | training_data_percentage | number_of_epochs | validation_split | number_of_repetitions | optimizer | learning_rate | epsilon | beta_1 | beta_2 | batch_size |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 643.6880697727204 |      (20, 15, 10) |          36 |            1 |              sigmoid |                   linear |       dense |      log_cosh |                        1 |              500 |              0.2 |                     5 |      adam |          0.01 |       1 |    0.9 |  0.999 |      10000 |
| 643.6880697727204 |      (20, 15, 10) |          36 |            1 |              sigmoid |                   linear |       dense |      log_cosh |                        1 |              500 |              0.2 |                     5 |      adam |         0.001 |       1 |    0.9 |  0.999 |        100 |
| 652.0155807495117 |      (20, 15, 10) |          36 |            1 |              sigmoid |                   linear |       dense |      log_cosh |                        1 |              500 |              0.2 |                     5 |      adam |          0.01 |   1e-07 |    0.9 |  0.999 |        100 |
| 652.0155807495117 |      (20, 15, 10) |          36 |            1 |              sigmoid |                   linear |       dense |      log_cosh |                        1 |              500 |              0.2 |                     5 |      adam |          0.01 |   1e-07 |    0.9 |  0.999 |      10000 |
| 652.0155807495117 |      (20, 15, 10) |          36 |            1 |              sigmoid |                   linear |       dense |      log_cosh |                        1 |              500 |              0.2 |                     5 |      adam |         0.001 |   1e-07 |    0.9 |  0.999 |        100 |

min list for metric: test_loss
|                value | neurons_per_layer | input_shape | output_shape | activation_functions | last_activation_function | layer_types | loss_function | training_data_percentage | number_of_epochs | validation_split | number_of_repetitions | optimizer | learning_rate | epsilon | beta_1 | beta_2 | batch_size |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0.006544356327503919 |      (20, 15, 10) |          36 |            1 |              sigmoid |                   linear |       dense |      log_cosh |                        1 |              500 |              0.2 |                     5 |      adam |         0.001 |   1e-07 |    0.9 |  0.999 |        100 |
| 0.006544356327503919 |          (50, 10) |          36 |            1 |              sigmoid |                   linear |       dense |      log_cosh |                        1 |              500 |              0.2 |                     5 |      adam |         0.001 |   1e-07 |    0.9 |  0.999 |      10000 |
| 0.006544356327503919 |          (50, 10) |          36 |            1 |              sigmoid |                   linear |       dense |      log_cosh |                        1 |              500 |              0.2 |                     5 |      adam |         0.001 |   1e-07 |    0.9 |  0.999 |        100 |
| 0.006842704769223928 |      (20, 15, 10) |          36 |            1 |              sigmoid |                   linear |       dense |      log_cosh |                        1 |              500 |              0.2 |                     5 |      adam |          0.01 |   1e-07 |    0.9 |  0.999 |       1000 |
| 0.006842704769223928 |          (50, 10) |          36 |            1 |              sigmoid |                   linear |       dense |      log_cosh |                        1 |              500 |              0.2 |                     5 |      adam |          0.01 |   1e-07 |    0.9 |  0.999 |      10000 |

max list for metric: test_loss
|              value | neurons_per_layer | input_shape | output_shape | activation_functions | last_activation_function | layer_types |      loss_function | training_data_percentage | number_of_epochs | validation_split | number_of_repetitions | optimizer | learning_rate | epsilon | beta_1 | beta_2 | batch_size |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1.9150392293930054 |             (32,) |          36 |            1 |                 relu |                   linear |       dense |           log_cosh |                        1 |               50 |              0.2 |                     5 |      adam |         0.001 |       1 |    0.9 |  0.999 |      10000 |
| 2.4474809527397157 |          (50, 10) |          36 |            1 |              sigmoid |                   linear |       dense |           log_cosh |                        1 |               50 |              0.2 |                     5 |      adam |         0.001 |       1 |    0.9 |  0.999 |      10000 |
| 2.4474809527397157 |          (50, 10) |          36 |            1 |              sigmoid |                   linear |       dense | mean_squared_error |                        1 |              500 |              0.2 |                     5 |      adam |         0.001 |       1 |    0.9 |  0.999 |      10000 |
| 2.4474809527397157 |          (50, 10) |          36 |            1 |              sigmoid |                   linear |       dense | mean_squared_error |                        1 |               50 |              0.2 |                     5 |      adam |         0.001 |       1 |    0.9 |  0.999 |      10000 |
| 2.4474809527397157 |          (50, 10) |          36 |            1 |              sigmoid |                   linear |       dense | mean_squared_error |                        1 |               50 |              0.2 |                     5 |      adam |         0.001 |   1e-07 |    0.9 |  0.999 |      10000 |


------------------------------------------------------------

best parameter values regarding \texttt{training_time}
parameter name & parameter values & win count & avg. differences & best value\\
\hline
neurons_per_layer & [(32,), (50, 10), (20, 15, 10)] & [215, 1, 0] & [5.45537030e-05 6.56174089e+00 1.96329612e+01] & (32,)\\
activation_functions & ['relu', 'sigmoid'] & [178, 146] & [0.69213005 1.4241056 ] & relu\\
last_activation_function & ['linear'] & [648] & [0.] & undetermined\\
loss_function & ['mean_squared_error', 'log_cosh'] & [306, 18] & [0.01122463 4.5908186 ] & mean_squared_error\\
number_of_epochs & [50, 150, 500] & [216, 0, 0] & [  0.          41.49192034 186.58211757] & 50\\
batch_size & [100, 1000, 10000] & [0, 0, 216] & [244.1522488   21.86807451   0.        ] & 10000\\
learning_rate & [0.1, 0.01, 0.001] & [78, 60, 78] & [0.74833719 0.91512518 0.70141308] & undetermined\\
epsilon & [1, 1e-07] & [182, 142] & [0.36245626 0.68786448] & 1\\

best parameter values regarding \texttt{test_loss}
parameter name & parameter values & win count & avg. differences & best value\\
\hline
neurons_per_layer & [(32,), (50, 10), (20, 15, 10)] & [63, 147, 6] & [0.00802518 0.03193105 0.04115721] & undetermined\\
activation_functions & ['relu', 'sigmoid'] & [220, 104] & [0.01529326 0.04245088] & relu\\
last_activation_function & ['linear'] & [648] & [0.] & undetermined\\
loss_function & ['mean_squared_error', 'log_cosh'] & [4, 320] & [0.06244804 0.00038945] & log_cosh\\
number_of_epochs & [50, 150, 500] & [6, 9, 201] & [0.10172983 0.03671006 0.00462116] & 500\\
batch_size & [100, 1000, 10000] & [157, 38, 21] & [0.00837542 0.0320425  0.15496564] & 100\\
learning_rate & [0.1, 0.01, 0.001] & [124, 66, 26] & [0.02233246 0.02838818 0.13720868] & 0.1\\
epsilon & [1, 1e-07] & [50, 274] & [0.1260881  0.01327256] & 1e-07\\

