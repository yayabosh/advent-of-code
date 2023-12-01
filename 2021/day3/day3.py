with open("input.txt") as f:
    lines = [line.strip() for line in f]


# Part One
# Returns a tuple of strings [gamma rate, epsilon rate] where each rate is represented in binary (base 2).
def rates(nums):
    gamma_rate, epsilon_rate = "", ""
    for i in range(0, len(nums[0])):
        zero_count = 0
        for num in nums:
            zero_count += 1 if num[i] == "0" else 0
        one_count = len(nums) - zero_count

        gamma_rate += "1" if one_count >= zero_count else "0"
        epsilon_rate += "1" if one_count < zero_count else "0"

    return [gamma_rate, epsilon_rate]


r = rates(lines)
print("power consumption: " + str(int(r[0], 2) * int(r[1], 2)))

# Part Two
nums = lines.copy()
digit = 0
while len(nums) > 1:
    most_common = rates(nums)[0]
    nums[:] = [n for n in nums if n[digit] == most_common[digit]]
    digit += 1

oxygen_generator_rating = nums[0]

nums = lines.copy()
digit = 0
while len(nums) > 1:
    least_common = rates(nums)[1]
    nums[:] = [n for n in nums if n[digit] == least_common[digit]]
    digit += 1

co2_scrubber_rating = nums[0]

print(
    "life support rating: "
    + str(int(oxygen_generator_rating, 2) * int(co2_scrubber_rating, 2))
)
