import numpy as np

# loss in logcosh
logcosh_loss = 0.0065443563 #-> mae_loss = 0.11453073780513061
# logcosh_loss = 0.0068427048 #-> mae_loss = 0.11711811618233561
# logcosh_loss = 2.4474809527

def logcosh(x):
    return np.log((np.exp(x)+np.exp(-x))/2)

def logcosh_inverse(x):
    return np.log(np.sqrt(np.exp(2*x) - 1) + np.exp(x))

mae_loss = logcosh_inverse(logcosh_loss)

print(f"{mae_loss=}")

check = logcosh(mae_loss)
print(f"{check=}")
print(f"{logcosh_loss=}")
