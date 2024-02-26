import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 10)

def check_winner(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != ' ' or board[0][i] == board[1][i] == board[2][i] != ' ':
            return board[i][i]  

    if board[0][0] == board[1][1] == board[2][2] != ' ' or board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[1][1]  

    return None

def is_board_full(board):
    for row in board:
        if ' ' in row:
            return False
    return True

def computer_move(board):
    empty_cells = [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']
    return random.choice(empty_cells) if empty_cells else None

def tic_tac_toe():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'

    while True:
        print_board(board)

        if current_player == 'X':  
            try:
                row = int(input(f"Player {current_player}, enter row ( 1,2 or 3): "))-1
                col = int(input(f"Player {current_player}, enter column (1,2 or 3): "))-1
                if not (0 <= row < 4 and 0 <= col < 4):
                    raise ValueError("Row and column must be between 0 and 2.")

            except ValueError as e:
                print(f"Invalid input. {e} Please try again.")
                continue
        else:  
            print(f"Player {current_player} (Computer) is making a move...")
            move = computer_move(board)
            if move:
                row, col = move
            else:
                print("No more moves available. It's a tie!")
                break

        if board[row][col] == ' ':
            board[row][col] = current_player
            winner = check_winner(board)

            if winner=='X':
                print_board(board)
                print(f"Player {winner} (USER) wins!")
                break
            elif winner=='O':
                print_board(board)
                print(f"Player {winner} (COMPUTER) wins!")
                break
            elif is_board_full(board):
                print_board(board)
                print("It's a tie!")
                break

            current_player = 'O' if current_player == 'X' else 'X'
        else:
            print("Cell already occupied. Try again.")

if __name__ == "__main__":
    tic_tac_toe()
