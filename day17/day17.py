"""Advent of code 2020 day 17"""

import csv
import operator
import itertools


def read_file(file):
    results = {}
    with open(file, newline="") as file:
        for i, row in enumerate(csv.reader(file)):
            item = row[0]
            for j in range(len(item)):
                results[(j, i, 0)] = item[j]
    return results


example = read_file("example.csv")
data = read_file("data.csv")


def find_neighbour_keys(key, dimensions):
    diffs = list(itertools.product([-1, 1, 0], repeat=dimensions))
    diffs = [diff for diff in diffs if set(diff) != {0}]
    neighbour_keys = []
    for diff in diffs:
        neighbour_keys.append(tuple(map(operator.add, key, diff)))
    return neighbour_keys


def one_cycle(data, dimensions):
    new_keys = []
    for key in data:
        neighbour_keys = find_neighbour_keys(key, dimensions)
        for neighbour_key in neighbour_keys:
            if neighbour_key not in data:
                new_keys.append(neighbour_key)
    data_0 = data.copy()
    for key in new_keys:
        data_0[key] = "."
    data_1 = data_0.copy()
    for key, val in data_0.items():
        neighbour_keys = find_neighbour_keys(key, dimensions)
        neighbour_vals = []
        for neighbour_key in neighbour_keys:
            if neighbour_key in data_0:
                neighbour_vals.append(data_0[neighbour_key])
        neighbour_active_count = neighbour_vals.count("#")
        if val == "#":
            if neighbour_active_count not in [2, 3]:
                data_1[key] = "."
        if val == ".":
            if neighbour_active_count == 3:
                data_1[key] = "#"
    return data_1


def add_dimension(data):
    return {(*key, 0): val for key, val in data.items()}


def run_simulation(data, dimensions, n_cycles):
    if dimensions == 4:
        data_update = add_dimension(data.copy())
    else:
        data_update = data.copy()
    for i in range(n_cycles):
        data_update = one_cycle(data_update, dimensions)
    return data_update


def count_active(data, dimensions, n_cycles):
    simulation = run_simulation(data, dimensions, n_cycles)
    return list(simulation.values()).count("#")


print(count_active(example, 3, 6))
print(count_active(data, 3, 6))

print(count_active(example, 4, 6))
print(count_active(data, 4, 6))
