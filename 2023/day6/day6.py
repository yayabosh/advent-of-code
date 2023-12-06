from math import prod

with open("input.txt") as f:
    # Times are in the format: "Times: 1 2 3 4 5"
    times = [int(n) for n in f.readline().split(":")[1].strip().split()]
    # Distances are in the format: "Distances: 1 2 3 4 5"
    distances = [int(n) for n in f.readline().split(":")[1].strip().split()]
    # Zip them together to get a list of tuples
    races = zip(times, distances)


# Returns the number of ways to win a race (race time, record distance for that
# race). The race is a fixed number of seconds long, and the winner is
# the boat that travels the furthest in that time. The boat's distance is
# calculated by multiplying the time the button is held before the race starts
# with the number of seconds in the race minus the time the button was held.
# So, if there were 7 seconds in a race, and the button was held for 3 seconds,
# the boat would travel 3 * (7 - 3) = 12 units. If the boat travels further than
# the record distance, it counts as a "way" to win the race and will be returned
# by this function.
def num_ways_to_win_race(race):
    # Get the race's time and record distance
    race_time, record_distance = race
    # We can hold the button for X seconds, where X is in the range of 0 to
    # the total time in the race (inclusive). Let's test out all the possible
    # values of X and see if the boat travels further than the record distance.
    for time_holding_button in range(race_time + 1):
        boat_speed = time_holding_button
        # The boat will travel for the time in the race minus the time the
        # button was held
        travel_time = race_time - time_holding_button
        # Distance = speed * time
        distance_traveled = boat_speed * travel_time

        # If we found a way to beat the record distance, we know now the lower
        # bound on the time the button can be held.
        if distance_traveled > record_distance:
            # We beat the record distance with a time of X seconds holding the
            # button down. X is the lower bound.
            minimum_time_held = time_holding_button
            # Y seconds is the upper bound for how long we can hold the button
            # down. Because if we hold it down for Y seconds, the boat will
            # travel at a speed of X units per second for Y seconds, and since
            # X * Y = Y * X, the boat will travel the same distance as if we
            # held the button down for X seconds.
            maximum_time_held = race_time - time_holding_button
            break
    # If we never beat the record distance, we can just return 0
    else:
        return 0

    # The number of ways is equal to the upper bound of seconds we can hold the
    # button down minus the lower bound + 1 The + 1 is to include the lower
    # bound in the range.
    num_ways = maximum_time_held - minimum_time_held + 1
    return num_ways


# Part One
# Calculate the product of the number of ways to beat the record distance for
# each race
product_of_ways = prod(num_ways_to_win_race(race) for race in races)
print(product_of_ways)

# Part Two
# The time is in the form: "Times: 1 2 3 4 5", except the time should be 12345
race_time = int("".join([str(t) for t in times]))
# The distance is in the form: "Distances: 1 2 3 4 5", except the distance
# should be 12345
record_distance = int("".join([str(d) for d in distances]))

num_ways_longer_race = num_ways_to_win_race((race_time, record_distance))
print(num_ways_longer_race)
