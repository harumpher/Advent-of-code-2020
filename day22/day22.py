"""Advent of code 2020 day 22"""


def read_file(file):
    with open(file) as file:
        result = file.readlines()
        result = [line.rstrip() for line in result]
    result = [int(i) for i in result if i not in ["", "Player 1:", "Player 2:"]]
    n = len(result)
    mid = int(n / 2)
    deck1 = result[:mid]
    deck2 = result[mid:]
    return deck1, deck2


example = read_file("example.txt")
actual = read_file("input.txt")


def score(game_result):
    win = max(game_result, key=len)
    n = len(win)
    vec = list(range(1, n + 1))[::-1]
    return sum(map(lambda x, y: x * y, win, vec))


def compare_cards(card1, card2):
    if card1 > card2:
        return "Player 1 wins"
    else:
        return "Player 2 wins"


def play_game(deck1, deck2):
    while (deck1 != []) and (deck2 != []):
        card1 = deck1[0]
        card2 = deck2[0]
        remaining1 = deck1[1:]
        remaining2 = deck2[1:]
        result = compare_cards(card1, card2)
        if result == "Player 1 wins":
            add1 = [card1, card2]
            add2 = []
        else:
            add1 = []
            add2 = [card2, card1]
        deck1 = remaining1 + add1
        deck2 = remaining2 + add2
    return deck1, deck2


def solve_part_1(decks):
    deck1 = decks[0]
    deck2 = decks[1]
    game_result = play_game(deck1, deck2)
    return score(game_result)


print(solve_part_1(example))
print(solve_part_1(actual))


def play_recursive_game(deck1, deck2):
    previous_decks = []
    while (deck1 != []) and (deck2 != []):
        starting_decks = (deck1, deck2)
        if starting_decks in previous_decks:
            result = "Player 1 wins"
            break
        card1 = deck1[0]
        card2 = deck2[0]
        remaining1 = deck1[1:]
        remaining2 = deck2[1:]
        n1 = len(remaining1)
        n2 = len(remaining2)
        if (n1 >= card1) and (n2 >= card2):
            sub1 = remaining1[:card1]
            sub2 = remaining2[:card2]
            result = play_recursive_game(sub1, sub2)[0]
        else:
            result = compare_cards(card1, card2)
        if result == "Player 1 wins":
            add1 = [card1, card2]
            add2 = []
        else:
            add1 = []
            add2 = [card2, card1]
        deck1 = remaining1 + add1
        deck2 = remaining2 + add2
        previous_decks.append(starting_decks)
    return result, deck1, deck2


def solve_part_2(decks):
    deck1 = decks[0]
    deck2 = decks[1]
    game_result = play_recursive_game(deck1, deck2)[1:]
    return score(game_result)


print(solve_part_2(example))
print(solve_part_2(actual))
