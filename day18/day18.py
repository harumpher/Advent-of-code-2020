"""Advent of code 2020 day 18"""

import csv


def read_file(file):
    results = []
    with open(file, newline="") as file:
        for row in csv.reader(file):
            results.append(row[0].replace(" ", ""))
    return results


example = read_file("example.csv")
data = read_file("data.csv")


def find_last_expression_info(string):
    """find the last expression in a string that is within parentheses
    and store its start and end positions
    """
    open_position = string.rfind("(") + 1
    substring = string[open_position:]
    close_position = substring.find(")")
    expression = substring[:close_position]
    start = open_position - 1
    end = open_position + close_position + 1
    return expression, start, end


def find_positions(expression, char):
    """find the positions of a character in an expression"""
    return [i for i in range(len(expression)) if expression[i] == char]


def find_first_operator_position(expression):
    """find the position of the first operator in an expression"""
    operator_positions = []
    for operator in operators:
        operator_positions = operator_positions + find_positions(expression, operator)
    first_operator_position = min(operator_positions)
    return first_operator_position


def find_delimiter_positions(expression):
    """find the positions of the delimiters in an expression
    and sort the positions in ascending order
    """
    delimiter_positions = []
    for delimiter in delimiters:
        delimiter_positions = delimiter_positions + find_positions(
            expression, delimiter
        )
    delimiter_positions.sort()
    return delimiter_positions


def count_operators(expression):
    """count the number of operators in an expression"""
    operator_count = 0
    for operator in operators:
        operator_count = operator_count + expression.count(operator)
    return operator_count


def evaluate(expression):
    """evaluate an expression"""
    operator_count = count_operators(expression)
    while operator_count > 0:
        first_operator_position = find_first_operator_position(expression)
        delimiter_positions = find_delimiter_positions(expression)
        delimiter_index = delimiter_positions.index(first_operator_position)
        # case where there is only one delimiter in the expression
        if len(delimiter_positions) == 1:
            expression = str(eval(expression))
        else:
            # case where the first operator is the first delimiter
            if first_operator_position == delimiter_positions[0]:
                end = delimiter_positions[1]
                evaluated = str(eval(expression[:end]))
                expression = evaluated + expression[end:]
            # case where the first operator is the last delimiter
            elif first_operator_position == delimiter_positions[-1]:
                start = delimiter_positions[-2] + 1
                evaluated = str(eval(expression[start:]))
                expression = expression[:start] + evaluated
            # case where there are delimiters on both sides of the first operator
            else:
                start = delimiter_positions[delimiter_index - 1] + 1
                end = delimiter_positions[delimiter_index + 1]
                evaluated = str(eval(expression[start:end]))
                expression = expression[:start] + evaluated + expression[end:]
        operator_count = count_operators(expression)
    evaluated = str(eval(expression))
    return evaluated


def evaluate_string(string):
    """generic evaluate a string"""
    while "(" in string:
        expression_info = find_last_expression_info(string)
        expression = expression_info[0]
        start = expression_info[1]
        end = expression_info[2]
        evaluated = evaluate(expression)
        string = string[:start] + evaluated + string[end:]
    return evaluate(string)


def evaluate_string_pt1(string):
    """evaluate a string using the part 1 rules"""
    globals()["operators"] = ["*", "+"]
    globals()["delimiters"] = ["*", "+"]
    return evaluate_string(string)


def evaluate_string_pt2(string):
    """evaluate a string using the part 2 rules"""
    globals()["operators"] = ["+"]
    globals()["delimiters"] = ["*", "+"]
    return evaluate_string(string)


def evaluate_list(data, part):
    """evaluate an entire list of strings and sum the values"""
    data_evaluated = []
    for i in data:
        if part == 1:
            evaluated = evaluate_string_pt1(i)
        if part == 2:
            evaluated = evaluate_string_pt2(i)
        data_evaluated.append(int(evaluated))
    return sum(data_evaluated)


for string in example:
    print(evaluate_string_pt1(string))

print(evaluate_list(data, part=1))


for string in example:
    print(evaluate_string_pt2(string))

print(evaluate_list(data, part=2))