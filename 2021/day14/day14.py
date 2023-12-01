from collections import defaultdict

with open("day14/input.txt") as f:
    polymer = f.readline().strip()
    f.readline()
    insertion_rules = {}
    for line in f:
        line = line.strip().split(" -> ")
        insertion_rules[line[0]] = line[1]
    current = defaultdict(int)
    for i in range(len(polymer) - 1):
        pair = polymer[i : i + 2]
        current[pair] += 1

# for i in range(10): # Part One
for i in range(40):  # Part Two
    next = defaultdict(int)
    for pair, count in current.items():
        next[pair[0] + insertion_rules[pair]] += count
        next[insertion_rules[pair] + pair[1]] += count
    current = next

counts = defaultdict(int)
for pair, count in current.items():
    counts[pair[0]] += count
counts[polymer[-1]] += 1

sort = sorted([count for element, count in counts.items()])
print(sort[-1] - sort[0])
