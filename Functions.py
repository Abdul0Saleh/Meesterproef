from lingowords import words

import random

correct_words_in_a_row = 0

failed_words_in_a_row = 0

green_balls_grabbed = 0

red_balls_grabbed = 0

ask_play_again = False

ball_pit = ["red_ball", "red_ball", "red_ball", "red_ball", "red_ball", "red_ball", "green_ball", "green_ball", "green_ball",
"green_ball", "green_ball", "green_ball", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16"]


# from Actual_Opdracht import *
def get_random_word():

    return random.choice(words)

# def guess_word():
    
#     for i in range(5):

#         print("Attempt", i + 1)
#         print("guess:", Secret_Word[0], "_ _ _ _")


#         while True:
#             guess = input("Enter your guess: ")

#             if len(guess) != 5:
#                 print("Word must be 5 letters.")
#             else:
#                 guess_letters = list(guess)
#                 return guess, guess_letters

def play_again():    
    while True:
        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again == "yes":
            break
        elif play_again == "no":
            print("Goodbye!")
            exit()
        else:
            print("Please enter 'yes' or 'no'.")
             


def grab_ball_function():
    global red_balls_grabbed, green_balls_grabbed
    for i in range(2):
        random_ball = random.choice(ball_pit)
        ball_pit.remove(random_ball)
        if random_ball == "red_ball":
            if i == 0:
                print("red ball!")
            else:
                print("second ball: red ball!")
            red_balls_grabbed += 1
            if red_balls_grabbed == 3:
                print("You grabbed 3 red balls! Game over.")
                ask_play_again = True
                break
            else:
                break
        elif random_ball == "green_ball":
            if i == 0:  
                print("first ball: green ball! you may grab another ball.")
            else:
                print("second ball: green ball!")
            green_balls_grabbed += 1
            if green_balls_grabbed == 3:
                print("You grabbed 3 green balls! You win!")
                ask_play_again == True
                break
                
            
        else:
            if i == 0:
                print(f"first ball: {random_ball}. you may grab another ball!")
            else:
                print(f"second ball: {random_ball}.")

            