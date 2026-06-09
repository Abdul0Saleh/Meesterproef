from lingowords import words
from random import randint
from bingo_display import flash_number, set_active_team
import random

green_balls_grabbed_team1 = 0
red_balls_grabbed_team1 = 0
green_balls_grabbed_team2 = 0
red_balls_grabbed_team2 = 0

ball_pit = ["red_ball", "red_ball", "red_ball", "green_ball", "green_ball", "green_ball",
            "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16"]


def get_random_word():
    return random.choice(words)


def reset_game():
    global green_balls_grabbed_team1, red_balls_grabbed_team1
    global green_balls_grabbed_team2, red_balls_grabbed_team2, ball_pit

    green_balls_grabbed_team1 = 0
    red_balls_grabbed_team1 = 0
    green_balls_grabbed_team2 = 0
    red_balls_grabbed_team2 = 0

    ball_pit = ["red_ball", "red_ball", "red_ball", "green_ball", "green_ball", "green_ball",
                "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16"]

# use as initializer^^^


def play_again():
    while True:
        answer = input("Do you want to play again? (yes/no): ").strip().lower()
        if answer == "yes":
            reset_game()
            return True
        elif answer == "no":
            print("Goodbye!")
            return False
        else:
            print("Please enter 'yes' or 'no'.")

# try except ^


def generate_bingo_card():
    number_list = []
    while len(number_list) < 16:
        number = randint(1, 64)
        if number not in number_list:
            number_list.append(number)

    row_1 = number_list[0:4]
    row_2 = number_list[4:8]
    row_3 = number_list[8:12]
    row_4 = number_list[12:16]

    return row_1, row_2, row_3, row_4
# ^array ipv seperate variables

def grab_ball_function(team_number):
    global red_balls_grabbed_team1, green_balls_grabbed_team1
    global red_balls_grabbed_team2, green_balls_grabbed_team2, ball_pit

    if team_number == 1:
        red_balls_grabbed  = red_balls_grabbed_team1
        green_balls_grabbed = green_balls_grabbed_team1
    else:
        red_balls_grabbed  = red_balls_grabbed_team2
        green_balls_grabbed = green_balls_grabbed_team2

    for i in range(2):
        if not ball_pit:
            ball_pit.extend(["red_ball", "red_ball", "red_ball", "green_ball", "green_ball", "green_ball",
                              "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16"])

        random_ball = random.choice(ball_pit)
        ball_pit.remove(random_ball)

        if random_ball == "red_ball":
            label = "first" if i == 0 else "second"
            print(f"{label} ball: RED BALL!")
            red_balls_grabbed += 1

            if team_number == 1:
                red_balls_grabbed_team1 = red_balls_grabbed
            else:
                red_balls_grabbed_team2 = red_balls_grabbed

            print(f"Team {team_number} red balls: {red_balls_grabbed}")

            if red_balls_grabbed == 3:
                print(f"Team {team_number} grabbed 3 red balls! They lose!")
                return "lose"

            if i == 0:
                print("Red ball on first grab — no second grab allowed.")
            break

        elif random_ball == "green_ball":
            label = "first" if i == 0 else "second"
            print(f"{label} ball: GREEN BALL!")
            green_balls_grabbed += 1

            if team_number == 1:
                green_balls_grabbed_team1 = green_balls_grabbed
            else:
                green_balls_grabbed_team2 = green_balls_grabbed

            print(f"Team {team_number} green balls: {green_balls_grabbed}")

            if green_balls_grabbed == 3:
                print(f"Team {team_number} grabbed 3 green balls! They win!")
                return "win"

            if i == 0:
                print("Green ball — you may grab a second ball!")

        else:
            label = "first" if i == 0 else "second"
            print(f"{label} ball: number {random_ball}!")
            print(f"Mark number {random_ball} if you have it on your card!")
            flash_number(random_ball)

            if i == 0:
                print("Number ball — you may grab a second ball!")

    return "continue"