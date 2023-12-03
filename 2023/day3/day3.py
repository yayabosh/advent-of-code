from collections import defaultdict


engine_schematic = []
with open("input.txt") as f:
    for line in f:
        engine_schematic.append(line.strip())


# Part One
# Checks the adjacent cells (including diagonals) to see if there is a symbol
# adjacent to the current cell (which contains a digit). Returns True if a symbol
# is found, otherwise returns False
def check_adjacent_cells(row: int, col: int) -> bool:
    # 🤓 way of checking adjacent cells
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            # Verify the current row is within the bounds of the schematic
            if row + dx < 0 or row + dx >= len(engine_schematic):
                continue
            # Verify the current column is within the bounds of the schematic
            elif col + dy < 0 or col + dy >= len(engine_schematic[row + dx]):
                continue

            char = engine_schematic[row + dx][col + dy]
            # If the character is not a period or a digit, then it is a symbol
            if char != "." and not char.isdigit():
                return True


sum = 0
# Iterate through the schematic and check each line for part numbers
for row, line in enumerate(engine_schematic):
    col = 0
    while col < len(line):
        # If the character is not a digit, then it is not part of a part number and we can skip it
        if not line[col].isdigit():
            col += 1
            continue

        is_valid_part_number = False
        part_number = ""
        while col < len(line) and line[col].isdigit():
            # If we haven't found a symbol adjacent to this part number yet,
            # then we need to keep checking the adjacent cells
            if not is_valid_part_number:
                is_valid_part_number = check_adjacent_cells(row, col)

            # Let's add the current digit to the part number we are building
            part_number += line[col]
            col += 1

        # If we found a valid part number, then we can add it to the sum
        if is_valid_part_number:
            sum += int(part_number)

print(sum)


# Part Two
# Checks the adjacent cells (including diagonals) to see if there is a gear (*)
# adjacent to the current cell (which contains a digit). Returns the coordinates
# of the gear if one is found, otherwise returns (-1, -1)
def check_for_gear(row: int, col: int) -> (int, int):
    # 🤓 way of checking adjacent cells
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            # Verify the current row is within the bounds of the schematic
            if row + dx < 0 or row + dx >= len(engine_schematic):
                continue
            # Verify the current column is within the bounds of the schematic
            elif col + dy < 0 or col + dy >= len(engine_schematic[row + dx]):
                continue

            char = engine_schematic[row + dx][col + dy]
            # If the character is *, then we found a gear
            if char == "*":
                return (row + dx, col + dy)

    return (-1, -1)


# Stores the gear coordinates mapping to a list of part numbers adjacent to the gear
part_nums_adjacent_to_gears = defaultdict(list)

# Iterate through the schematic and check each line for part numbers. If a part number
# is found, then we check the adjacent cells to see if there is a gear. If there is,
# then we put that mf in the map!
for row, line in enumerate(engine_schematic):
    col = 0
    while col < len(line):
        # If the character is not a digit, then it is not part of a part number and we can skip it
        if not line[col].isdigit():
            col += 1
            continue

        # We need to keep track of whether or not we found a gear adjacent to the part number
        is_adjacent_to_gear = False
        # We also need to keep track of the coordinates of the gear
        gear_x, gear_y = -1, -1

        part_number = ""
        while col < len(line) and line[col].isdigit():
            # If we haven't found a gear adjacent to this part number yet,
            # then we need to keep checking the adjacent cells
            if not is_adjacent_to_gear:
                # Get the coordinates (if any) of the gear adjacent to the current cell
                gear_x, gear_y = check_for_gear(row, col)
                # If the coordinates are not (-1, -1), then we found a gear!
                if gear_x != -1 and gear_y != -1:
                    is_adjacent_to_gear = True

            # Let's add the current digit to the part number we are building
            part_number += line[col]
            col += 1

        # If we found a part number next to a gear, then we can put it in the map
        if is_adjacent_to_gear:
            part_nums_adjacent_to_gears[(gear_x, gear_y)].append(int(part_number))

sum = 0
# Iterate through the part numbers next to gears and calculate and sum the gear ratios
for part_numbers in part_nums_adjacent_to_gears.values():
    # If there are not exactly two part numbers adjacent to the gear, then it's not a valid gear
    if len(part_numbers) != 2:
        continue

    gear_ratio = part_numbers[0] * part_numbers[1]
    sum += gear_ratio

print(sum)
