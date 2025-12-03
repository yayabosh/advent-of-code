from collections import defaultdict
from math import ceil, floor, sqrt

with open("./input.txt") as f:
    ranges = f.readline().split(",")
    ranges = [r.split("-") for r in ranges]
    ranges = [(int(a[0]), int(a[1])) for a in ranges]


# Part One
def check_pt1(r):
    sum = 0
    st, end = r
    st = str(st)
    leng = ceil(len(st) / 2)
    n = 10 ** (leng - 1)
    dup = int(str(n) + str(n))
    while dup <= end:
        s = str(n)
        dup = int(s + s)
        if dup < int(st) or end < dup:  # is the num out of the range?
            n += 1
            continue
        sum += dup
        n += 1
    return sum

# Part Two
factors = defaultdict(set)
for n in range(1, 16):
    for j in range(1, floor(sqrt(n)) + 1):
        if n % j == 0:
            factors[n].add(j)
            if j != 1:  # don't add n as a factor of n
                factors[n].add(n // j)

def sum_nums_of_length(factor: int, length: int, st, end, visited):
    sum = 0
    for n in range(10 ** (factor - 1), 10 ** factor):  # keep fixed num of digits
        seq = int(str(n) * (length // factor))  # make a seq of length length with repeated digits
        if seq > end:
            break
        if st <= seq <= end and seq not in visited:
            visited.add(seq)
            sum += seq
    return sum

def check_pt2(r):
    sum = 0
    st, end = r
    visited = set()
    for leng in range(len(str(st)), len(str(end)) + 1):
        for f in factors[leng]:
            sum += sum_nums_of_length(f, leng, st, end, visited)
    return sum

sum = 0
for r in ranges:
    # s = check_pt1(r)
    s = check_pt2(r)
    sum += s

print(sum)
