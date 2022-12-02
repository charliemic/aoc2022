from file_utils import read_input_file


def main():
    calorie_list = read_input_file("resources/day_1_actual.txt")
    elves_grouped = group_elves(calorie_list)
    elf_totals = sum_elves(elves_grouped)
    top_3_sum = get_top_three_sum(elf_totals)
    print(top_3_sum)


def group_elves(calorie_list):
    elves = []
    buffer = []
    for line in calorie_list:
        # empty line
        if line == "\n":
            # add group and clear buffer
            elves.append(buffer)
            buffer = []
        else:
            # strip new line char and convert to int
            buffer.append(int(line[:-1]))
    elves.append(buffer)
    return elves


def sum_elves(elves_list):
    totals_list = []
    for elf in elves_list:
        totals_list.append(sum(elf))
    return totals_list


def get_highest_value(input_list):
    return max(input_list)


def get_top_three_sum(input_list):
    sorted_list = sorted(input_list, reverse=True)
    top_3 = [sorted_list[0], sorted_list[1], sorted_list[2]]
    return sum(top_3)


if __name__ == "__main__":
    main()
