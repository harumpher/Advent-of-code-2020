"""Advent of code 2020 day 24"""


def read_file(file):
    with open(file) as file:
        results = file.readlines()
        results = [line.rstrip() for line in results]
    instructions_list = []
    for result in results:
        instructions = []
        i = 0
        while i < len(result):
            if result[i] in ["n", "s"]:
                direction = result[i : (i + 2)]
                i = i + 2
            else:
                direction = result[i]
                i = i + 1
            instructions.append(direction)
        instructions_list.append(instructions)
    return instructions_list


example = read_file("example.txt")
actual = read_file("input.txt")


# set up grid along three axes: SW to NE, NW to SE, W to E
sw = (0, 1, -1)
ne = (0, -1, 1)
nw = (-1, 0, 1)
se = (1, 0, -1)
w = (-1, 1, 0)
e = (1, -1, 0)


def identify_tiles(instructions_list):
    identified_tiles = []
    for instructions in instructions_list:
        coordinates = (0, 0, 0)
        for direction in instructions:
            moves = globals()[direction]
            coordinates = tuple(
                coordinate + move for coordinate, move in zip(coordinates, moves)
            )
        identified_tiles.append(coordinates)
    return identified_tiles


def find_black_tiles(identified_tiles):
    """if a tile was identified an odd number of times, then it must be black"""
    coordinate_counts = {}
    for coordinates in identified_tiles:
        coordinate_counts[coordinates] = coordinate_counts.get(coordinates, 0) + 1
    black_tiles = []
    for coordinates, count in coordinate_counts.items():
        if count % 2 == 1:
            black_tiles.append(coordinates)
    return black_tiles


example_identified_tiles = identify_tiles(example)
example_black_tiles = find_black_tiles(example_identified_tiles)
print(len(example_black_tiles))

actual_identified_tiles = identify_tiles(actual)
actual_black_tiles = find_black_tiles(actual_identified_tiles)
print(len(actual_black_tiles))


def find_neighbours(coordinates):
    neighbours = []
    directions = ["sw", "ne", "nw", "se", "w", "e"]
    for direction in directions:
        moves = globals()[direction]
        neighbour = tuple(
            coordinate + move for coordinate, move in zip(coordinates, moves)
        )
        neighbours.append(neighbour)
    return neighbours


def find_candidates(black_tiles):
    """candidates to be flipped are the current black tiles and their neighbours"""
    candidates = black_tiles.copy()
    for tile in black_tiles:
        neighbours = find_neighbours(tile)
        for neighbour in neighbours:
            candidates.append(neighbour)
    candidates = list(set(candidates))
    return candidates


def day_flip(initial_black_tiles):
    candidates = find_candidates(initial_black_tiles)
    neighbours_map = {}
    for tile in candidates:
        neighbours_map[tile] = find_neighbours(tile)
    black_neighbours = {}
    for tile, neighbours in neighbours_map.items():
        n_black_neighbours = 0
        for neighbour in neighbours:
            if neighbour in initial_black_tiles:
                n_black_neighbours = n_black_neighbours + 1
        black_neighbours[tile] = n_black_neighbours
    flip_black_to_white = [
        tile
        for tile in initial_black_tiles
        if black_neighbours[tile] == 0 or black_neighbours[tile] > 2
    ]
    flip_white_to_black = [
        tile
        for tile, neighbours in black_neighbours.items()
        if neighbours == 2 and tile not in initial_black_tiles
    ]
    resulting_black_tiles = initial_black_tiles.copy()
    for tile in flip_black_to_white:
        resulting_black_tiles.remove(tile)
    for tile in flip_white_to_black:
        resulting_black_tiles.append(tile)
    return resulting_black_tiles


def n_day_flips(initial_black_tiles, n):
    black_tiles = initial_black_tiles.copy()
    for i in range(n):
        black_tiles = day_flip(black_tiles)
    return black_tiles


print(len(n_day_flips(example_black_tiles, 100)))
print(len(n_day_flips(actual_black_tiles, 100)))
