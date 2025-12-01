with open("./input.txt") as f:
    lines = [line.strip() for line in f.readlines()]

# Part One
rotations = [int(line[1:]) * (1 if line[0] == 'R' else -1) for line in lines]
pw = 0
dial = 50
for r in rotations:
    dial += r    # rotate
    dial %= 100  # adjust
    if dial == 0:
        pw += 1

print(pw)

# Part Two
pw = 0
dial = 50
for r in rotations:
    if r > 0:
        if dial + r >= 100:
            pw += (dial + r) // 100
    elif dial != 0:
        if dial + r <= 0:
            pw += 1 + abs(dial + r) // 100
    elif r <= -100:
        pw += abs(r) // 100
    dial += r
    dial %= 100

print(pw)