"""Advent of code 2020 day 7"""

import csv
import re


def read_file(file):
    results = []
    with open(file, newline="") as file:
        for row in csv.reader(file):
            results.append(
                re.split(" bags contain | bag | bags | bags.| bag.", "".join(row))
            )
    results = {
        i[0]: {
            j if j[0] == "n" else j[2:]: 0 if j[0] == "n" else int(j[0])
            for j in i[1:-1]
        }
        for i in results
    }
    return results


example = read_file("example.csv")
data = read_file("data.csv")


def count_could_contain(data, color):
    data = data.copy()
    could_contain = [color]
    delete = [color]
    next_iter = True
    while next_iter:
        for check_color, contents in data.items():
            if any(i in contents for i in could_contain):
                could_contain.append(check_color)
                delete.append(check_color)
        if delete == []:
            next_iter = False
        for i in delete:
            del data[i]
        delete = []
    # drop initial color from list
    could_contain.remove(color)
    return len(could_contain)


print(count_could_contain(example, "shiny gold"))
print(count_could_contain(data, "shiny gold"))


def count_contents(data, color):
    count = 0
    direct_contents = data[color]
    if direct_contents == {"no other": 0}:
        return count
    else:
        for inner_color in direct_contents:
            inner_color_count = direct_contents[inner_color]
            count = count + inner_color_count
            # recursion
            inner_color_count_contents = count_contents(data, inner_color)
            count = count + (inner_color_count * inner_color_count_contents)
    return count


print(count_contents(example, "shiny gold"))
print(count_contents(data, "shiny gold"))
