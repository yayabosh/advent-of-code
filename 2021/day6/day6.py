with open('input.txt') as f: fishies = [int(timer) for timer in f.read().split(',')]

# Part One
map = {}
for i in range(0, 9): map[i] = 0
for fish in fishies: map[fish] += 1

def simulate(days) -> int:
    while days > 0:
        zeroes = map[0]
        for i in range(1, 9):
            map[i - 1] += map[i]
            map[i] = 0
        if zeroes:
            map[0] -= zeroes
            map[6] += zeroes
            map[8] += zeroes
        days -= 1
    return sum(map.values())

print(simulate(80))

# Part Two
print(simulate(256))