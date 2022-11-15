# This file serves as the template for the other ones,
# it has the basics you would need for the other ones 
# and to use the algorithms we set out to use.

# Import Section
import numpy as np
import os

# Define the main function.
def main():
    # Define our constants
    ROOT = os.path.dirname(os.path.abspath(__file__)) # root directory of this file
    TRAININGDATAFILE = 'poker-hand-training.csv'
    TESTDATAFILE = 'poker-hand-testing.csv'
    
    # Extract the data by using loadtxt and store it in the variable training_data.
    training_data = np.loadtxt(TRAININGDATAFILE, dtype=int, delimiter=',')

    # Splice the array of data to separate the labels from the rest of the data.
    train_x = training_data[:, :10]
    train_labels = training_data[:, 10]


if __name__ == '__main__':
    main()