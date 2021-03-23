"""Advent of code 2020 day 10"""

import csv


def read_file(file):
    results = []
    with open(file, newline="") as file:
        for row in csv.reader(file):
            results.append(int(row[0]))
    return results


example = read_file("example.csv")
data = read_file("data.csv")


def count_diffs(data):
    top = max(data)
    current = 0
    count_1 = 0
    count_3 = 0
    while current < top:
        if (current + 1) in data:
            current = current + 1
            count_1 = count_1 + 1
        elif (current + 3) in data:
            current = current + 3
            count_3 = count_3 + 1
    # add built-in diff of 3
    count_3 = count_3 + 1
    return count_1 * count_3


print(count_diffs(example))
print(count_diffs(data))


def count_arrangements(data):
    data = data.copy()
    data.sort()
    data.insert(0, 0)
    top = data[-1] + 3
    data.append(top)
    # one way to start at 0
    count_ways = {0: 1}
    for i in data[1:]:
        ways = 0
        for j in range(1, 4):
            if (i - j) not in data:
                continue
            else:
                ways = ways + count_ways[i - j]
        count_ways[i] = ways
    return count_ways[top]


print(count_arrangements(example))
print(count_arrangements(data))
