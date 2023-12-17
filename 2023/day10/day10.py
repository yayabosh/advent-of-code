with open("small_complex_2.txt") as f:
    pipes = [[pipe for pipe in line.strip()] for line in f]


# Find the starting position (the position marked "S")
for row in range(len(pipes)):
    for col in range(len(pipes[row])):
        if pipes[row][col] == "S":
            starting_position = (row, col)
            break

# | is a vertical pipe connecting north and south.
# - is a horizontal pipe connecting east and west.
# L is a 90-degree bend connecting north and east.
# J is a 90-degree bend connecting north and west.
# 7 is a 90-degree bend connecting south and west.
# F is a 90-degree bend connecting south and east.
# . is ground; there is no pipe in this tile.
# S is the starting position of the animal; there is a pipe on this tile, but your sketch doesn't show what shape the pipe has.

NUM_ROWS = len(pipes)
NUM_COLS = len(pipes[0])

ACCEPTS_NORTH = set(["|", "7", "F"])
ACCEPTS_SOUTH = set(["|", "L", "J"])
ACCEPTS_EAST = set(["-", "J", "7"])
ACCEPTS_WEST = set(["-", "L", "F"])


# Return how many steps along the loop does it take to get from the starting position to
# the point farthest from the starting position.
def bfs(grid: list[list[str]], starting_position: (int, int)) -> int:
    # We want to run BFS on the grid, starting at the starting position.
    # At each level, we will enqueue positions we can reach from the current position.
    # We will also keep track of the number of steps we have taken to reach the current position.
    num_steps = 0

    # We will use a queue to keep track of the positions we need to visit.
    queue = [starting_position]

    # We will use a set of (row, col) to keep track of the positions we have
    # already visited.
    visited = set()

    while queue:
        to_visit = len(queue)
        for _ in range(to_visit):
            # Get the next position to explore from the queue.
            row, col = queue.pop(0)

            # If we have already visited this position, skip it.
            if (row, col) in visited:
                continue

            # Mark the current position as visited.
            visited.add((row, col))

            # Explore the neighbors. We have a lot of cases.
            match grid[row][col]:
                # If we are at a vertical pipe, we can go north or south.
                case "|":
                    # Check the north neighbor. If it can accept northward exploration, enqueue it.
                    if row - 1 >= 0 and grid[row - 1][col] in ACCEPTS_NORTH:
                        queue.append((row - 1, col))

                    # Check the south neighbor. If it can accept southward exploration, enqueue it.
                    if row + 1 < NUM_ROWS and grid[row + 1][col] in ACCEPTS_SOUTH:
                        queue.append((row + 1, col))

                # If we are at a horizontal pipe, we can go east or west.
                case "-":
                    # Check the east neighbor. If it can accept eastward exploration, enqueue it.
                    if col + 1 < NUM_COLS and grid[row][col + 1] in ACCEPTS_EAST:
                        queue.append((row, col + 1))

                    # Check the west neighbor. If it can accept westward exploration, enqueue it.
                    if col - 1 >= 0 and grid[row][col - 1] in ACCEPTS_WEST:
                        queue.append((row, col - 1))

                # If we are at L, a 90-degree bend connecting north and east, we can go north or east.
                case "L":
                    # Check the north neighbor. If it can accept northward exploration, enqueue it.
                    if row - 1 >= 0 and grid[row - 1][col] in ACCEPTS_NORTH:
                        queue.append((row - 1, col))

                    # Check the east neighbor. If it can accept eastward exploration, enqueue it.
                    if col + 1 < NUM_COLS and grid[row][col + 1] in ACCEPTS_EAST:
                        queue.append((row, col + 1))

                # If we are at J, a 90-degree bend connecting north and west, we can go north or west.
                case "J":
                    # Check the north neighbor. If it can accept northward exploration, enqueue it.
                    if row - 1 >= 0 and grid[row - 1][col] in ACCEPTS_NORTH:
                        queue.append((row - 1, col))

                    # Check the west neighbor. If it can accept westward exploration, enqueue it.
                    if col - 1 >= 0 and grid[row][col - 1] in ACCEPTS_WEST:
                        queue.append((row, col - 1))

                # If we are at 7, a 90-degree bend connecting south and west, we can go south or west.
                case "7":
                    # Check the south neighbor. If it can accept southward exploration, enqueue it.
                    if row + 1 < NUM_ROWS and grid[row + 1][col] in ACCEPTS_SOUTH:
                        queue.append((row + 1, col))

                    # Check the west neighbor. If it can accept westward exploration, enqueue it.
                    if col - 1 >= 0 and grid[row][col - 1] in ACCEPTS_WEST:
                        queue.append((row, col - 1))

                # If we are at F, a 90-degree bend connecting south and east, we can go south or east.
                case "F":
                    # Check the south neighbor. If it can accept southward exploration, enqueue it.
                    if row + 1 < NUM_ROWS and grid[row + 1][col] in ACCEPTS_SOUTH:
                        queue.append((row + 1, col))

                    # Check the east neighbor. If it can accept eastward exploration, enqueue it.
                    if col + 1 < NUM_COLS and grid[row][col + 1] in ACCEPTS_EAST:
                        queue.append((row, col + 1))

                # If we are at S, the starting position, we can go north, south, east, or west.
                case "S":
                    # Check the north neighbor. If it can accept northward exploration, enqueue it.
                    if row - 1 >= 0 and grid[row - 1][col] in ACCEPTS_NORTH:
                        queue.append((row - 1, col))

                    # Check the south neighbor. If it can accept southward exploration, enqueue it.
                    if row + 1 < NUM_ROWS and grid[row + 1][col] in ACCEPTS_SOUTH:
                        queue.append((row + 1, col))

                    # Check the east neighbor. If it can accept eastward exploration, enqueue it.
                    if col + 1 < NUM_COLS and grid[row][col + 1] in ACCEPTS_EAST:
                        queue.append((row, col + 1))

                    # Check the west neighbor. If it can accept westward exploration, enqueue it.
                    if col - 1 >= 0 and grid[row][col - 1] in ACCEPTS_WEST:
                        queue.append((row, col - 1))

                # If we are at ., the ground, we cannot go anywhere.
                case ".":
                    pass

                # If we are at any other character, we cannot go anywhere.
                case _:
                    pass

        # Increment the number of steps we have taken.
        if queue:
            num_steps += 1

    # Return the number of steps we have taken.
    return num_steps


