from collections import Counter

with open("./input.txt") as f:
    lines = [line.strip() for line in f]

    list1 = []
    list2 = []
    for line in lines:
        num1, num2 = line.split()
        list1.append(int(num1))
        list2.append(int(num2))

# Part One
list1 = sorted(list1)
list2 = sorted(list2)

total = 0
for num1, num2 in zip(list1, list2):
    diff = abs(num1 - num2)
    total += diff

print(total)

# Part Two
list2_counter = Counter(list2)

total_similarity_score = 0
for num in list1:
    list2_count = list2_counter[num]
    similarity_score = num * list2_count
    total_similarity_score += similarity_score

print(total_similarity_score)