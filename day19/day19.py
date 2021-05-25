"""Advent of code 2020 day 19"""

import csv


def rule_string_to_list(rule):
    return [[int(char) for char in option.split()] for option in rule.split("|")]


def read_file(file):
    results = []
    with open(file, newline="") as file:
        for row in csv.reader(file):
            if len(row) == 0:
                results.append("split")
            else:
                results.append(row[0])
    split_id = results.index("split")
    messages = results[(split_id + 1):]
    rules = results[:(split_id)]
    rule_dict = {}
    for rule in rules:
        key, value = rule.split(": ")
        key = int(key)
        if value[0] != '"':
            value = rule_string_to_list(value)
        rule_dict[key] = value
    return rule_dict, messages


rules_ex, messages_ex = read_file("example.csv")
rules_ex_2, messages_ex_2 = read_file("example_2.csv")
rules, messages = read_file("data.csv")


def check_valid(rules, message, rule_ids):
    """recursive function for checking if a message is valid"""
    # if there are no more characters to check in the message and there are no more rules, then the message is valid
    # if there are characters remaining but no more rules, then the message is invalid
    # if there are rules remaining but no more characters, then the message is invalid
    if (message == "") or (rule_ids == []):
        if (message == "") and (rule_ids == []):
            return True
        else:
            return False
    # while there are still characters to check
    rule_id = rule_ids[0]
    rule = rules[rule_id]
    # case where the rule is a single character
    if rule[0] == '"':
        # if the first character in the message matches the rule, then check the remaining characters recursively
        message_char = message[0]
        rule_char = rule.replace('"', '')
        if message_char == rule_char:
            return check_valid(rules, message[1:], rule_ids[1:])
        else:
            return False
    # case where the rule is a list of other rule IDs
    # check the first character against each option in the rule for that character
    # and keep checking characters recursively
    else:
        return any(
            check_valid(rules, message, option + rule_ids[1:]) for option in rule
        )


def count_valid(rules, messages, rule_ids):
    count = 0
    for message in messages:
        if check_valid(rules, message, rule_ids):
            count = count + 1
    return count


print(count_valid(rules_ex, messages_ex, [0]))
print(count_valid(rules, messages, [0]))


print(count_valid(rules_ex_2, messages_ex_2, [0]))
rules_ex_2_updated = rules_ex_2.copy()
rules_ex_2_updated[8] = rule_string_to_list("42 | 42 8")
rules_ex_2_updated[11] = rule_string_to_list("42 31 | 42 11 31")
print(count_valid(rules_ex_2_updated, messages_ex_2, [0]))


rules_updated = rules.copy()
rules_updated[8] = rule_string_to_list("42 | 42 8")
rules_updated[11] = rule_string_to_list("42 31 | 42 11 31")
print(count_valid(rules_updated, messages, [0]))
