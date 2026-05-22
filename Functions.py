from lingowords import words
from bingo import check_bingo_card

import random

correct_words_in_a_row = 0

failed_words_in_a_row = 0

green_balls_grabbed = 0

red_balls_grabbed = 0

ask_play_again = False

ball_pit = ["red_ball", "red_ball", "red_ball", "green_ball", "green_ball", "green_ball",
            "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16"]


# from Actual_Opdracht import *
def get_random_word():

    return random.choice(words)

def reset_game():
    global green_balls_grabbed, red_balls_grabbed, ask_play_again, ball_pit

    green_balls_grabbed = 0
    red_balls_grabbed = 0

    ball_pit = ["red_ball", "red_ball", "red_ball", "green_ball", "green_ball", "green_ball",
                "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16"]



def play_again():    
    while True:
        play_again = input("Do you want to play again? (yes/no): ").strip().lower()

        if play_again == "yes":
            reset_game()
            return True

        elif play_again == "no":
            print("Goodbye!")
            return False

        else:
            print("Please enter 'yes' or 'no'.")
             


def grab_ball_function(bingo_card, marked_numbers):
    global red_balls_grabbed, green_balls_grabbed, ball_pit
    
    for i in range(2):
        random_ball = random.choice(ball_pit)
        ball_pit.remove(random_ball)
        
        if random_ball == "red_ball":
            if i == 0:
                print("red ball!")
            else:
                print("second ball: red ball!")
            red_balls_grabbed += 1
            print(f"red ball amount {red_balls_grabbed}")
            if red_balls_grabbed == 3:
                print("You grabbed 3 red balls! Game over.")
                return "lose"
 
            break
        elif random_ball == "green_ball":
            if i == 0:  
                print("first ball: green ball! you may grab another ball.")
            else:
                print("second ball: green ball!")
            green_balls_grabbed += 1
            print(f"green ball amount {green_balls_grabbed}")
            if green_balls_grabbed == 3:
                print("You grabbed 3 green balls! You win!")
                return "win"
                
            
        else:
            if i == 0:
                print(f"first ball: {random_ball}. you may grab another ball!")
            else:
                print(f"second ball: {random_ball}.")
            
            marked_numbers, is_bingo = check_bingo_card(bingo_card, random_ball, marked_numbers)
            if is_bingo:
                print("BINGO! You win!")
                return "win"
                    
    return "continue"