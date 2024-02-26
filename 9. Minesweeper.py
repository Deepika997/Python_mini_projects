import random
def generate_board(rows, cols, num_mines):
    board = [[' ' for _ in range(cols)] for _ in range(rows)]
    mines = random.sample(range(rows * cols), num_mines)
    for idx in mines:
        row = idx // cols
        col = idx % cols
        board[row][col] = '*'
    return board
def print_board(board):
    for r in range(len(board)):
        for c in range(len(board[0])):
            if board[r][c]=="*":
                print(" ",end=" |")
            else:
                print(board[r][c],end=" |")
        print()
        print("-"*20)
def count_adjacent_mines(board, row, col):
    count = 0
    for r in range(row-1, row+2):
        for c in range(col-1, col+2):
            if 0 <= r < len(board) and 0 <= c < len(board[0]) and board[r][c] == '*':
                count += 1
    return count
def reveal_cells(board, row, col):
    if board[row][col] != ' ':
        return
    board[row][col] = str(count_adjacent_mines(board, row, col))
    if board[row][col] == '0':
        for r in range(row-1, row+2):
            for c in range(col-1, col+2):
                if 0 <= r < len(board) and 0 <= c < len(board[0]):
                    reveal_cells(board, r, c)
def play_minesweeper(rows, cols, num_mines):
    board = generate_board(rows, cols, num_mines)
    print_board(board)
    while True:
        row = int(input("Enter row: "))
        col = int(input("Enter column: "))
        if row<rows and col<cols:
            if board[row][col] == '*':
                print("Game over! You hit a mine.")
                break
            reveal_cells(board, row, col)
            print_board(board)
            if all(cell != ' ' for row in board for cell in row):
                print("Congratulations! You've cleared all safe cells.")
                break
        else:
            print("please enter in range values only.")
rows = int(input("Enter the row length: "))
cols = int(input("Enter the col length: "))
num_mines = int(input("Enter the no of mines: "))
play_minesweeper(rows, cols, num_mines)
