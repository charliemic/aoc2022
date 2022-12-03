from file_utils import read_input_file

LETTERS = "abcdefghijklmnopqrstuvwxyz"


def main():
    rucksacks = read_input_file("resources/day_3_examples.txt")
    common = find_common_item_in_rucksacks(rucksacks)
    total = sum_items(common)
    print(total)


def halve(input_string):
    half = int(len(input_string) / 2)
    return input_string[: -(half + 1)], input_string[half:]


def common_letters(comparator_x, comparator_y) -> list:
    non_unique = [letter for letter in comparator_x if letter in comparator_y]
    return list(set(non_unique))


def assign_value() -> dict:
    letters = {}
    for index, letter in enumerate(LETTERS):
        letters[letter] = index + 1
        letters[letter.upper()] = index + 27
    return letters


def find_common_item_in_rucksacks(rucksacks):
    sacks = []
    for rucksack in rucksacks:
        first, second = halve(rucksack)
        sacks.append(common_letters(first, second))
    return sacks


def score(item):
    lookup = assign_value()
    return lookup[item]


def sum_items(common_items):
    total = 0
    for rucksack in common_items:
        for item in rucksack:
            total += score(item)
    return total


if __name__ == "__main__":
    main()
