"""Advent of code 2020 day 4"""

import csv
import string


def read_data(data_file):
    raw_data = []
    with open(data_file, newline="") as data_file:
        for row in csv.reader(data_file):
            if len(row) == 0:
                raw_data.append("|")
            else:
                raw_data.append(row[0])
    clean_data = [i for i in " ".join(raw_data).split("|")]
    return clean_data


example = read_data("example.csv")
data = read_data("data.csv")


def has_all_fields(data, required_fields):
    has_all_fields = []
    for i in data:
        if all(field in i for field in required_fields):
            has_all_fields.append(i)
    return has_all_fields


required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid",]


print(len(has_all_fields(example, required_fields)))
print(len(has_all_fields(data, required_fields)))


def find_entry(field, passport):
    return next(i for i in passport.split() if i.startswith(field)).split(":")[1]


def range_condition(x, min_allowed, max_allowed):
    return min_allowed <= int(x) <= max_allowed


def year_condition(x, min_allowed, max_allowed):
    return (len(x) == 4) & range_condition(x, min_allowed, max_allowed)


def count_valid(has_all_fields_list):
    n_valid = 0
    int_list = [str(i) for i in range(10)]
    hcl_alpha_list = list(string.ascii_lowercase.split("g")[0])
    hcl_list = int_list + hcl_alpha_list
    for i in has_all_fields_list:
        for field in required_fields:
            globals()[field] = find_entry(field, i)
        if not year_condition(byr, 1920, 2002):
            continue
        if not year_condition(iyr, 2010, 2020):
            continue
        if not year_condition(eyr, 2020, 2030):
            continue
        if hgt[-2:] not in ["cm", "in"]:
            continue
        if (hgt[-2:] == "cm") & (not range_condition(hgt[:-2], 150, 193)):
            continue
        if (hgt[-2:] == "in") & (not range_condition(hgt[:-2], 59, 76)):
            continue
        if len(hcl) != 7:
            continue
        if hcl[0] != "#":
            continue
        if any(j for j in hcl[1:] if j not in hcl_list):
            continue
        if ecl not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
            continue
        if len(pid) != 9:
            continue
        if any(j for j in pid if j not in int_list):
            continue
        n_valid = n_valid + 1
    return n_valid


print(count_valid(has_all_fields(data, required_fields)))
