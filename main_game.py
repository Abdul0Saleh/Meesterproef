from Functions import *
from lingowords import *
from termcolor import colored
from bingo_display import start_bingo_window, update_cards, set_active_team, stop_bingo_window
import time


def play_round(team_number, bingo_card):
    team_name = f"Team {team_number}"
    print(f"\n{'='*40}")
    print(f"       {team_name}'s Turn")
    print(f"{'='*40}")

    set_active_team(team_number)

    Secret_Word = get_random_word()
    secret_letters = list(Secret_Word)

    print(f"[CHEATS ON] Secret Word: {Secret_Word}")

    guessed = False

    for i in range(5):
        print(f"\nAttempt {i + 1}")
        print(f"First letter: {Secret_Word[0]}  _ _ _ _")

        while True:
            guess = input(f"{team_name} — Enter your guess: ").strip().lower()
            if len(guess) != 5:
                print("Word must be exactly 5 letters.")
            else:
                break

        guess_letters = list(guess)

        if guess == Secret_Word:
            print(f"\nCorrect! {team_name} guessed the word!")
            guessed = True
            break
        elif i >= 4:
            print(f"\nOut of attempts! The word was: {Secret_Word}")
        else:
            print("Wrong guess. Here's a hint:")

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
                    print(colored(guess_letters[j].upper(), 'green'), end=" ")
                elif result[j] == "yellow":
                    print(colored(guess_letters[j].upper(), 'yellow'), end=" ")
                else:
                    print(colored(guess_letters[j].upper(), 'red'), end=" ")
            print()

    if guessed:
        print(f"\n{team_name} gets to grab from the ball pit!")
        result = grab_ball_function(team_number)
        return result

    return "continue"


bingo_card_team1 = generate_bingo_card()
bingo_card_team2 = generate_bingo_card()

start_bingo_window(bingo_card_team1, bingo_card_team2)
time.sleep(0.5)

while True:
    print("\n" + "="*40)
    print("      WELCOME TO LINGO BINGO!")
    print("="*40)

    game_over = False

    while not game_over:
        for team_number in [1, 2]:
            bingo_card = bingo_card_team1 if team_number == 1 else bingo_card_team2

            outcome = play_round(team_number, bingo_card)

            if outcome == "win":
                print(f"\nTeam {team_number} wins the game!")
                game_over = True
                break
            elif outcome == "lose":
                other_team = 2 if team_number == 1 else 1
                print(f"\nTeam {team_number} is eliminated! Team {other_team} wins!")
                game_over = True
                break

    set_active_team(0)

    if not play_again():
        stop_bingo_window()
        break

    bingo_card_team1 = generate_bingo_card()
    bingo_card_team2 = generate_bingo_card()
    update_cards(bingo_card_team1, bingo_card_team2)