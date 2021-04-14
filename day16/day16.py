"""Advent of code 2020 day 16"""

import csv
import math


def read_file(file):
    rules = {}
    tickets = []
    with open(file, newline="") as file:
        rows = [
            row
            for row in csv.reader(file)
            if row not in [[], ["your ticket:"], ["nearby tickets:"]]
        ]
    for row in rows:
        item = row[0]
        if item[0].isalpha():
            field = item[: item.find(":")]
            a = int(item[item.find(": ") + 2 : item.find("-")])
            b = int(item[item.find("-") + 1 : item.find(" or")])
            valid_0 = set(range(a, b + 1))
            a = int(item[item.find("or ") + 3 : item.rfind("-")])
            b = int(item[item.rfind("-") + 1 :])
            valid_1 = set(range(a, b + 1))
            valid = valid_0.union(valid_1)
            rules[field] = valid
        else:
            tickets.append(list(map(int, row)))
    return rules, tickets


example = read_file("example.csv")
data = read_file("data.csv")


def ticket_scanner(data):
    rules = data[0]
    tickets = data[1]
    valid_values = set.union(*rules.values())
    invalid_values = []
    invalid_tickets = []
    for ticket in tickets:
        for value in ticket:
            if value not in valid_values:
                invalid_values.append(value)
                invalid_tickets.append(ticket)
    return invalid_values, invalid_tickets


def find_error_rate(data):
    invalid_values = ticket_scanner(data)[0]
    return sum(invalid_values)


print(find_error_rate(example))
print(find_error_rate(data))


def find_valid_tickets(data):
    tickets = data[1]
    invalid_tickets = ticket_scanner(data)[1]
    valid_tickets = [i for i in tickets if i not in invalid_tickets]
    return valid_tickets


def find_field_order(data):
    valid_tickets = find_valid_tickets(data)
    rules = data[0]
    n_fields = len(rules)
    possible_positions = {}
    for field, valid in rules.items():
        possible_field_positions = []
        for i in range(n_fields):
            if set([ticket[i] for ticket in valid_tickets]).union(valid) == valid:
                possible_field_positions.append(i)
        possible_positions[field] = possible_field_positions
    field_order = [""] * n_fields
    while any(field == "" for field in field_order):
        for field, positions in possible_positions.items():
            if len(positions) == 1:
                position = positions[0]
                field_order[position] = field
                for possible_field_positions in possible_positions.values():
                    if position in possible_field_positions:
                        possible_field_positions.remove(position)
    return field_order


example2 = read_file("example2.csv")
print(find_field_order(example2))


def find_departure_positions(data):
    field_order = find_field_order(data)
    departure_positions = [
        i for i, field in enumerate(field_order) if field.startswith("departure")
    ]
    return departure_positions


departure_positions = find_departure_positions(data)
my_ticket = data[1][0]
print(math.prod([my_ticket[i] for i in departure_positions]))
