with open("./input.txt") as f:
    # Lop off the "Game #: " part of each line (by splitting on : and taking the second part)
    lines = [line.split(":")[1].strip() for line in f]


# Part One

# Process the games, game by game.
games = []
for i, line in enumerate(lines):
    # Stores the draws of red, green, blue cubes the elf draws in each draw of this game
    game = []

    # Split on semicolons for each draw of cubes the elf gets when he reaches into the bag
    draws = line.split(";")
    # Process each time the elf draws cubes from the bag
    for d in draws:
        # Stores the number of red, green, blue cubes the elf draws in this draw
        draw = [0] * 3

        # Split on commas for the number of each cube the elf pulls out of the bag (red, green, blue)
        cubes = d.split(",")

        # Process each number of cubes the elf draws from the bag
        for cube in cubes:
            cube = cube.strip()
            num_cubes = int(cube[:cube.index(" ")])
            color = cube[cube.index(" ") + 1:]

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
    game_id = i + 1
    impossible = False
    for draw in game:
        # Verify the number of red, green, and blue cubes is valid 
        if draw[0] > 12 or draw[1] > 13 or draw[2] > 14:
            impossible = True
            break
    
    if impossible:
        continue
    
    sum += game_id
    

print(sum)