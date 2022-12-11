# This file serves as the template for the other ones,
# it has the basics you would need for the other ones 
# and to use the algorithms we set out to use.

# Import Section
import matplotlib.pyplot as plt
import numpy as np
import os
import pdb
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import confusion_matrix

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

    clf = DecisionTreeClassifier(
        criterion="entropy",
        splitter="best",
        max_depth=None,
        random_state=10
    )
    clf.fit(train_x, train_labels)

    #Test the decision tree
    pred = clf.predict(test_x)

    #Compare training and test accuracy
    print("Train Accuracy =", np.mean(train_labels == clf.predict(train_x)))
    print("Test Accuracy =", np.mean(test_labels == pred))

    #Visualize the tree using matplotlib and plot_tree
    plot_tree(clf, max_depth=5, filled=True, fontsize=4)
    plt.show()




if __name__ == '__main__':
    main()