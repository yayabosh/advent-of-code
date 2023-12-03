engine_schematic = []
with open("input.txt") as f:
    for line in f:
        engine_schematic.append(line.strip())


# Part One


# Checks the adjacent cells (including diagonals) to see if there is a symbol
# adjacent to the current cell (which contains a digit in a number)
def check_adjacent_cells(row: int, col: int) -> bool:
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
    # Iterate through each character in the line.
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
            # Move to the next character in the line
            col += 1

        # If we found a valid part number, then we can add it to the sum
        if is_valid_part_number:
            sum += int(part_number)

print(sum)
