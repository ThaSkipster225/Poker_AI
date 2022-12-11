# File to run the AI algorithms to classify poker hands.
# Super simple file that allows the user to pick which file they'd like to run.

import PokerNeuralNetwork
import PokerDecisionTree
import PokerSVM

def main():
    print("Welcome to the Poker Classifier, which classification algorithm would you like to run?\n1. Decision Trees\n2. Neural Networks\n3. SVMs (Caution: Takes a little while to finish running)\nPlease enter the number corresponding with your choice: ")

    while True:
        uInput = input()
        if (int(uInput) == 1):
            print()
            PokerDecisionTree.DecisionTree()
            print('\nWould you like to run another algorithm? (1. Decision Trees, 2. Neural Networks, 3. SVMs, q - Quit): ')
        elif (int(uInput) == 2):
            print()
            PokerNeuralNetwork.Neural()
            print('\nWould you like to run another algorithm? (1. Decision Trees, 2. Neural Networks, 3. SVMs, q - Quit): ')
        elif (int(uInput) == 3):
            print()
            PokerSVM.svm()
            print('\nWould you like to run another algorithm? (1. Decision Trees, 2. Neural Networks, 3. SVMs, q - Quit): ')
        elif (uInput.lower() == 'q'):
            print('Exiting application.')
            break
        else:
            print('Unrecognized input. Please try again')

if __name__ == "__main__":
    main()