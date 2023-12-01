with open("input.txt") as f:
    entries = []
    for entry in f:
        entry = entry.split("|")
        for i in range(0, 2):
            entry[i] = entry[i].strip()
        entries.append(entry)

# Part One
# values: number of segments needed to display corresponding key
segments = {2: 1, 4: 4, 3: 7, 7: 8}
counts = {1: 0, 4: 0, 7: 0, 8: 0}

for entry in entries:
    output = entry[1].split()
    for combination in output:
        if len(combination) in segments:
            counts[segments[len(combination)]] += 1

print(sum(counts.values()))
