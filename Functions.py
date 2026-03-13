from lingowords import words

import random

# The game (the code) randomly selects a word from the word list for the player to guess.
# The game displays the first letter of the word.
# A team has 5 attempts to guess the word.
# With each attempt, the letters that are in the correct position are colored green. Letters that are in the word but in the wrong position are shown in yellow.
# When a new attempt is made the correct letters must be there
# When a player guesses the word correctly, they can grab a ball from the ball pit.
# If a red ball is grabbed on the first attempt, the team is not allowed to grab a second time.
# At the end of the game, the players are asked if they want to play again.

def get_random_word():
    return random.choice(words)

