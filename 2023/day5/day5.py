# Input is in the form of:
# Seeds: 1 2 3 4 5
#
# Map:
# 1 2 3
# 4 5 6
# 7 8 9
with open("input.txt") as f:
    # Python fun stuff to read the first element into seeds and then the rest
    # into map_blocks as a list of strings 🤗
    seeds, *map_blocks = f.read().split("\n\n")

# Part One
# Seeds are in the form "Seeds: 1 2 3 4 5" as a list of seeds
seeds = list(map(int, seeds.split(":")[1].split()))

# Each iteration of the loop is one conversion of the seed through the map
for block in map_blocks:
    # Get rid of the first line since it's just the map name
    ranges = []
    for line in block.splitlines()[1:]:
        # Store the map ranges as (source_start, dest_start, range_length) tuples
        dest_start, source_start, range_length = map(int, line.split())
        ranges.append((source_start, dest_start, range_length))

    # Will contain the seeds to be processed in the NEXT iteration
    queue = []
    for seed in seeds:
        for source_start, dest_start, range_length in reversed(ranges):
            # We found a seed number that maps to a destination number. So
            # we want to append the destination number to the queue, so it can
            # be processed in the NEXT iteration.
            if source_start <= seed < source_start + range_length:
                mapping = dest_start + (seed - source_start)
                queue.append(mapping)
                break
        # If we never broke out of the loop, it means we found no seed numbers
        # that map to a destination number. So we want to append the seed number
        # to the queue, so it can be processed in the NEXT iteration anyways.
        else:
            queue.append(seed)

    # Update the seeds for the next iteration.
    seeds = queue

# At this point, seeds contains the location numbers after all the iterations,
# since the last map in the map_blocks input is humidity-to-location.
locations = seeds
lowest_location = min(locations)
print(lowest_location)


# Part Two
with open("input.txt") as f:
    seeds, *map_blocks = f.read().split("\n\n")

# Seeds are in the form "Seeds: 1 2 3 4 5" as a pair of (seed number, range length)
seeds = list(map(int, seeds.split(":")[1].split()))

# Put the (seed number, range length) pairs into a list
seed_ranges = []
for i in range(0, len(seeds), 2):
    range_start = seeds[i]
    range_end = range_start + seeds[i + 1]
    seed_ranges.append((range_start, range_end))

for map_block in map_blocks:
    # Get rid of the first line since it's just the map name
    ranges = []
    for line in map_block.splitlines()[1:]:
        # Store the map ranges as (source_start, dest_start, range_length) tuples
        dest_start, source_start, range_length = map(int, line.split())
        ranges.append((source_start, dest_start, range_length))

    # Will contain the seed ranges to be processed in the NEXT iteration
    queue = []
    # Process the seed ranges. We can stop once we finish this level of seed ranges.
    while seed_ranges:
        start, end = seed_ranges.pop(0)
        for source_start, dest_start, range_length in reversed(ranges):
            # We currently have something like:
            #   [source_start   source_end]
            #             [start            end]
            # We want to split this into two ranges:
            #             [start          ]
            #                             [ end]
            #
            # Another case:
            #           [source_start   source_end]
            #    [start                            end]
            # Want to split into three ranges:
            #           [source_start   source_end]
            #    [start ]                         [ end]

            # In total, we might have something like this:
            #  [a_start        a_end]   [b_start      b_end]
            #             [start            end]
            # Basically, we have one seed range that overlaps with two map ranges
            # in this level.
            # So, for the overlapping parts ([start, a_end] and [b_start, end]),
            # we want to append the destination ranges to the queue, because they
            # will be processed in the NEXT iteration.
            #
            # For the non-overlapping parts ([a_end, b_start]), we want to append
            # them to the seeds, because they will be processed in THIS iteration.
            new_start = max(source_start, start)
            new_end = min(source_start + range_length, end)

            # If this new range is non-empty, it means we had some overlap
            # between the seed range and the map range. So we need to add
            # this new range to the list of seeds to be processed in the
            # NEXT iteration
            if new_start < new_end:
                # Remember, we have to add the DESTINATION ranges into the queue
                # because they're mappings. So we start with the destination start,
                # and then shift ahead by the difference between the new start
                # and the source start and the new end and the source start.
                queue.append(
                    (
                        dest_start + (new_start - source_start),
                        dest_start + (new_end - source_start),
                    )
                )

                # This means we have elements before new_start (start : new_start)
                # that still need to be processed in THIS iteration
                if start < new_start:
                    seed_ranges.append((start, new_start))

                # This means we have elements after new_end (new_end : end)
                # that still need to be processed in THIS iteration
                if new_end < end:
                    seed_ranges.append((new_end, end))

                break
        else:
            # If we didn't break out of the loop, it means we didn't have
            # any overlap between the seed range and the map range. So we
            # can just add the whole seed range (as the newly mapped range)
            # into the queue to be processed in the NEXT iteration
            queue.append((start, end))

    # Update the seeds for the next iteration.
    seed_ranges = queue

# We only care about the start of the seed ranges, since that's the lowest
# number in the range. So we calculate the minimum of all the seed range starts.
lowest_location = min(seed_ranges)[0]
print(lowest_location)