# Part One
# We subtract one to account for the fact that we don't want to count the extra BFS
# step after we enqueued the farthest position.
num_steps_to_farthest_position = bfs(pipes, starting_position) - 1
# print(num_steps_to_farthest_position)

# Part Two
# We want to find all the tiles that are enclosed by the loop.
# We will start on the edges, and "invalidate" each of those positions. This is
# because they cannot possibly be enclosed because they are on the edge (not fully
# enclosed by Xs).
# Then, in each successive BFS, we will invalidate the positions that are touching
# these positions. Finally, we will count the number of tiles that are not invalidated.
def enclosed_tiles(explored_grid: list[list[str]]) -> int:
    # We will use a queue to keep track of the positions we need to visit.
    queue = []

    # First, enqueue all the positions on the top row that are not Xs.
    for col in range(NUM_COLS):
        if explored_grid[0][col] != "X":
            queue.append((0, col))

    # Next, enqueue all the positions on the bottom row that are not Xs.
    for col in range(NUM_COLS):
        if explored_grid[NUM_ROWS - 1][col] != "X":
            queue.append((NUM_ROWS - 1, col))

    # Next, enqueue all the positions on the left column that are not Xs. Except,
    # we don't want to enqueue the top-left or bottom-left corners as they are
    # already enqueued.
    for row in range(1, NUM_ROWS - 1):
        if explored_grid[row][0] != "X":
            queue.append((row, 0))

    # Next, enqueue all the positions on the right column that are not Xs. Except,
    # we don't want to enqueue the top-right or bottom-right corners as they are
    # already enqueued.
    for row in range(1, NUM_ROWS - 1):
        if explored_grid[row][NUM_COLS - 1] != "X":
            queue.append((row, NUM_COLS - 1))

    while queue:
        to_visit = len(queue)
        for _ in range(to_visit):
            # Get the next position to explore from the queue.
            row, col = queue.pop(0)

            if explored_grid[row][col] == "X":
                continue

            # Mark the current position as X.
            explored_grid[row][col] = "X"

            # Explore the neighbors. If it's an X, don't enqueue it. Otherwise, enqueue it.
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    r, c = row + dx, col + dy
                    if r == 0 and c == 0:
                        continue

                    if (
                        1 <= r < NUM_ROWS - 1
                        and 1 <= c < NUM_COLS - 1
                        and explored_grid[r][c] != "X"
                    ):
                        if explored_grid[r][c] in ACCEPTS_NORTH and dx == -1:
                            queue.append((r, c))

    # Count the number of tiles that are not invalidated (and thus are enclosed).
    num_enclosed = sum(1 for row in explored_grid for tile in row if tile != "X")

    print("\n\n" + "\n".join(["".join(row) for row in explored_grid]))

    return num_enclosed


num_enclosed = enclosed_tiles(pipes)
print(num_enclosed)
