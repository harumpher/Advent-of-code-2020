"""Advent of code 2020 day 13"""

import csv


def read_file(file):
    with open(file, newline="") as file:
        reader = csv.reader(file)
        target = int(next(reader)[0])
        id_list = [int(i) if i != "x" else i for i in next(reader)]
    return target, id_list


example = read_file("example.csv")
example_target = example[0]
example_ids = example[1]
actual = read_file("actual.csv")
actual_target = actual[0]
actual_ids = actual[1]


def find_earliest_bus(target, ids):
    """from the target timestamp find the earliest bus"""
    wait_times = []
    positions = []
    for i in ids:
        if type(i) is int:
            next_multiple = target + i - (target % i)
            wait_time = next_multiple - target
            wait_times.append(wait_time)
            positions.append(ids.index(i))
    min_wait = min(wait_times)
    earliest_bus = ids[positions[wait_times.index(min_wait)]]
    return earliest_bus * min_wait


print(find_earliest_bus(example_target, example_ids))
print(find_earliest_bus(actual_target, actual_ids))


def find_earliest_timestamp(ids):
    """Find a number, t, that is divisible by all of the IDs plus their offsets.
    The approach is to find a t that is divisible by the first ID.
    Then check if it is divisible by the second ID plus its offset.
    If so check if it is divisible by the third ID plus its offset and so on.
    If not, iterate t by the lowest common multiple of the previous IDs and check that t.
    That is the next t that is divisible by all of the previous IDs plus their offsets.
    Continue this process until you find a t that is divisible by all of the IDs plus their offsets.
    This approach significantly reduces the search space.
    Since all of the numbers are prime, the lowest common multiple is just the product.
    """
    id_ints = [i for i in ids if type(i) is int]
    offsets = [ids.index(i) for i in id_ints]
    # start checking at the first instance of the first ID
    t = id_ints[0]
    lcm = id_ints[0]
    for i in range(1, len(id_ints)):
        id_current = id_ints[i]
        offset = offsets[i]
        while (t + offset) % id_current != 0:
            t = t + lcm
        lcm = lcm * id_current
    return t


print(find_earliest_timestamp(example_ids))
print(find_earliest_timestamp(actual_ids))