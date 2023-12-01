with open("day10/input.txt") as f:
    lines = [line.strip() for line in f]

# Part One
table = {")": 3, "]": 57, "}": 1197, ">": 25137}
matching_chars = {"(": ")", "[": "]", "{": "}", "<": ">"}


def corrupted(line):
    stack = []
    for c in line:
        if c in matching_chars:
            stack.append(matching_chars[c])
        else:
            top = stack.pop()
            if top != c:
                return c
    return None


illegal_chars = []
for line in lines:
    char = corrupted(line)
    if char is not None:
        illegal_chars.append(char)

print(sum([table[char] for char in illegal_chars]))

# Part Two
table = {")": 1, "]": 2, "}": 3, ">": 4}


def ignored(line):
    stack = []
    for c in line:
        if c in matching_chars:
            stack.append(matching_chars[c])
        else:
            top = stack.pop()
            if top != c:
                return None
    return stack


sequences = []
for line in lines:
    sequence = ignored(line)
    if sequence is not None:
        sequences.append("".join(sequence[::-1]))

total_scores = []
for sequence in sequences:
    score = 0
    for c in sequence:
        score = 5 * score + table[c]
    total_scores.append(score)

middle_score = sorted(total_scores)[len(total_scores) // 2]
print(middle_score)
