"""Advent of code 2020 day 14"""

import csv
import math
import itertools


def read_file(file):
    masks = []
    memory_instructions = []
    memory_instructions_i = []
    with open(file, newline="") as file:
        for row in csv.reader(file):
            item = row[0]
            if item[:4] == "mask":
                memory_instructions.append(memory_instructions_i)
                memory_instructions_i = []
                masks.append([int(x) if x == "1" or x == "0" else x for x in item[7:]])
            else:
                memory_dict = {}
                key = int(item[item.find("[") + 1 : item.rfind("]")])
                value = int(item[item.find("= ") + 2 :])
                memory_dict[key] = value
                memory_instructions_i.append(memory_dict)
        # add the final list to memory_instructions
        memory_instructions.append(memory_instructions_i)
        # remove the initial empty list from memory_instructions
        memory_instructions.pop(0)
    return masks, memory_instructions


example = read_file("example.csv")
data = read_file("data.csv")


def apply_bitmask(bit, mask_bit):
    if mask_bit != "X":
        bit = mask_bit
    return bit


def int_to_binary(integer):
    binary = []
    if integer == 0:
        for i in range(36):
            binary.insert(0, 0)
    else:
        while integer > 0:
            remainder = integer % 2
            binary.insert(0, remainder)
            integer = math.floor(integer / 2)
        for i in range(36 - len(binary)):
            binary.insert(0, 0)
    return binary


def binary_to_int(binary):
    integer = 0
    for i in range(36):
        bit = binary[i]
        power = 36 - i - 1
        bit_integer = bit * (2 ** power)
        integer = integer + bit_integer
    return integer


def initialize_program(data):
    masks = data[0]
    memory_instructions = data[1]
    memory = {}
    for i in range(len(masks)):
        mask = masks[i]
        for j in memory_instructions[i]:
            for key, val in j.items():
                binary = int_to_binary(val)
                mask_binary = list(map(apply_bitmask, binary, mask))
                integer = binary_to_int(mask_binary)
                memory[key] = integer
    return memory


print(sum(initialize_program(example).values()))
print(sum(initialize_program(data).values()))


example2 = read_file("example2.csv")


def apply_bitmask2(bit, mask_bit):
    if mask_bit == 1:
        bit = 1
    elif mask_bit == "X":
        bit = "X"
    return bit


def binary_to_base_int(binary):
    base_integer = 0
    for i in range(len(binary)):
        if binary[i] != "X":
            bit = binary[i]
            power = 36 - i - 1
            bit_integer = bit * (2 ** power)
            base_integer = base_integer + bit_integer
    return base_integer


def find_addresses(binary):
    base_integer = binary_to_base_int(binary)
    bit_integers = []
    for i in range(len(binary)):
        bit_integers_i = [0]
        if binary[i] == "X":
            power = 36 - i - 1
            bit_integer = 2 ** power
            bit_integers_i.append(bit_integer)
            bit_integers.append(bit_integers_i)
    combinations = list(itertools.product(*bit_integers))
    addresses = []
    for j in combinations:
        addresses.append(base_integer + sum(j))
    return addresses


def initialize_program2(data):
    masks = data[0]
    memory_instructions = data[1]
    memory = {}
    for i in range(len(masks)):
        mask = masks[i]
        for j in memory_instructions[i]:
            for key, val in j.items():
                binary = int_to_binary(key)
                mask_binary = list(map(apply_bitmask2, binary, mask))
                addresses = find_addresses(mask_binary)
            for k in addresses:
                memory[k] = val
    return memory


print(sum(initialize_program2(example2).values()))
print(sum(initialize_program2(data).values()))