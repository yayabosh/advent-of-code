with open('input.txt') as f:
    lines = [line.split() for line in f]

# Part One
position, depth = 0, 0
for line in lines:
    if line[0] == 'forward':
        position += int(line[1])
    elif line[0] == 'down':
        depth += int(line[1])
    else:
        depth -= int(line[1])

print(position * depth)

# Part Twot
position, depth, aim = 0, 0, 0
for line in lines:
    if line[0] == 'forward':
        position += int(line[1])
        depth += aim * int(line[1])
    elif line[0] == 'down':
        aim += int(line[1])
    else:
        aim -= int(line[1])

print(position * depth)