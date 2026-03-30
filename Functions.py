from lingowords import words

import random

from Actual_Opdracht import *
def get_random_word():

    return random.choice(words)


def guess_word():
    
    for i in range(5):

        print("Attempt", i + 1)
        print("guess:", Secret_Word[0], "_ _ _ _")


        while True:
            guess = input("Enter your guess: ")

            if len(guess) != 5:
                print("Word must be 5 letters.")
            else:
                guess_letters = list(guess)
                return guess, guess_letters
            

        