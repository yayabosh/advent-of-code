from math import lcm

with open("input.txt") as f:
    # Read the instructions (first line) and the maps (third through end of file)
    instructions, maps = f.read().split("\n\n")

    # Will store the network as a dictionary. The key is the current labeled node,
    # and the value is going to be the tuple that contains the left and right
    # instructions you can take from this node.
    network = {}
    for line in maps.splitlines():
        # A line is in the format:
        # AAA = (BBB, CCC) <=> node = (left_node, )

        # Split the line into the current node and the left and right instructions
        # you can take from this node
        node, left_right = line.split(" = (")

        # Remove the trailing parenthesis
        left_right = left_right[:-1]
        left, right = left_right.split(", ")

        # Store the left and right instructions as a tuple
        network[node] = (left, right)


def num_steps_from_start_to_end(
    network: dict,
    instructions: str,
    starting_node: str,
    ending_node=None,
) -> int:
    # The number of steps we've taken
    num_steps = 0
    # The current instruction we're on
    instruction = 0
    # The current node we're on
    current_node = starting_node
    # The condition to stop at. If end is defined, we'll stop when we reach that node.
    # Otherwise, we'll stop when we reach a node that ends with "Z" (Part Two)
    # Define the condition based on whether 'end' is provided or not
    if ending_node:
        condition = lambda node: node != ending_node
    else:
        condition = lambda node: node[-1] != "Z"

    while condition(current_node):
        # Get the left and right instructions you can take from this node
        left, right = network[current_node]

        # Get the current instruction
        current_instruction = instructions[instruction]

        # Get the next node to visit
        next_node = left if current_instruction == "L" else right
        current_node = next_node

        # Increment the instruction
        instruction += 1
        instruction %= len(instructions)

        # Increment the number of steps
        num_steps += 1

    return num_steps


# Part One
num_steps = num_steps_from_start_to_end(network, instructions, "AAA", "ZZZ")
print(num_steps)


# Part Two
# We'll start at all nodes that end with "A"
starting_nodes = [node for node in network.keys() if node[-1] == "A"]
distances = [
    num_steps_from_start_to_end(network, instructions, node) for node in starting_nodes
]
num_steps = lcm(*distances)
print(num_steps)
