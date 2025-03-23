#Treasure Hunt Game
import random

def create_board(rows, cols):
    return [['*' for _ in range(cols)] for _ in range(rows)]

def display_board(board):
    for row in board:
        print(' '.join(row))

def get_valid_position(prompt, max_val):
    while True:
        try:
            pos = int(input(prompt)) - 1  # Convert to zero-based index
            if 0 <= pos < max_val:
                return pos
            else:
                print(f"Invalid input! Enter a number between 1 and {max_val}.")
        except ValueError:
            print("Invalid input! Please enter a valid number.")

def main():
    print("Welcome to the Treasure Hunt Game!")

    # Get board size from the player
    rows = get_valid_position("Enter number of rows (min 2): ", 100) + 1
    cols = get_valid_position("Enter number of columns (min 2): ", 100) + 1
    board = create_board(rows, cols)

    # Get treasure location
    print("Choose where to hide the treasure!")
    treasure_row = get_valid_position("Enter row number: ", rows)
    treasure_col = get_valid_position("Enter column number: ", cols)
    board[treasure_row][treasure_col] = 'T'

    # Place a random trap
    while True:
        trap_row = random.randint(0, rows - 1)
        trap_col = random.randint(0, cols - 1)
        if (trap_row, trap_col) != (treasure_row, treasure_col):
            break

    print("\nHere is your game board:")
    display_board(board)

    # Player guessing loop
    while True:
        print("\nTime to find the treasure!")
        guess_row = get_valid_position("Enter your guess for row: ", rows)
        guess_col = get_valid_position("Enter your guess for column: ", cols)

        if (guess_row, guess_col) == (treasure_row, treasure_col):
            print("Congratulations! You found the treasure! 🏆")
            break
        elif (guess_row, guess_col) == (trap_row, trap_col):
            print("Oh no! You fell into a trap! Game Over. ☠️")
            break
        else:
            print("No treasure here! Try again.")
            break

if __name__ == "__main__":
    main()
