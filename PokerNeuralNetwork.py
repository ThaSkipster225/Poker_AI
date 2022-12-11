from sklearn import datasets
from sklearn.neural_network import MLPClassifier
from skimage.util import montage

import numpy as np

import matplotlib.pyplot as plt

import os

import tensorflow as tf
import keras.utils as KRSu
import keras.callbacks as KRScb
from keras.models import Sequential
from keras.layers import Input, Dense
from keras.optimizers import SGD

import pdb

def Neural():
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
    # numOutputs = len(np.unique(train_x))
    test_x = testing_data[:, :10]
    test_labels = testing_data[:,10]
    

    # Build the Neural Network
    clf = MLPClassifier(100, 'logistic', solver="adam", max_iter=1000, batch_size=55)
    clf.fit(train_x, train_labels)
    
    # Score Against Self
    score = (clf.score(test_x, test_labels))*100
    
    # Output Results
    print(f"Accuracy = {score}%")


#    model = Sequential()
#    model.add(Input(train_x))
#    model.add(Dense(units=1000, activation='relu', name='hidden1'))
#    model.add(Dense(units=500, activation='relu', name='hidden2',))
#    model.add(Dense(units=500, activation='relu', name='hidden3'))
#    model.add(Dense(units=numOutputs, activation='softmax', name='output'))
#    model.summary()

#    callback = KRScb.EarlyStopping(
#        monitor= 'loss',
#        min_delta=1e-2,
#        patience=15,
#        verbose=1
#    )

#    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
#    history = model.fit(train_x, train_labels, epochs=100, batch_size=100, callbacks=[callback], verbose=1)
#    metrics = model.evaluate(test_x, test_labels, verbose=0)

#    print(f'Accuracy = {metrics[1]:0.4f}')


if __name__ == '__main__':
    Neural()