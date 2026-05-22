from random import randint
from termcolor import colored


def generate_bingo_card():
    number_list = []

    while len(number_list) < 16:
        number = randint(1, 16)
        if number not in number_list:
            number_list.append(number)


    row_1 = number_list[0:4]
    row_2 = number_list[4:8]
    row_3 = number_list[8:12]
    row_4 = number_list[12:16]

    return row_1, row_2, row_3, row_4

def check_bingo_card(bingo_card, pulled_number, marked_numbers):

    row_1, row_2, row_3, row_4 = bingo_card
    grid = [row_1, row_2, row_3, row_4]
    
    number_found = False
    for row in grid:
        if int(pulled_number) in row:
            number_found = True
            break
    
    if not number_found:
        print(f"Number {pulled_number} not found in your bingo card.")
        return marked_numbers, False
    
    marked_numbers.add(int(pulled_number))
    colored_number = colored(pulled_number, 'green')
    print(f"Number {colored_number} marked!")
    
    for i, row in enumerate(grid, 1):
        if all(num in marked_numbers for num in row):
            print(f"BINGO! Complete row {i}!")
            return marked_numbers, True
    
    for col in range(4):
        if all(grid[row][col] in marked_numbers for row in range(4)):
            print(f"BINGO! Complete column {col + 1}!")
            return marked_numbers, True
    
    if all(grid[i][i] in marked_numbers for i in range(4)):
        print("BINGO! Diagonal (top-left to bottom-right)!")
        return marked_numbers, True
    
    if all(grid[i][3-i] in marked_numbers for i in range(4)):
        print("BINGO! Diagonal (top-right to bottom-left)!")
        return marked_numbers, True
    
    return marked_numbers, False