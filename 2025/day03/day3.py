with open("./input.txt") as f:
    banks = []
    for line in f.readlines():
        bank = [int(joltage) for joltage in line.strip()]
        banks.append(bank)


# Part One
def max_joltage_pt1(bank):
    # find the max
    max_num = max(bank)
    max_idx = bank.index(max_num)
    if max_idx == len(bank) - 1:
        return 10 * max(bank[:-1]) + max_num
    else:
        return 10 * max_num + max(bank[max_idx + 1 :])


# Part Two
def max_joltage_pt2(bank, digits):
    if digits == 1:
        return max(bank)

    max_digit = bank[0]
    max_idx = 0
    # choose the max digit that leaves digits - 1 remaining digits to choose from
    for i, n in enumerate(bank[: -(digits - 1)]):
        if n > max_digit:
            max_digit = n
            max_idx = i

    return (10 ** (digits - 1) * max_digit) + max_joltage_pt2(
        bank[max_idx + 1 :], digits - 1
    )


sum = 0
for bank in banks:
    # sum += max_joltage_pt1(bank, 2)
    max_j = max_joltage_pt2(bank, 12)
    sum += max_j

print(sum)
