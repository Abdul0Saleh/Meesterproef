def check_bingo_card(bingo_card, pulled_number, marked_numbers):
    # Convert pulled number to int once
    number = int(pulled_number)

    # Put the card into a grid (4 rows)
    grid = []
    for row in bingo_card:
        grid.append(row)

    # Check if number is on the card
    found = False
    for row in grid:
        for value in row:
            if value == number:
                found = True

    if found == False:
        print("Number", pulled_number, "not found in your bingo card.")
        return marked_numbers, False

    # Mark the number
    marked_numbers.add(number)
    print("Number", pulled_number, "marked!")

    # -------------------
    # Check rows
    # -------------------
    row_index = 0
    for row in grid:
        row_index = row_index + 1
        row_complete = True

        for value in row:
            if value not in marked_numbers:
                row_complete = False

        if row_complete == True:
            print("BINGO! Complete row", row_index)
            return marked_numbers, True

    # -------------------
    # Check columns
    # -------------------
    for col in range(4):
        column_complete = True

        for row in range(4):
            if grid[row][col] not in marked_numbers:
                column_complete = False

        if column_complete == True:
            print("BINGO! Complete column", col + 1)
            return marked_numbers, True

    # -------------------
    # Check diagonal top-left -> bottom-right
    # -------------------
    diagonal1_complete = True
    for i in range(4):
        if grid[i][i] not in marked_numbers:
            diagonal1_complete = False

    if diagonal1_complete == True:
        print("BINGO! Diagonal (top-left to bottom-right)")
        return marked_numbers, True

    # -------------------
    # Check diagonal top-right -> bottom-left
    # -------------------
    diagonal2_complete = True
    for i in range(4):
        if grid[i][3 - i] not in marked_numbers:
            diagonal2_complete = False

    if diagonal2_complete == True:
        print("BINGO! Diagonal (top-right to bottom-left)")
        return marked_numbers, True

    return marked_numbers, False