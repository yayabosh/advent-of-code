with open("input.txt") as f:
    lines = [int(line) for line in f]

# Part One
increases = 0
for i in range(1, len(lines)):
    increases += 1 if lines[i] > lines[i - 1] else 0

print(increases)

# Part Two
increases = 0
for i in range(3, len(lines)):
    increases += 1 if lines[i] > lines[i - 3] else 0

print(increases)
