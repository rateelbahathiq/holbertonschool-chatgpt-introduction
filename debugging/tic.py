#!/usr/bin/python3

def print_board(board):
    """Print the current state of the Tic Tac Toe board."""
    for row in board:
        print(" | ".join(row))
        print("-" * 5)


def check_winner(board):
    """Check if there is a winner on the board.

    Returns:
        str: "X" or "O" if there is a winner, or None otherwise.
    """
    # Check rows
    for row in board:
        if row[0] != " " and row.count(row[0]) == len(row):
            return row[0]

    # Check columns
    for col in range(len(board[0])):
        if (
            board[0][col] == board[1][col] == board[2][col]
            and board[0][col] != " "
        ):
            return board[0][col]

    # Check diagonals
    if (
        board[0][0] == board[1][1] == board[2][2]
        and board[0][0] != " "
    ):
        return board[0][0]

    if (
        board[0][2] == board[1][1] == board[2][0]
        and board[0][2] != " "
    ):
        return board[0][2]

    return None


def tic_tac_toe():
    """Main game loop for Tic Tac Toe."""
    board = [[" "] * 3 for _ in range(3)]
    player = "X"
    moves = 0

    while True:
        print_board(board)

        # Get valid user input
        try:
            row = int(input(f"Enter row (0, 1, or 2) for player {player}: "))
            col = int(input(f"Enter column (0, 1, or 2) for player {player}: "))
        except ValueError:
            print("Invalid input. Please enter numbers only (0, 1, or 2).")
            continue

        # Validate range
        if row not in [0, 1, 2] or col not in [0, 1, 2]:
            print("Invalid position. Row and column must be 0, 1, or 2.")
            continue

        # Check if spot is free
        if board[row][col] != " ":
            print("That spot is already taken! Try again.")
            continue

        # Place the move
        board[row][col] = player
        moves += 1

        # Check for winner
        winner = check_winner(board)
        if winner:
            print_board(board)
            print("Player " + winner + " wins!")
            break

        # Check for draw
        if moves == 9:
            print_board(board)
            print("It's a draw!")
            break

        # Switch player
        player = "O" if player == "X" else "X"


if __name__ == "__main__":
    tic_tac_toe()
