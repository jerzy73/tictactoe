class tictactoe:
    def __init__(self):
        self.field = [[" ", " ", " "],
                      [" ", " ", " "],
                      [" ", " ", " "]]
        self.player = "x"

    def print_board(self):
        start_end = ("-"*13)
        print(start_end)
        for i in range(3):
            print("|", self.field[i][0], "|", self.field[i][1], "|", self.field[i][2], "|")
            print(start_end)

    def check_win(self):
        # rows check
        for i in range(3):
            if self.field[i][0] == self.field[i][1] == self.field[i][2] == self.player:
                return True

        # columns check
        for i in range(3):
            if self.field[0][i] == self.field[1][i] == self.field[2][i] == self.player:
                return True

        # diagonals check
        if self.field[0][0] == self.field[1][1] == self.field[2][2] == self.player:
            return True

        if self.field[0][2] == self.field[1][1] == self.field[2][0] == self.player:
            return True

        return False

    def play(self):
        while True:
            self.print_board()

            # Get input for row and column
            while True:
                try:
                    row = int(input("Enter row for placement (0-2): "))
                    col = int(input("Enter column for placement (0-2): "))
                    if not (0 <= row <= 2 and 0 <= col <= 2):
                        raise ValueError()
                    # check what is entered corresponds to an empty cell
                    if self.field[row][col] != " ":
                        raise ValueError()
                    break
                except ValueError:
                    print("Invalid input! Please enter two integers between 0 and 2 that represent an empty cell.")

            # Move
            self.field[row][col] = self.player

            # Check if the game is over
            if self.check_win():
                self.print_board()
                print(f"Player {self.player} wins!")
                break

            # Check if there is a tie
            if all([self.field[i][j] != " " for i in range(3) for j in range(3)]):
                self.print_board()
                print("Tie game!")
                break

            # Switch between players/symbols on each turn
            if self.player == "x":
                self.player = "o"
            else:
                self.player = "x"

        # Check if the game is over
        if self.check_win():
            self.print_board()
            print(f"Player {self.player} wins!")

        # Check if there is a tie
        if all([self.field[i][j] != " " for i in range(3) for j in range(3)]):
            self.print_board(field)
            print("Tie game!")

        # Switch between players/symbols on each turn
        if self.player == "x":
            self.player = "o"
        else:
            self.player = "x"

game = tictactoe()
game.play()
