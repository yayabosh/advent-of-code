import math

with open("./input.txt") as f:
    lines = [line.strip().split() for line in f.readlines()]
    ops = lines.pop()
    lines = [[int(n) for n in line] for line in lines]

# Part One
total = 0
for i, op in enumerate(ops):
    if op == "*":
        res = 1
    else:
        assert op == "+"
        res = 0
    for j in range(len(lines)):
        n = lines[j][i]
        if op == "*":
            res *= n
        else:
            res += n

    total += res

print(total)

# Part Two
with open("./input.txt") as f:
    lines = [line[:-1] for line in f.readlines()]
    ops = lines.pop().split()


column_ends = [len(lines[0])]
c = len(lines[0]) - 1
while c >= 0:
    # check if there's a value in the column
    for r in range(len(lines)):
        if lines[r][c] != " ":
            c -= 1
            break
    else:
        column_ends.insert(0, c)
        c -= 1

matrix = []
for c_i, c_e in enumerate(column_ends):
    transposed = []
    c = c_e - 1
    while c > column_ends[c_i - 1]:
        n = 0
        for i in range(len(lines)):
            if lines[i][c] != " ":
                n *= 10
                n += int(lines[i][c])
        transposed.append(n)
        c -= 1
    matrix.append(transposed)

total = 0
for op, nums in zip(ops, matrix):
    if op == "*":
        res = math.prod(nums)
    else:
        res = sum(nums)
    total += res

print(total)
