with open("./input.txt") as f:
    ranges_text, ids_text = f.read().strip().split("\n\n")
    ranges = []
    for line in ranges_text.splitlines():
        a, b = line.split("-")
        a, b = int(a), int(b)
        ranges.append([a, b] if a <= b else [b, a])  # sort asc
    ids = [int(x) for x in ids_text.splitlines()]


# Part One
def merge_overlapping_ranges(ranges):
    if not ranges:
        return ranges

    ranges.sort(key=lambda x: x[0])
    res = [ranges[0]]

    for i in range(1, len(ranges)):
        last = res[-1]
        curr = ranges[i]

        if curr[0] <= last[1]:
            last[1] = max(curr[1], last[1])
        else:
            res.append(curr)

    return res


ranges = merge_overlapping_ranges(ranges)


def search(id: int) -> int:
    """binary search ranges for id"""
    left, right = 0, len(ranges) - 1
    while left <= right:
        mid = (left + right) // 2
        if ranges[mid][0] < ranges[mid][1]:
            return True
        if id < ranges[mid][0]:
            right = mid - 1
        elif id > ranges[mid][1]:
            left = mid + 1
    return False


count = 0
for id in ids:
    if search(id):  # in or out?
        count += 1

print(count)

# Part Two
# sum the non-overlapping ranges
count_all_ranges = sum(r[1] - r[0] + 1 for r in ranges)
print(count_all_ranges)
