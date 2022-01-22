def get_num_params(layout):
    """
    calculate the number of learnable parameters for a given network layout, assuming it is densly connected

    inputs:
    -------
        layout (tuple) of (int) - number of neurons in each layer

    returns:
    --------
        (int) - number of learnable parameters
    """
    n_params = 0
    for i, n_neurons in enumerate(layout[:-1]):
        next_n_neurons = layout[i+1]
        n_params += (n_neurons+1)*next_n_neurons  # densely connected + biases
    return n_params


mnist_layouts = [(784, 32, 10),
                 (784, 50, 10, 10),
                 (784, 20, 15, 10, 10)]
chemex_layouts = [(36, 32,  1),
                  (36, 50, 10,  1),
                  (36, 20, 15, 10,  1)]
# chemex_layouts_master = [(36, 512, 256, 128, 64, 1)]
# test = [(784, 30, 10, 10)]

print("mnist layouts param counts:")
print("-"*27)
for layout in mnist_layouts:
    print(f"{str(layout):25} -> {get_num_params(layout):10}")
print()
print("chemex layouts param counts:")
print("-"*28)
for layout in chemex_layouts:
    print(f"{str(layout):25} -> {get_num_params(layout):10}")

# print()
# print("chemex_master layouts param counts:")
# print("-"*27)
# for layout in chemex_layouts_master:
#     print(f"{str(layout):25} -> {get_num_params(layout):10}")
