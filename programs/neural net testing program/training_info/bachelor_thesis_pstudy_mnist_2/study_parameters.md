## all parameters used in this study: 


### Neural Network parameters:
   - neurons_per_layer:         [(32,), (50, 10), (20, 15, 10)]
   - input_shape:               (28, 28)
   - output_shape:              10
   - activation_functions:      ['relu', 'sigmoid']
   - last_activation_function:  ['softmax', 'sigmoid']
   - layer_types:               dense
   - loss_function:             ['categorical_crossentropy', 'mean_squared_error']

### Training parameters:
   - training_data_percentage:  1
   - number_of_epochs:          [5, 25, 50]
   - batch_size:                [100, 1000, 10000]
   - validation_split:          0.2
   - number_of_repetitions:     5

### Optimizer parameters:
   - optimizer:                 ['adam', 'c_adam']
   - learning_rate:             [0.1, 0.01, 0.001]
   - epsilon:                   [1.0, 1e-07]
   - beta_1:                    0.9
   - beta_2:                    0.999
