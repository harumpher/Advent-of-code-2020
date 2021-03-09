"""Advent of code 2020 day 9"""

import csv


def read_file(file):
    results = []
    with open(file, newline="") as file:
        for row in csv.reader(file):
            results.append(int(row[0]))
    return results


example = read_file("example.csv")
data = read_file("data.csv")


def find_invalid(data, preamble_length):
    for i in range(preamble_length, len(data)):
        preamble = data[(i - preamble_length) : i]
        x = data[i]
        if not any((((x - j) in preamble) and ((x - j) != j)) for j in preamble):
            break
    return x


print(find_invalid(example, 5))
print(find_invalid(data, 25))


def find_contiguous_set(data, preamble_length):
    invalid = find_invalid(data, preamble_length)
    for i in range(2, len(data) + 1):
        for j in range((len(data) + 1) - i):
            contiguous_set = data[j : (j + i)]
            if sum(contiguous_set) == invalid:
                break
        else:
            continue
        break
    return contiguous_set


def find_encryption_weakness(contiguous_set):
    return min(contiguous_set) + max(contiguous_set)


print(find_encryption_weakness(find_contiguous_set(example, 5)))
print(find_encryption_weakness(find_contiguous_set(data, 25)))
