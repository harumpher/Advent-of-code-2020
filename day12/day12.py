"""Advent of code 2020 day 12"""

import csv


def read_file(file):
    results = []
    with open(file, newline="") as file:
        for row in csv.reader(file):
            results.append([row[0][0], int(row[0][1:])])
    return results


example = read_file("example.csv")
data = read_file("data.csv")


def compass_directions():
    """list of compass directions"""
    # the ship starts facing east
    return ["E", "S", "W", "N"]


def compass_to_cartesian(compass_direction):
    """get cartesian direction from compass direction"""
    cartesian_directions = {"N": [0, 1], "E": [1, 0], "S": [0, -1], "W": [-1, 0]}
    return cartesian_directions[compass_direction]


def rotation_direction_to_int(rotation_direction):
    """get the way to cycle through the compass directions list"""
    rotation_direction_ints = {"L": -1, "R": 1}
    return rotation_direction_ints[rotation_direction]


def move(location, compass_direction, steps):
    """move the ship"""
    cartesian_direction = compass_to_cartesian(compass_direction)
    new_location = [
        sum(x) for x in zip(location, [i * steps for i in cartesian_direction])
    ]
    return new_location


def rotate(current_facing, rotation_direction, degrees):
    """rotate the ship"""
    # using modular arithmetic to cycle through the compass directions list
    current_facing_index = compass_directions().index(current_facing)
    cycle_direction = rotation_direction_to_int(rotation_direction)
    shift_positions = int(degrees / 90)
    new_facing_index = (current_facing_index + (cycle_direction * shift_positions)) % 4
    new_facing = compass_directions()[new_facing_index]
    return new_facing


def follow_instructions(instructions):
    """follow the instructions from part 1"""
    # the ship starts at (0,0) facing east
    location = [0, 0]
    current_facing = "E"
    for instruction in instructions:
        if instruction[0] in (compass_directions() + ["F"]):
            if instruction[0] in compass_directions():
                compass_direction = instruction[0]
            elif instruction[0] == "F":
                compass_direction = current_facing
            steps = instruction[1]
            location = move(location, compass_direction, steps)
        else:
            rotation_direction = instruction[0]
            degrees = instruction[1]
            current_facing = rotate(current_facing, rotation_direction, degrees)
    return sum(list(map(abs, location)))


print(follow_instructions(example))
print(follow_instructions(data))


def move_ship(location, waypoint, step_instruction):
    """move the ship toward the waypoint"""
    # now that the ship is moving relative to the waypoint we can restrict the directions
    # to East and North and then negative numbers will move West and South
    compass_directions_positive = ["E", "N"]
    for i in [0, 1]:
        compass_direction = compass_directions_positive[i]
        steps = waypoint[i] * step_instruction
        location = move(location, compass_direction, steps)
    return location


def get_waypoint_compass(waypoint):
    """the compass directions of the waypoint from the ship"""
    waypoint_compass = ["", ""]
    if waypoint[0] >= 0:
        waypoint_compass[0] = "E"
    elif waypoint[0] < 0:
        waypoint_compass[0] = "W"
    if waypoint[1] >= 0:
        waypoint_compass[1] = "N"
    elif waypoint[1] < 0:
        waypoint_compass[1] = "S"
    return waypoint_compass


def rotate_waypoint(waypoint, rotation_direction, degrees):
    """rotate the waypoint around the ship"""
    waypoint_compass = get_waypoint_compass(waypoint)
    move_dict = {}
    for i in [0, 1]:
        compass_direction = rotate(waypoint_compass[i], rotation_direction, degrees)
        # take the absolute value because the direction to move is already determined
        steps = abs(waypoint[i])
        # moving from (0,0) because want the relative distance from the ship
        move_dict[i] = move([0, 0], compass_direction, steps)
    new_waypoint = [sum(x) for x in zip(*list(move_dict.values()))]
    return new_waypoint


def follow_instructions_properly(instructions):
    """follow the instructions from part 2"""
    # the ship starts at (0,0)
    location = [0, 0]
    # the waypoint starts 10 East and 1 North from the ship
    waypoint = [10, 1]
    for instruction in instructions:
        if instruction[0] == "F":
            step_instruction = instruction[1]
            location = move_ship(location, waypoint, step_instruction)
        elif instruction[0] in compass_directions():
            compass_direction = instruction[0]
            steps = instruction[1]
            waypoint = move(waypoint, compass_direction, steps)
        else:
            rotation_direction = instruction[0]
            degrees = instruction[1]
            waypoint = rotate_waypoint(waypoint, rotation_direction, degrees)
    return sum(list(map(abs, location)))


print(follow_instructions_properly(example))
print(follow_instructions_properly(data))
