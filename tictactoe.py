def print_board(field):
    start_end = ("-"*13)
    print(start_end)
    for i in range(3):
        print("|", field[i][0], "|", field[i][1], "|", field[i][2], "|")
        print(start_end)

def check_win(field, player):
    #rows check
    for i in range(3):
        if field[i][0] == field[i][1] == field[i][2] == player:
            return True

    #columns check
    for i in range(3):
        if field[0][i] == field[1][i] == field[2][i] == player:
            return True

    #diagonals check
    if field[0][0] == field[1][1] == field[2][2] == player:
        return True

    if field[0][2] == field[1][1] == field[2][0] == player:
        return True

    return False

def tic_tac_toe():
    # Starting function. Access to individual fields on the board
    field = [[" ", " ", " "],
             [" ", " ", " "],
             [" ", " ", " "]]

    # Player with X starts
    player = "x"

    # End condition
    while True:
        print_board(field)

        # Get input for row and column
        while True:
            try:
                row = int(input("Enter row for placement (0-2): "))
                col = int(input("Enter column for placement (0-2): "))
                if not (0 <= row <= 2 and 0 <= col <= 2):
                    raise ValueError()
                #check what is entered coresponds to an empty cell
                if field[row][col] != " ":
                    raise ValueError()
                break
            except ValueError:
                print("Invalid input! Please enter two integers between 0 and 2 that represent an empty cell.")

        # Move
        field[row][col] = player

        # Check if the game is over
        if check_win(field, player):
            print_board(field)
            print(f"Player {player} wins!")
            break

        # Check if there is a tie
        if all([field[i][j] != " " for i in range(3) for j in range(3)]):
            print_board(field)
            print("Tie game!")
            break

        # Switch between players/symbols on each turn
        if player == "x":
            player = "o"
        else:
            player = "x"
