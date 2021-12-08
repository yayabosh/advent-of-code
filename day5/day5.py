with open('input.txt') as f:
    lines = []
    for line in f:
        split = line.strip().split(' -> ')
        lines.append([split[0].split(','), split[1].split(',')])
    for line in lines:
        for point in line: point[:] = [int(n) for n in point]

# Part One
horizontal_vertical = list(filter(lambda line: line[0][0] == line[1][0] or line[0][1] == line[1][1], lines.copy()))

def create_grid(lines):
    width, height = 0, 0
    for line in lines:
        for point in line:
            width = point[0] if point[0] > width else width
            height = point[1] if point[1] > height else height
    return [[0 for x in range(width + 1)] for y in range(height + 1)]

cartesian = create_grid(horizontal_vertical) # Part One
cartesian = create_grid(lines)               # Part Two

def fill_column(start, end) -> None:
    for i in range(start[1], end[1] + 1): cartesian[i][start[0]] += 1

def fill_row(start, end) -> None:
    for i in range(start[0], end[0] + 1): cartesian[start[1]][i] += 1

def mark_horizontals_verticals() -> None:
    for line in horizontal_vertical:
        if line[0][0] == line[1][0]:
            min = line[0] if line[0][1] <= line[1][1] else line[1]
            max = line[0] if line[0][1] > line[1][1] else line[1]
            fill_column(min, max)
        else:
            min = line[0] if line[0][0] <= line[1][0] else line[1]
            max = line[0] if line[0][0] > line[1][0] else line[1]
            fill_row(min, max)

def count_dangerous() -> int:
    count = 0
    for row in cartesian:
        for col in row: count += 1 if col > 1 else 0
    return count

mark_horizontals_verticals()
print(count_dangerous())

# Part Two
def fill_top_right(start, delta_x) -> None:
    for i in range(0, delta_x + 1): cartesian[start[1] - i][start[0] + i] += 1

def fill_bottom_right(start, delta_x) -> None:
    for i in range(0, delta_x + 1): cartesian[start[1] + i][start[0] + i] += 1

def fill_bottom_left(start, delta_x) -> None:
    for i in range(0, delta_x + 1): cartesian[start[1] + i][start[0] - i] += 1

def fill_top_left(start, delta_x) -> None:
    for i in range(0, delta_x + 1): cartesian[start[1] - i][start[0] - i] += 1

def mark_lines() -> None:
    for line in lines:
        if line[0][0] == line[1][0]:
            min = line[0] if line[0][1] <= line[1][1] else line[1]
            max = line[0] if line[0][1] > line[1][1] else line[1]
            fill_column(min, max)
        elif line[0][1] == line[1][1]:
            min = line[0] if line[0][0] <= line[1][0] else line[1]
            max = line[0] if line[0][0] > line[1][0] else line[1]
            fill_row(min, max)
        else:
            delta_x = line[1][0] - line[0][0]
            delta_y = line[1][1] - line[0][1]
            if delta_x >= 0:
                if delta_y >= 0: fill_bottom_right(line[0], delta_x)
                else: fill_top_right(line[0], delta_x)
            else:
                if delta_y >= 0: fill_bottom_left(line[0], abs(delta_x))
                else: fill_top_left(line[0], abs(delta_x))

mark_lines()
print(count_dangerous())