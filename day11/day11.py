"""Advent of code 2020 day 11"""

import csv


def read_file(file):
    results = []
    with open(file, newline="") as file:
        for row in csv.reader(file):
            results.append(row[0])
    graph = {}
    for x in range(len(results[0])):
        for y in range(len(results)):
            graph[(x, y)] = results[y][x]
    return graph


example = read_file("example.csv")
data = read_file("data.csv")


def one_round(graph, rules):
    graph_new = graph.copy()
    max_point = list(graph.keys())[-1]
    x_max = max_point[0]
    y_max = max_point[1]
    # all the valid directions to go in from a point
    directions = [[0, 1], [0, -1], [1, 0], [-1, 0], [1, 1], [-1, -1], [1, -1], [-1, 1]]
    for key, val in graph.items():
        if val == ".":
            continue
        else:
            x = key[0]
            y = key[1]
            checks = []
            for direction in directions:
                i = direction[0]
                j = direction[1]
                check_x = x + i
                check_y = y + j
                check = False
                while (0 <= check_x <= x_max) and (0 <= check_y <= y_max):
                    check_val = graph[(check_x, check_y)]
                    if check_val == "L":
                        break
                    if check_val == "#":
                        check = True
                        break
                    # break out of the loop now if only want the adjacent points
                    if rules == "part_1":
                        break
                    # continue loop if want all visible points
                    check_x = check_x + i
                    check_y = check_y + j
                checks.append(check)
            count_occupied = sum(checks)
            if val == "L":
                if count_occupied == 0:
                    graph_new[key] = "#"
            if val == "#":
                if rules == "part_1":
                    max_occupied = 4
                else:
                    max_occupied = 5
                if count_occupied >= max_occupied:
                    graph_new[key] = "L"
    return graph_new


def stabilize(graph, rules):
    graph = graph.copy()
    graph_new = {}
    while graph_new != graph:
        graph_new = graph.copy()
        graph = one_round(graph, rules)
    return graph


def count_occupied(graph):
    return list(graph.values()).count("#")


print(count_occupied(stabilize(example, "part_1")))
print(count_occupied(stabilize(data, "part_1")))
print(count_occupied(stabilize(example, "part_2")))
print(count_occupied(stabilize(data, "part_2")))