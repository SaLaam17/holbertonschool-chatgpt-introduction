#!/usr/bin/python3

def print_board(board):
    """
    Prints the current state of the game board.

    Parameters:
    board (list): A 2D list representing the game board.

    Returns:
    None
    """
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    """
    Checks if there is a winner in the game.

    Parameters:
    board (list): A 2D list representing the game board.

    Returns:
    bool: True if there is a winner, False otherwise.
    """
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

def tic_tac_toe():
    """
    Main function to run the Tic-Tac-Toe game.

    Parameters:
    None

    Returns:
    None
    """
    board = [[" "]*3 for _ in range(3)]
    player = "X"
    while True:
        print_board(board)
        try:
            row = int(input("Enter row (0, 1, or 2) for player " + player + ": "))
            col = int(input("Enter column (0, 1, or 2) for player " + player + ": "))
            if row not in [0, 1, 2] or col not in [0, 1, 2]:
                print("Invalid input. Please enter 0, 1, or 2.")
                continue
        except ValueError:
            print("Invalid input. Please enter numbers only.")
            continue

        if board[row][col] == " ":
            board[row][col] = player
            if check_winner(board):
                print_board(board)
                print("Player " + player + " wins!")
                break
            if player == "X":
                player = "O"
            else:
                player = "X"
        else:
            print("That spot is already taken! Try again.")

        if all(cell != " " for row in board for cell in row):
            print_board(board)
            print("It's a tie!")
            break

if __name__ == "__main__":
    tic_tac_toe()
