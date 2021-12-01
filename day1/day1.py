with open('input.txt') as f:
    lines = [int(line) for line in f]

# Part One
increases = 0
for i in range(1, len(lines)):
    if lines[i] > lines[i - 1]:
        increases += 1

print(increases)

# Part Two
increases = 0
for i in range(3, len(lines)):
    if lines[i - 3] < lines[i]:
        increases += 1

print(increases)