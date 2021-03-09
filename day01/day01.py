"""Advent of code 2020 day 1"""

import csv
import numpy as np


def read_data(data_file):
    results = []
    with open(data_file, newline="") as data_file:
        for row in csv.reader(data_file):
            results.append(int(row[0]))
    return results


example = read_data(data_file="example.csv")
data = read_data(data_file="data.csv")


def find_winning_pair(data):
    """Find the two numbers in the list that sum to 2020"""
    n = len(data)
    pair_sum = 0
    for i in range(n - 1):
        x = data[i]
        for j in range(i + 1, n):
            y = data[j]
            pair_sum = x + y
            if pair_sum == 2020:
                break
        else:
            continue
        break
    assert pair_sum == 2020
    return x, y


print(find_winning_pair(example))
print(np.prod(find_winning_pair(example)))

print(find_winning_pair(data))
print(np.prod(find_winning_pair(data)))


def find_winning_triple(data):
    """Find the three numbers in the list that sum to 2020"""
    n = len(data)
    triple_sum = 0
    for i in range(n - 2):
        x = data[i]
        for j in range(i + 1, n - 1):
            y = data[j]
            for k in range(j + 1, n):
                z = data[k]
                triple_sum = x + y + z
                if triple_sum == 2020:
                    break
            else:
                continue
            break
        else:
            continue
        break
    assert triple_sum == 2020
    return x, y, z


print(find_winning_triple(example))
print(np.prod(find_winning_triple(example)))

print(find_winning_triple(data))
print(np.prod(find_winning_triple(data)))
