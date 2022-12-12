# File to run the AI algorithms to classify poker hands.
# Super simple file that allows the user to pick which file they'd like to run.

import PokerNeuralNetwork
import PokerDecisionTree
import PokerSVM
import time

def main():
    print("Welcome to the Poker Classifier, which classification algorithm would you like to run?\n1. Decision Trees\n2. Neural Networks\n3. SVMs (Caution: Takes a little while to finish running)\nPlease enter the number corresponding with your choice: ")

    while True:
        uInput = input()
        if (int(uInput) == 1):
            start = time.time()
            print('Decisition Tree Selected...')
            PokerDecisionTree.DecisionTree()
            end = time.time()
            print(f'\nTotal elapsed time was {end-start:.2f} seconds.')
            print('\nWould you like to run another algorithm? (1. Decision Trees, 2. Neural Networks, 3. SVMs, q - Quit): ')
        elif (int(uInput) == 2):
            print('Neural Network Selected...')
            start = time.time()
            PokerNeuralNetwork.Neural()
            end = time.time()
            print(f'\nTotal elapsed time was {end-start:.2f} seconds.')
            print('\nWould you like to run another algorithm? (1. Decision Trees, 2. Neural Networks, 3. SVMs, q - Quit): ')
        elif (int(uInput) == 3):
            print('SVM Selected...')
            start = time.time()
            PokerSVM.support()
            end = time.time()
            print(f'\nTotal elapsed time was {end-start:.2f} seconds.')
            print('\nWould you like to run another algorithm? (1. Decision Trees, 2. Neural Networks, 3. SVMs, q - Quit): ')
        elif (uInput.lower() == 'q'):
            print('Exiting application.')
            break
        else:
            print('Unrecognized input. Please try again')

if __name__ == "__main__":
    main()