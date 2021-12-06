with open('numbers.txt') as f:
    numbers = f.read().split(",")
    numbers = [int(n) for n in numbers]

with open('boards.txt') as f:
    lines = [line.strip().split(" ") for line in f]
    lines[:] = [line for line in lines if line != ['']]
    for line in lines:
        line[:] = [n for n in line if n != '']
    for line in lines:
        line[:] = [int(n) for n in line]

boards = []
for i in range(0, len(lines), 5):
    board = []
    for j in range(i, i + 5):
        board.append(lines[j])
    boards.append(board)

# Part One
def mark_number(num: int, board):
    for row in board:
        for i in range(0, len(row)):
            row[i] = -row[i] - 1 if row[i] == num else row[i]

def check_rows(board) -> bool:  
    for row in board:
        winner = True
        for num in row:
            if num >= 0:
                winner = False
                break
        if winner is True:
            return True
    return False

def check_cols(board) -> bool:
    for col in range(0, len(board)):
        winner = True
        for row in range(0, len(board)):
            if board[row][col] >= 0:
                winner = False
                break
        if winner is True:
            return True
    return False

def check_diagonals(board) -> bool:
    first = True
    for i in range(0, len(board)):
        if board[i][i] >= 0:
            first = False
    second = True
    for i in range(len(board) - 1, -1, -1):
        if board[i][i] >= 0:
            second = False
    return first or second

def winner(board) -> bool:
    return check_rows(board) or check_cols(board) or check_diagonals(board)

def play_bingo(numbers, boards):
    for num in numbers:
        ret = None
        for board in boards:
            mark_number(num, board)
            if winner(board):
                return [board, num]

# bingo_result = play_bingo(numbers, boards)
# winning_board = bingo_result[0]
# winning_number = bingo_result[1]

def winning_score(number, board):
    sum_unmarked = 0
    for line in board:
        sum_unmarked += sum([n for n in line if n > 0])
    return sum_unmarked * number

# print(winning_score(winning_number, winning_board))

# Part Two
def play_bingo_till_end(numbers, boards):
    for num in numbers:
        w = False
        ret = [[], None]
        for board in boards:
            mark_number(num, board)
            if winner(board):
                ret[1] = num
                ret[0].append(board)
                w = True
        if w == True:
            return ret

while len(boards):
    bingo_result = play_bingo_till_end(numbers, boards)
    for b in bingo_result[0]:
        boards.remove(b)
    numbers = numbers[numbers.index(bingo_result[1]) + 1:]

print(winning_score(bingo_result[1], bingo_result[0][0]))