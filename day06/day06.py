"""Advent of code 2020 day 6"""

import csv


def read_file(file):
    data = []
    with open(file, newline="") as file:
        for row in csv.reader(file):
            if len(row) == 0:
                data.append("|")
            else:
                data.append(row[0])
    data = [i.split() for i in " ".join(data).split("|")]
    return data


example = read_file("example.csv")
data = read_file("data.csv")


def count_unique_chars(i):
    return len(set("".join(i)))


def solve_part_1(data):
    count = 0
    for i in data:
        count = count + count_unique_chars(i)
    return count


print(solve_part_1(example))
print(solve_part_1(data))


def count_common_chars(i):
    sets = [set(j) for j in i]
    return len(sets[0].intersection(*sets[1:]))


def solve_part_2(data):
    count = 0
    for i in data:
        count = count + count_common_chars(i)
    return count


print(solve_part_2(example))
print(solve_part_2(data))
