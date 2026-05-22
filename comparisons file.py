def grab_ball_function():
    global red_balls_grabbed, green_balls_grabbed, ball_pit

    for i in range(2):

        random_ball = random.choice(ball_pit)
        ball_pit.remove(random_ball)

        if random_ball == "red_ball":
            print("red ball!" if i == 0 else "second ball: red ball!")

            red_balls_grabbed += 1

            if red_balls_grabbed == 3:
                print(" You grabbed 3 red balls! YOU LOSE.")
                return "lose"

            break

        elif random_ball == "green_ball":
            print("green ball!" if i == 0 else "second ball: green ball!")

            green_balls_grabbed += 1

            if green_balls_grabbed == 3:
                print(" You grabbed 3 green balls! YOU WIN!")
                return "win"

        else:
            print(f"{'first' if i == 0 else 'second'} ball: {random_ball}")

            while True:
                bingo = input("Did you get bingo? (yes/no): ").lower()

                if bingo == "yes":
                    print(" Bingo! YOU WIN!")
                    return "win"

                elif bingo == "no":
                    break

                else:
                    print("Please type yes or no.")

    return "continue"