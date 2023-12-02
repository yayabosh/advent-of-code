with open("./small.txt") as f:
    # Lop off the "Game #: " part of each line (by splitting on : and taking the second part)
    lines = [line.split(":")[1].strip() for line in f]


# Part One

# Process the games, game by game.
games = []
for i, line in enumerate(lines):
    # Stores the draws of red, green, blue cubes the elf draws in each draw of this game
    # They'll be stored as 3-element lists in each list
    game = []

    # Split on semicolons for each draw of cubes the elf gets when he reaches into the bag
    draws = line.split("; ")

    # Process each time the elf draws cubes from the bag
    for d in draws:
        # Stores the number of [red, green, blue] cubes the elf draws in this draw
        draw = [0] * 3

        # Split on commas for the number of each cube the elf pulls out of the bag [red, green, blue]
        cubes = d.split(", ")

        # Process each number of cubes the elf draws from the bag
        for cube in cubes:
            # The number of cubes the elf draws
            num_cubes = int(cube[: cube.index(" ")])
            # The color of the cubes the elf draws
            color = cube[cube.index(" ") + 1 :]

            # Update the number of cubes of this color the elf draws
            if color == "red":
                draw[0] = num_cubes
            elif color == "green":
                draw[1] = num_cubes
            elif color == "blue":
                draw[2] = num_cubes

        # Add this draw to the game. Should look something like [1, 2, 3]
        game.append(draw)

    # Add this game to the list of games
    games.append(game)


# Iterate through each game, and for each game, iterate through each draw of cubes the elf gets
# For each draw, we want to check and make sure the game would have been possible if
# the bag contained only 12 red cubes, 13 green cubes, and 14 blue cubes.
sum = 0
for i, game in enumerate(games):
    # The game ID is just the index of the game in the list + 1 (cuz 1-indexing)
    game_id = i + 1
    # Assume the game is possible until we find a draw that makes it impossible
    impossible = False
    for draw in game:
        # Verify the number of red, green, and blue cubes is valid
        if draw[0] > 12 or draw[1] > 13 or draw[2] > 14:
            # If not, the game is impossible, so we can just exit
            impossible = True
            break

    # If the game is possible, add the game ID to the sum
    if not impossible:
        sum += game_id


print(sum)

# Part Two

# Process the games, game by game.
games = []
for i, line in enumerate(lines):
    # Stores the fewest number of red, green, blue cubes needed for this game to be possible
    # That is, it stores the maximum number of cubes the elf draws across all draws in this game.
    # Bad variable naming but whatever
    game = [0] * 3

    # Split on semicolons for each draw of cubes the elf gets when he reaches into the bag
    draws = line.split("; ")
    # Process each time the elf draws cubes from the bag
    for d in draws:
        # Split on commas for the number of each cube the elf pulls out of the bag (red, green, blue)
        cubes = d.split(", ")

        # Process each number of cubes the elf draws from the bag
        for cube in cubes:
            # The number of cubes the elf draws
            num_cubes = int(cube[: cube.index(" ")])
            # The color of the cubes the elf draws
            color = cube[cube.index(" ") + 1 :]

            # Update the fewest number of cubes needed for this game to be possible.
            # It's just the maximum between what we currently have and what we just drew.
            if color == "red":
                game[0] = max(game[0], num_cubes)
            elif color == "green":
                game[1] = max(game[1], num_cubes)
            elif color == "blue":
                game[2] = max(game[2], num_cubes)

        # Add this draw to the game. Should look something like [1, 2, 3]
        game.append(game)

    # Add this game to the list of games
    games.append(game)


# Iterate through each game, and for each game, calculate the power of the game.
# The power of a game is the product of the fewest number of red, green, and blue cubes needed
sum = 0
for i, game in enumerate(games):
    power = game[0] * game[1] * game[2]
    sum += power

print(sum)
