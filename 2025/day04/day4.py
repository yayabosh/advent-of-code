with open("./input.txt") as f:
    grid = [[roll for roll in rolls.strip()] for rolls in f.readlines()]


# Part One
accessible_rolls = 0


def surrounding_rolls(i, j):
    surrounding_rolls = []
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue
            if not (0 <= i + dx < len(grid) and 0 <= j + dy < len(grid[0])):
                continue
            if grid[i + dx][j + dy] == "@":
                surrounding_rolls.append((i + dx, j + dy))
    return surrounding_rolls


accessible_rolls = 0
q = []
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == "@" and len(surrounding_rolls(i, j)) < 4:
            accessible_rolls += 1

print(accessible_rolls)


# Part Two
accessible_rolls = 0
q = []
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == "@" and len(surrounding_rolls(i, j)) < 4:
            q.append((i, j))

while q:
    length = len(q)
    for r in range(length):
        i, j = q.pop()
        if grid[i][j] == ".":
            continue
        neighbors = surrounding_rolls(i, j)
        if len(neighbors) < 4:
            accessible_rolls += 1
            grid[i][j] = "."
            q.extend(neighbors)

print(accessible_rolls)
