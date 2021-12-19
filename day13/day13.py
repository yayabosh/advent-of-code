with open('day13/fold_instructions.txt') as f:
    folds = []
    for line in f:
        fold = line.strip().split()[2].split('=')
        folds.append([fold[0], int(fold[1])])

with open('day13/dots.txt') as f:
    dots = [[int(coordinate) for coordinate in line.split(',')] for line in f]

def create_paper(dots):
    width, height = 0, 0
    for coordinate in dots:
        width = max(coordinate[0], width)
        height = max(coordinate[1], height)
    paper = [[0 for x in range(width + 1)] for y in range(height + 1)]
    for dot in dots:
        paper[dot[1]][dot[0]] += 1
    return paper

paper = create_paper(dots)

# Part One
def fold_up(paper, line):
    for i in range(line + 1, len(paper)):
        for j in range(len(paper[i])):
            paper[line - (i - line)][j] += paper[i][j]
    return paper[:line]

def fold_left(paper, line):
    for i in range(len(paper)):
        for j in range(line + 1, len(paper[i])):
            paper[i][line - (j - line)] += paper[i][j]
    for a in paper:
        a[:] = a[:line]
    return paper

def count_dots(paper):
    count = 0
    for a in paper:
        count += len([n for n in a if n != 0])
    return count

first_fold = fold_left(paper, folds[0][1])
print(count_dots(first_fold))

# Part Two
for fold in folds:
    if fold[0] == 'x':
        paper = fold_left(paper, fold[1])
    else:
        paper = fold_up(paper, fold[1])

for i in range(len(paper)):
    for j, n in enumerate(paper[i]):
        if paper[i][j] > 0:
            print('#', end='')
        else:
            print(' ', end='')
    print()