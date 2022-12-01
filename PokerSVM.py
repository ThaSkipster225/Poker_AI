# Support Vector Machine for the classification of Poker Hands.f
# Coded by Sebastian 'Skippy' Paquette

# Import Section
import numpy as np
import os
from sklearn import svm
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score

# Define the main function.
def main():
    # Define our constants
    ROOT = os.path.dirname(os.path.abspath(__file__)) # root directory of this file
    TRAININGDATAFILE = 'poker-hand-training.csv'
    TESTDATAFILE = 'poker-hand-testing.csv'
    
    # Extract the data by using loadtxt and store it in the variable training_data.
    training_data = np.loadtxt(TRAININGDATAFILE, dtype=int, delimiter=',')
    testing_data = np.loadtxt(TESTDATAFILE, dtype=int, delimiter=',')

    # Splice the array of data to separate the labels from the rest of the data.
    train_x = training_data[:, :10]
    train_labels = training_data[:, 10]
    test_x = testing_data[:, :10]
    test_labels = testing_data[:,10]

    # Training
    clf = svm.SVC()
    clf.fit(train_x, train_labels)

    # Predict
    classifer_pred = clf.predict(test_x)

    # Get accuracy
    print(accuracy_score(test_labels, classifer_pred)*100)


if __name__ == '__main__':
    main()