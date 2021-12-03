"""Advent of code 2020 day 25"""


def find_loop_size(subject_number, key):
    value = 1
    i = 0
    while value != key:
        value = value * subject_number
        value = value % 20201227
        i = i + 1
    assert value == key
    return i


def find_encryption_key(subject_number, loop_size):
    value = 1
    i = 0
    while i < loop_size:
        value = value * subject_number
        value = value % 20201227
        i = i + 1
    return value


subject_number = 7


example_card_key = 5764801
example_door_key = 17807724


example_card_loop_size = find_loop_size(subject_number, example_card_key)
example_door_loop_size = find_loop_size(subject_number, example_door_key)


print(find_encryption_key(example_door_key, example_card_loop_size))
print(find_encryption_key(example_card_key, example_door_loop_size))


card_key = 11349501
door_key = 5107328


card_loop_size = find_loop_size(subject_number, card_key)
door_loop_size = find_loop_size(subject_number, door_key)


print(find_encryption_key(door_key, card_loop_size))
print(find_encryption_key(card_key, door_loop_size))
