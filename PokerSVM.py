# Support Vector Machine for the classification of Poker Hands.f
# Coded by Sebastian 'Skippy' Paquette

# Import Section
import numpy as np
import os
from sklearn import svm
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score

# Define the main function.
def support():
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
    numoutputs = len(np.unique(train_labels))

    # Training
    clf = svm.SVC(
        kernel='poly'
        , C=0.1
        , decision_function_shape='ovr'
        , degree=3
        , verbose=True
        , break_ties=True
        )

    print('Beginning Training')
    clf.fit(train_x, train_labels)
    print('Training Ended')

    # Predict
    print('Beginning Testing')
    classifer_pred = clf.predict(test_x)
    print('Testing ended')

    # Get accuracy
    print(f'{accuracy_score(test_labels, classifer_pred)*100}% accurate')


if __name__ == '__main__':
    support()