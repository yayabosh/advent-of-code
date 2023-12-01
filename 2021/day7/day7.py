import statistics, math

with open("input.txt") as f:
    crabs = [int(n) for n in f.read().split(",")]

# Part One
median = statistics.median(crabs)
cost = sum([abs(crab - median) for crab in crabs])
print(cost)


# Part Two
def fuel(steps):
    return steps * (steps + 1) / 2


def cost(avg):
    return sum([fuel(abs(crab - avg)) for crab in crabs])


mean = statistics.mean(crabs)
cost = min(cost(math.floor(mean)), cost(math.ceil(mean)))
print(cost)
