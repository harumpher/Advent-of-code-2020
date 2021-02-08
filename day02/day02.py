"""Advent of code 2020 day 2"""

import csv
import re


def read_data(data_file):
    results = []
    with open(data_file, newline="") as data_file:
        for row in csv.reader(data_file):
            results.append(re.split("-| |: ", row[0]))
    return results


example = read_data("example.csv")
data = read_data("data.csv")


def count_valid(data):
    valid = 0
    for x in data:
        n = x[-1].count(x[-2])
        if (n >= int(x[0])) & (n <= int(x[1])):
            valid = valid + 1
    return valid


print(count_valid(example))
print(count_valid(data))


def count_valid_part2(data):
    valid = 0
    for x in data:
        value1 = x[-1][int(x[0]) - 1]
        value2 = x[-1][int(x[1]) - 1]
        matches = 0
        if value1 == x[-2]:
            matches = matches + 1
        if value2 == x[-2]:
            matches = matches + 1
        if matches == 1:
            valid = valid + 1
    return valid


print(count_valid_part2(example))
print(count_valid_part2(data))
