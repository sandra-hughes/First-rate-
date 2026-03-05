"""Simple terminal Tic-Tac-Toe game for two players."""


WIN_LINES = (
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8),
    (0, 3, 6),
    (1, 4, 7),
    (2, 5, 8),
    (0, 4, 8),
    (2, 4, 6),
)


def render_cell(board, index):
    return board[index] if board[index] != " " else str(index + 1)


def print_board(board):
    print()
    print(f" {render_cell(board, 0)} | {render_cell(board, 1)} | {render_cell(board, 2)} ")
    print("---+---+---")
    print(f" {render_cell(board, 3)} | {render_cell(board, 4)} | {render_cell(board, 5)} ")
    print("---+---+---")
    print(f" {render_cell(board, 6)} | {render_cell(board, 7)} | {render_cell(board, 8)} ")
    print()


def get_winner(board):
    for a, b, c in WIN_LINES:
        if board[a] != " " and board[a] == board[b] == board[c]:
            return board[a]
    return None


def is_draw(board):
    return all(cell != " " for cell in board)


def get_move(board, player):
    while True:
        raw = input(f"Player {player}, choose a position (1-9): ").strip()
        if raw.lower() in {"q", "quit", "exit"}:
            return None
        if not raw.isdigit():
            print("Invalid input. Please enter a number from 1 to 9.")
            continue
        move = int(raw)
        if move < 1 or move > 9:
            print("Out of range. Please enter a number from 1 to 9.")
            continue
        idx = move - 1
        if board[idx] != " ":
            print("That position is already taken. Try another one.")
            continue
        return idx


def play_round():
    board = [" "] * 9
    player = "X"

    while True:
        print_board(board)
        idx = get_move(board, player)
        if idx is None:
            print("Game ended by user.")
            return False

        board[idx] = player
        winner = get_winner(board)
        if winner:
            print_board(board)
            print(f"Player {winner} wins!")
            return True
        if is_draw(board):
            print_board(board)
            print("Draw game!")
            return True

        player = "O" if player == "X" else "X"


def ask_replay():
    while True:
        answer = input("Play again? (y/n): ").strip().lower()
        if answer in {"y", "yes"}:
            return True
        if answer in {"n", "no"}:
            return False
        print("Please enter y or n.")


def main():
    print("Tic-Tac-Toe")
    print("Enter q anytime to quit.")

    while True:
        finished = play_round()
        if not finished:
            break
        if not ask_replay():
            break

    print("Thanks for playing.")


if __name__ == "__main__":
    main()
