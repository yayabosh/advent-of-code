from collections import defaultdict

cards = []
with open("input.txt") as f:
    for line in f:
        # Get rid of the "Card #: " part of each line
        line = line[line.index(": ") + 1 :]

        # Split the line into the winning numbers (everything before the "|") and
        # the numbers you have (everything after the "|")
        winning, yours = line.split(" | ")

        # Split the winning numbers and your numbers into sets of numbers (split
        # on the space between each number)
        winning = set(int(x) for x in winning.split())
        yours = set(int(x) for x in yours.split())

        # Add the number of matches between the winning numbers and your numbers
        # Python is COOL 😎
        cards.append(len(winning & yours))


# Part One
# For each card, we want to add 2^(X - 1) to the total points, where X is the
# number of matches. Obviously, if X == 0, then we don't want to add anything.
total_points = sum(2 ** (num_matches - 1) for num_matches in cards if num_matches)
print(total_points)


# Part Two
# Will store the number of copies of each card
num_copies = defaultdict(int)
for card, num_matches in enumerate(cards):
    # Add one copy for the original card
    num_copies[card] += 1
    # The current card has X matches, and C copies. For each of the C copies,
    # we want to add 1 copy to the next X cards. In other words, we can add
    # C copies to the next X cards.
    # In this case, X = num_matches and C = num_copies[card].
    for i in range(1, num_matches + 1):
        num_copies[card + i] += num_copies[card]

print(sum(num_copies.values()))
