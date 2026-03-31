from Functions import *

from lingowords import *

from termcolor import colored

# The game (the code) randomly selects a word from the word list for the player to guess.
# The game displays the first letter of the word.
# A team has 5 attempts to guess the word.
# With each attempt, the letters that are in the correct position are colored green. Letters that are in the word but in the wrong position are shown in yellow.
# When a new attempt is made the correct letters must be there
# When a player guesses the word correctly, they can grab a ball from the ball pit.
# If a red ball is grabbed on the first attempt, the team is not allowed to grab a second time.
# At the end of the game, the players are asked if they want to play again.

# 5 attempts to guess word

while True:

    Secret_Word = get_random_word()
    secret_letters = list(Secret_Word)
    print(Secret_Word)

    for i in range(5):

        print("Attempt", i + 1)
        print("guess:", Secret_Word[0], "_ _ _ _")

        while True:
            guess = input("Enter your guess: ")

            if len(guess) != 5:
                print("Word must be 5 letters.")
            else:
                break

        guess_letters = list(guess)

        if guess == Secret_Word:
            print("Congratulations! You guessed the word.")
            guessed = True
            break
        elif guess != Secret_Word and i >= 4:
            print("Sorry, you've used all attempts. The word was:", Secret_Word)
        
        else:
            print("Wrong guess. Try again.")

            remaining_letters = secret_letters.copy()
            result = [""] * 5

            for j in range(5):
                if guess_letters[j] == secret_letters[j]:
                    result[j] = "green"
                    remaining_letters[j] = None

            for j in range(5):
                if result[j] == "":
                    if guess_letters[j] in remaining_letters:
                        result[j] = "yellow"
                        remaining_letters[remaining_letters.index(guess_letters[j])] = None
                    else:
                        result[j] = "gray"

            for j in range(5):

                if result[j] == "green":
                    print(colored(guess_letters[j], 'green'), end=" ")
                elif result[j] == "yellow":
                    print(colored(guess_letters[j], 'yellow'), end=" ")
                else:
                    print(colored(guess_letters[j], 'red'), end=" ")

            
    if guessed:
        print("You can grab a ball from the ball pit!")



    while True:
        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again == "yes":
            break
        elif play_again == "no":
            print("Goodbye!")
            exit()
        else:
            print("Please enter 'yes' or 'no'.")

