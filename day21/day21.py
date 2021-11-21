"""Advent of code 2020 day 21"""


def read_file(file):
    with open(file) as file:
        result = file.readlines()
        result = [line.rstrip() for line in result]
    return result


example = read_file("example.txt")
actual = read_file("input.txt")


def get_ingredients(food_list):
    return [i.split("(")[0][:-1].split() for i in food_list]


def get_allergens(food_list):
    return [i.split("contains ")[1][:-1].replace(",", "").split() for i in food_list]


def flatten_list(initial_list):
    return [i for j in initial_list for i in j]


def map_allergens_to_ingredients(food_list):
    allergens_list = get_allergens(food_list)
    ingredients_list = get_ingredients(food_list)
    allergens_to_ingredients = {
        allergen: {} for allergen in flatten_list(allergens_list)
    }
    for allergen in allergens_to_ingredients.keys():
        ingredients = []
        for i in range(len(allergens_list)):
            if allergen in allergens_list[i]:
                ingredients.append(set(ingredients_list[i]))
        allergens_to_ingredients[allergen] = ingredients
    for allergen, ingredients in allergens_to_ingredients.items():
        allergens_to_ingredients[allergen] = set.intersection(*ingredients)
    return allergens_to_ingredients


def find_inert_ingredients(food_list):
    ingredients = set(flatten_list(get_ingredients(food_list)))
    allergens_to_ingredients = map_allergens_to_ingredients(food_list)
    allergen_ingredients = set.union(*list(allergens_to_ingredients.values()))
    inert_ingredients = list(ingredients - allergen_ingredients)
    return inert_ingredients


def solve_part_1(food_list):
    ingredients = flatten_list(get_ingredients(food_list))
    inert_ingredients = find_inert_ingredients(food_list)
    n_inert_ingredients = 0
    for ingredient in inert_ingredients:
        n = ingredients.count(ingredient)
        n_inert_ingredients = n_inert_ingredients + n
    return n_inert_ingredients


print(solve_part_1(example))
print(solve_part_1(actual))


def map_allergens_to_ingredient(food_list):
    allergens_to_ingredient = map_allergens_to_ingredients(food_list)
    ingredients_to_assign = set(flatten_list(get_ingredients(food_list))) - set(
        find_inert_ingredients(food_list)
    )
    while ingredients_to_assign != set():
        for allergen in allergens_to_ingredient.keys():
            ingredient = allergens_to_ingredient[allergen]
            if len(ingredient) == 1:
                allergens_to_ingredient = {
                    key: ((value - ingredient) if key != allergen else value)
                    for key, value in allergens_to_ingredient.items()
                }
                ingredients_to_assign = ingredients_to_assign - ingredient
    allergens_to_ingredient = {
        key: list(value)[0] for key, value in allergens_to_ingredient.items()
    }
    return allergens_to_ingredient


def solve_part_2(food_list):
    allergens_to_ingredient = map_allergens_to_ingredient(food_list)
    allergens_to_ingredient_sorted = dict(sorted(allergens_to_ingredient.items()))
    canonical_dangerous_ingredient_list = ",".join(
        list(allergens_to_ingredient_sorted.values())
    )
    return canonical_dangerous_ingredient_list


print(solve_part_2(example))
print(solve_part_2(actual))
