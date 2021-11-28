"""Advent of code 2020 day 23"""


example = [int(x) for x in "389125467"]
actual = [int(x) for x in "135468729"]


def find_cup_m1(current, max_cup):
    destination = current - 1
    if destination == 0:
        destination = max_cup
    return destination


def play_game(cup_list, n):
    circle_size = len(cup_list)
    circle_map = {cup_list[i]: cup_list[i + 1] for i in range(circle_size - 1)}
    # complete the circle
    circle_map[cup_list[-1]] = cup_list[0]
    max_cup = max(cup_list)
    current = cup_list[0]
    for i in range(n):
        pick_ups = []
        pick_up = circle_map[current]
        for i in range(3):
            pick_ups.append(pick_up)
            pick_up = circle_map[pick_up]
        destination = find_cup_m1(current, max_cup)
        if destination in pick_ups:
            while destination in pick_ups:
                destination = find_cup_m1(destination, max_cup)
        first_pick_up = pick_ups[0]
        last_pick_up = pick_ups[-1]
        new_after_pick_ups = circle_map[destination]
        new_after_current = circle_map[last_pick_up]
        circle_map[destination] = first_pick_up
        circle_map[last_pick_up] = new_after_pick_ups
        circle_map[current] = new_after_current
        current = circle_map[current]
    return circle_map


def solve_part_1(cup_list, n):
    result = play_game(cup_list, n)
    circle_size = len(cup_list)
    result_str = ""
    key = 1
    for j in range(circle_size - 1):
        result_str = result_str + str(result[key])
        key = result[key]
    return result_str


print(solve_part_1(example, 100))
print(solve_part_1(actual, 100))


def build_part_2_cup_list(cup_list):
    return cup_list + list(range(10, 10 ** 6 + 1))


example_part_2 = build_part_2_cup_list(example)
actual_part_2 = build_part_2_cup_list(actual)


def solve_part_2(cup_list, n):
    result = play_game(cup_list, n)
    star_1 = result[1]
    star_2 = result[star_1]
    return star_1, star_2, star_1 * star_2


print(solve_part_2(example_part_2, 10 ** 7))
print(solve_part_2(actual_part_2, 10 ** 7))
