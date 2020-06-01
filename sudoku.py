import random

board = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
]

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
rem_num = [0, 1, 2, 3, 4, 5, 6, 7, 8]


# Check for blank cells on the board. If there's a blank cell, it will return which position it is.
def check_blank():
    for x in range(9):
        for y in range(9):
            if board[x][y] == 0:
                return x, y
    return False


# Check if the number is valid for the blank cell on the board.
def check_valid(x, y, num):
    # Checking for x axis
    for x_pos in range(len(board[x])):
        if board[x][x_pos] == num:
            return False

    # Checking for y axis
    for y_pos in range(9):
        if board[y_pos][y] == num:
            return False

    # Checking inside the box
    x_box = (x//3) * 3
    y_box = (y//3) * 3

    for i_x in range(x_box, x_box + 3):
        for i_y in range(y_box, y_box + 3):
            if board[i_x][i_y] == num:
                return False
    return True


# Generate Sudoku board using the shuffled numbers
def generate_board():
    find = check_blank()
    if not find:
        return True
    else:
        x, y = find

    # random number from 1-9
    res = random.sample(numbers, len(numbers))
    for num in res:
        if check_valid(x, y, num):
            board[x][y] = num
            if generate_board():
                return True
            board[x][y] = 0
    return


# Removing random numbers on the Sudoku board
def remove_numbers():
    for x in range(9):
        y_len = random.randint(5, 7)
        random.shuffle(rem_num)
        ctr = 0
        for y in range(y_len):
            board[x][rem_num[ctr]] = 0
            ctr += 1


# Solving the puzzle (with the removed numbers on the Sudoku board)
def solve():
    find = check_blank()
    if not find:
        return True
    else:
        x, y = find

    for num in range(1, 10):
        if check_valid(x, y, num):
            board[x][y] = num
            if solve():
                return True
            board[x][y] = 0
    return


# Printing the formatted board
def print_board():
    for x in range(9):
        if x % 3 == 0:
            print("-------------------------------------------")
        for y in range(9):
            if y % 3 == 0:
                print("|", end=" ")
            if y == 8:
                if board[x][y] == 0:
                    print(" " + "." + "  |")
                else:
                    print(" " + str(board[x][y]) + "  |")
            else:
                if board[x][y] == 0:
                    print(" " + "." + " ", end=" ")
                else:
                    print(" " + str(board[x][y]) + " ", end=" ")
    print("-------------------------------------------")


print("--Sudoku Generator and Solver--")
generate_board()
remove_numbers()
print("")
print("Original Puzzle")
print_board()
print("")
print("Solved Puzzle")
solve()
print_board()
