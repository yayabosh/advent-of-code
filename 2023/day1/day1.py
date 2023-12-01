with open("./input.txt") as f:
    lines = [line.strip() for line in f]

# Part One
sum = 0
for line in lines:
    first = last = None
    # Indices of the first and last digits in the line
    f, l = 0, len(line) - 1

    # Find the first and last digits in the line
    while f < len(line) and l >= 0 and (not first or not last):
        if not first and line[f].isnumeric():
            first = int(line[f])

        if not last and line[l].isnumeric():
            last = int(line[l])

        f += 1
        l -= 1

    num = 10 * first + last
    sum += num

print(sum)

# Part Two
digits = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


# Finds the first digit in the line, numeric or spelled out
def find_first_digit(line):
    first_digit, first_idx = None, len(line)

    # First try to find the first digit spelled out
    for digit in digits:
        idx = line.find(digit)
        # If we found the digit in the line, and it's before the current first digit
        # we found so far (if any), update the first digit and its index
        if 0 <= idx < first_idx:
            first_idx, first_digit = idx, digits[digit]

    # Check if there's a numeric digit before the first spelled out digit
    for i in range(first_idx):
        if line[i].isdigit():
            return int(line[i])

    return first_digit


# Finds the last digit in the line, numeric or spelled out
def find_last_digit(line):
    last_digit, last_idx = None, -1

    # First try to find the last digit spelled out
    for digit in digits:
        idx = line.rfind(digit)
        # If we found the digit in the line, and it's after the current last digit
        # we found so far (if any), update the last digit and its index
        if last_idx < idx:
            last_idx, last_digit = idx, digits[digit]

    # Check if there's a numeric digit after the last spelled out digit
    for i in reversed(range(last_idx, len(line))):
        if line[i].isdigit():
            return int(line[i])

    return last_digit


sum = 0
for line in lines:
    first = find_first_digit(line)
    last = find_last_digit(line)

    num = 10 * first + last
    sum += num

print(sum)
