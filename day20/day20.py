"""Advent of code 2020 day 20"""

import csv
from functools import reduce
from operator import mul


def read_file(file):
    results = []
    with open(file, newline="") as file:
        for row in csv.reader(file):
            if not "".join(row).strip():
                continue
            results.append(row[0])
    keys = [int(i[-5:-1]) for i in results if "Tile" in i]
    tiles = [i for i in results if "Tile" not in i]
    n = 10
    tiles = [tiles[i * n : (i + 1) * n] for i in range((len(tiles) + n - 1) // n)]
    return dict(zip(keys, tiles))


def solve_part_1(file):
    """The method for part 1 is to:
    1. Find all the possible edges for each tile. After flipping and rotating,
        this includes all of the edges and all of the edges reversed.
    2. Compare the possible edges of each tile to the set of all the possible edges
        of the other tiles.
    3. If there are only four matches, then the tile must be a corner tile.
    """
    tiles = read_file(file)
    possible_edges = dict.fromkeys(tiles.keys(), [])
    for key, tile in tiles.items():
        tile_edges = [
            tile[0],
            tile[-1],
            "".join([i[0] for i in tile]),
            "".join([i[-1] for i in tile]),
        ]
        reversed_tile_edges = [i[::-1] for i in tile_edges]
        possible_edges[key] = tile_edges + reversed_tile_edges
    corners = []
    for key, tile_edges in possible_edges.items():
        exclude_tile = {k: v for k, v in possible_edges.items() if k != key}
        compare_edges = []
        for compare_edge in exclude_tile.values():
            compare_edges = compare_edges + compare_edge
        matches = set(compare_edges).intersection(set(tile_edges))
        if len(matches) == 4:
            corners.append(key)
    return reduce(mul, corners, 1)


print(solve_part_1("example.csv"))
print(solve_part_1("data.csv"))


# the method for part 2 is to calculate the likelihood of a sea monster from the example
# and then use that likelihood to guess and check


def remove_borders(file):
    tiles = read_file(file)
    contents = ""
    for tile in tiles.values():
        tile = [i[1:-1] for i in tile]
        tile = tile[1:-1]
        tile = "".join(tile)
        contents = contents + tile
    return contents


example_contents = remove_borders("example.csv")
contents = remove_borders("data.csv")


def find_example_proportion():
    n = len(example_contents)
    n_sea_monsters = 2  # given in the example
    return n_sea_monsters / n


def find_likely_n_sea_monsters():
    n = len(contents)
    example_proportion = find_example_proportion()
    return n * example_proportion


def solve_part_2(contents, n_sea_monsters):
    n_hash = contents.count("#")
    sea_monster_size = 15  # given in the question
    return n_hash - (n_sea_monsters * sea_monster_size)


print(solve_part_2(example_contents, 2))
print(find_likely_n_sea_monsters())
print(solve_part_2(contents, 32))
print(solve_part_2(contents, 33))


# luckily the actual number of sea monsters is only one more than
# that predicted from the likelihood from the example
# so I wasn't guess and checking for long!
