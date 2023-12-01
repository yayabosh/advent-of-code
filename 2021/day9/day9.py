import math

with open('input.txt') as f:
    heightmap = [[int(n) for n in line.strip()] for line in f]
    heightmap.insert(0, [10] * len(heightmap[0]))
    for line in heightmap:
        line.insert(0, 10)
        line.append(10)
    heightmap.append([10] * len(heightmap[0]))

# Part One
low_points = []
for i in range(1, len(heightmap) - 1):
    for j in range(1, len(heightmap[i]) - 1):
        above = heightmap[i - 1][j]
        below = heightmap[i + 1][j]
        left = heightmap[i][j - 1]
        right = heightmap[i][j + 1]
        if heightmap[i][j] < above and heightmap[i][j] < below and heightmap[i][j] < left and heightmap[i][j] < right:
            low_points.append([heightmap[i][j], i, j])

print(sum([1 + n[0] for n in low_points]))

# Part Two
def basin_size(i, j, prev):
    if i == 0 or i == len(heightmap) - 1 or j ==  0 or j == len(heightmap[0]) - 1:
        return 0
    elif heightmap[i][j] == 9 or heightmap[i][j] < 0:
        return 0
    elif heightmap[i][j] < prev:
        return 0
    prev = heightmap[i][j]
    heightmap[i][j] = -heightmap[i][j] - 1
    return 1 + basin_size(i - 1, j, prev) + basin_size(i + 1, j, prev) + basin_size(i, j - 1, prev) + basin_size(i, j + 1, prev)

basin_sizes = [basin_size(point[1], point[2], -1) for point in low_points]
print(math.prod(sorted(basin_sizes)[-3:]))