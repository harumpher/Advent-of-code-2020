"""Advent of code 2020 day 8"""

import csv


def read_file(file):
    operation = []
    argument = []
    with open(file, newline="") as file:
        for row in csv.reader(file):
            operation.append(row[0][:3])
            argument.append(int(row[0][4:]))
    return operation, argument


example = read_file("example.csv")
data = read_file("data.csv")


def accumulator(data):
    value = 0
    i = 0
    visited = []
    terminate = False
    while not terminate:
        operation = data[0][i]
        visited.append(i)
        if operation == "acc":
            value = value + data[1][i]
        if operation in ["nop", "acc"]:
            i = i + 1
        elif operation == "jmp":
            i = i + data[1][i]
        if i in visited:
            terminate = True
        if i == len(data[0]):
            terminate = True
    return value, i


print(accumulator(example))
print(accumulator(data))


def fix_program(data):
    check_positions = [i for i, x in enumerate(data[0]) if x in ["nop", "jmp"]]
    for i in check_positions:
        temp = (data[0].copy(), data[1].copy())
        if temp[0][i] == "nop":
            temp[0][i] = "jmp"
        elif temp[0][i] == "jmp":
            temp[0][i] = "nop"
        result = accumulator(temp)
        if result[1] == len(temp[0]):
            return result


print(fix_program(example))
print(fix_program(data))
