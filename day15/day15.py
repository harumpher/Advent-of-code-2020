"""Advent of code 2020 day 15. Part 2 takes about 20 seconds"""

import time

examples = [[0, 3, 6], [1, 3, 2], [2, 1, 3], [1, 2, 3], [2, 3, 1], [3, 2, 1], [3, 1, 2]]
actual = [2, 0, 1, 9, 5, 19]


def find_last_spoken(starting_numbers, turns):
    last_turn_spoken = {
        number: (position + 1) for position, number in enumerate(starting_numbers)
    }
    turn = len(starting_numbers)
    last_number_spoken = starting_numbers[-1]
    while turn < turns:
        if last_number_spoken in last_turn_spoken:
            diff = turn - last_turn_spoken[last_number_spoken]
            last_turn_spoken[last_number_spoken] = turn
            last_number_spoken = diff
        else:
            last_turn_spoken[last_number_spoken] = turn
            last_number_spoken = 0
        turn = turn + 1
    return last_number_spoken


for example in examples:
    start = time.time()
    print(find_last_spoken(example, 2020))
    end = time.time()
    print(end - start)


start = time.time()
print(find_last_spoken(actual, 2020))
end = time.time()
print(end - start)


for example in examples:
    start = time.time()
    print(find_last_spoken(example, 30000000))
    end = time.time()
    print(end - start)


start = time.time()
print(find_last_spoken(actual, 30000000))
end = time.time()
print(end - start)