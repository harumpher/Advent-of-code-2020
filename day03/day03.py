"""Advent of code 2020 day 3"""

import csv
import numpy as np


def read_data(data_file):
    results = []
    with open(data_file, newline="") as data_file:
        for row in csv.reader(data_file):
            results.append(row[0])
    return results


example = read_data("example.csv")
data = read_data("data.csv")


def traverse(data, right, down):
    n = len(data)
    row_length = len(data[0])
    counter = 0
    n_trees = 0
    for i in range(down, n, down):
        counter = counter + 1
        x = data[i]
        j = (right * counter) % row_length
        if x[j] == "#":
            n_trees = n_trees + 1
    return n_trees


print(traverse(example, 3, 1))
print(traverse(data, 3, 1))


slopes = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]


def traverse_more_slopes(data, slopes):
    n_trees = []
    for i in slopes:
        n_trees.append(traverse(data, i[0], i[1]))
    return n_trees


print(traverse_more_slopes(example, slopes))
print(np.prod(traverse_more_slopes(example, slopes)))


print(traverse_more_slopes(data, slopes))
print(np.prod(traverse_more_slopes(data, slopes)))
