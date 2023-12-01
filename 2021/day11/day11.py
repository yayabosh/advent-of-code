with open('input.txt') as f:
    octopi = [[int(n) for n in line.strip()] for line in f]

# Part One
total_flashes = 0
def flash(r, c):
    global total_flashes
    total_flashes += 1
    octopi[r][c] = -1
    for rr in [r - 1, r, r + 1]:
        for cc in [c - 1, c, c + 1]:
            if 0 <= rr < len(octopi) and 0 <= cc < len(octopi[0]) and octopi[rr][cc] != -1:
                octopi[rr][cc] += 1
                if octopi[rr][cc] == 10:
                    flash(rr, cc)

for i in range(100):
    for r in range(len(octopi)):
        for c in range(len(octopi[0])):
            octopi[r][c] += 1
    for r in range(len(octopi)):
        for c in range(len(octopi[0])):
            if octopi[r][c] >= 10:
                flash(r, c)
    for r in range(len(octopi)):
        for c in range(len(octopi[0])):
            if octopi[r][c] == -1:
                octopi[r][c] = 0

print(total_flashes)

# Part Two
def simultaneous(octopi):
    for i in range(len(octopi)):
        for j in range(len(octopi[0])):
            if octopi[i][j] != 0:
                return False
    return True

step = 0
while not simultaneous(octopi):
    for r in range(len(octopi)):
        for c in range(len(octopi[0])):
            octopi[r][c] += 1
    for r in range(len(octopi)):
        for c in range(len(octopi[0])):
            if octopi[r][c] >= 10:
                flash(r, c)
    for r in range(len(octopi)):
        for c in range(len(octopi[0])):
            if octopi[r][c] == -1:
                octopi[r][c] = 0
    step += 1

print(step)