from itertools import combinations

with open("input.txt") as f:
    lines = [line.strip() for line in f]

# Find all horizontal lines in f that only contain "." (no "#"s).
horizontal_indices = set(
    i for i, line in enumerate(lines) if all(pixel == "." for pixel in line.strip())
)

# Find all vertical lines in f that only contain "." (no "#"s). We essentially
# want to transpose f and then find all horizontal lines that only contain "."
# (no "#"s).

# Crazy list comprehension. *lines unpacks each line into a list of lines.
# zip(*lines) then takes each line, and puts the first character of each line into
# a list, then the second character of each line into a list, etc. This is
# essentially transposing f (first characters of all horizontal lines is
# the first vertical line, etc.)
vertical_indices = set(
    i for i, ln in enumerate(zip(*lines)) if all(pixel == "." for pixel in ln)
)


# lines is in the format of a 2D array where "." is empty space and "#" is a
# galaxy. We want to find the shortest path between each pair of galaxies.


# Returns the distance between two points (x1, y1) and (x2, y2). This
# is the sum of the absolute values of the differences between the x and y
# coordinates. However, we also take a parameter expansion, which is how many times
# the rows or columns with only "."s are expanded by. If the path between the
# two points crosses over any line in the horizontal or vertical indices, then
# actually, we want to add expansion - 1 (since the path will be expanded by
# expansion, but we don't want to count the original path).
def shortest_path_distance(r1, c1, r2, c2, expansion):
    distance = abs(r1 - r2) + abs(c1 - c2)
    for r in horizontal_indices:
        if min(r1, r2) <= r <= max(r1, r2):
            print(f"crossed horizontal line at {r}")
            distance += expansion - 1
    for c in vertical_indices:
        if min(c1, c2) <= c <= max(c1, c2):
            print(f"crossed vertical line at {c}")
            distance += expansion - 1

    return distance


# Find all galaxies. A galaxy is a point in lines that is a "#".
galaxies = [
    (r, c)
    for r, line in enumerate(lines)
    for c, pixel in enumerate(line)
    if pixel == "#"
]

# Find the shortest path between each pair of galaxies.
shortest_paths = {}
for (r1, c1), (r2, c2) in combinations(galaxies, 2):
    # Part One
    shortest_paths[(r1, c1, r2, c2)] = shortest_path_distance(
        r1, c1, r2, c2, expansion=2
    )
    # Part Two
    shortest_paths[(r1, c1, r2, c2)] = shortest_path_distance(
        r1, c1, r2, c2, expansion=1000000
    )


print(sum(shortest_paths.values()))
