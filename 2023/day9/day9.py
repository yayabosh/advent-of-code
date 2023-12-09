# Part One
with open("input.txt") as f:
    histories = []
    for line in f:
        history = [int(n) for n in line.split()]
        histories.append(history)


def extrapolate_value(history: list[str]) -> int:
    # First we need to get all sequences of differences until all differences
    # are 0. We will do this by iterating over the history, and comparing each
    # adjacent pair of numbers and calculating their difference. If the
    # differences are all 0, we are done. Otherwise, we will repeat the
    # process with the new list of differences. But we still need to keep track
    # of all the lists of differences we have seen so far, so we will use a
    # list of lists.
    differences = [history]
    current_differences = history
    while not all(difference == 0 for difference in current_differences):
        new_differences = []
        # Iterate over the current differences and calculate the difference
        # between each pair of adjacent numbers
        for i in range(len(current_differences) - 1):
            # Not sure if this should be absolute difference or not
            diff = current_differences[i + 1] - current_differences[i]
            new_differences.append(diff)

        # Keep track of all the differences we have seen so far
        differences.append(new_differences)

        # Update the current differences
        current_differences = new_differences

    # Now that we have all sequences of differences, we need to "extrapolate"
    # to find the next number in the sequence. We will do this by summing the
    # last numbers in each sequence of differences
    last_value = sum(difference[-1] for difference in differences)

    # Part Two
    # We also want to "backwards extrapolate" to find the first number in the
    # sequence. We will start with the last value (0) and then successively
    # subtract the current value from the first number in the previous sequence
    # of differences. At the end, we will have (what should be) the first number
    # in the first sequence of differences.
    first_value = 0
    for difference in reversed(differences):
        first_value = difference[0] - first_value

    return first_value, last_value


first_values = 0
last_values = 0
for history in histories:
    first_value, last_value = extrapolate_value(history)
    # Part One
    last_values += last_value
    # Part Two
    first_values += first_value

# Part One
print(last_values)

# Part Two
print(first_values)
