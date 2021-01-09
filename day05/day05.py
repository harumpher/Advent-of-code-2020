"""Advent of code 2020 day 5"""

import csv
import math


def read_file(file):
    results = []
    with open(file, newline="") as file:
        for row in csv.reader(file):
            results.append(row[0])
    return results


example = read_file("example.csv")
data = read_file("data.csv")


def partition(x, top_int, front_char):
    for i in range(len(x)):
        if x[i] == front_char:
            top_int = math.floor(top_int - 2**(len(x) - 1 - i))
    return top_int


def calc_seat_id(boarding_pass):
    row_chars = boarding_pass[:7]
    col_chars = boarding_pass[7:]
    seat_id = partition(row_chars, 127, "F") * 8 + partition(col_chars, 7, "L")
    return seat_id


def calc_seat_ids(boarding_passes):
    seat_ids = []
    for i in boarding_passes:
        seat_ids.append(calc_seat_id(i))
    return seat_ids


print(calc_seat_ids(example))
seat_ids = calc_seat_ids(data)
print(max(seat_ids))

for i in seat_ids:
    if (i != max(seat_ids)) & ((i + 1) not in seat_ids):
        print(i + 1)
