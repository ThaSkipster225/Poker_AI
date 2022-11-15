# This file will allow you to choose which of the 
# other Python files you want to run from this repository.

import numpy as np

data = np.loadtxt('poker-hand-training.csv', dtype=int, delimiter=',')

x = data[:, :10]
labels = data[:, 10]

print(labels)