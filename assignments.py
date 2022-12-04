from file_utils import read_input_file


def main():
    read_input = read_input_file("resources/day_4_actual.txt")
    sections = parse_input(read_input)
    total = overlapping_ranges(sections)
    print(total)


def parse_input(lines):
    sections = []
    for line in lines:
        line = line.strip("\n")
        sections.append(line.split(",")[0])
        sections.append(line.split(",")[1])
    return sections


def contained_ranges(sections) -> int:
    count = 0
    buffer = ()
    for section in sections:
        lower, upper = section.split("-")
        if buffer:
            if (int(lower) >= int(buffer[0]) and int(upper) <= int(buffer[1])) or (
                int(buffer[0]) >= int(lower) and int(buffer[1]) <= int(upper)
            ):
                count += 1
            buffer = ()
        else:
            buffer = lower, upper
    return count


def overlapping_ranges(sections):
    count = 0
    buffer = ()

    for section in sections:
        lower, upper = section.split("-")
        if buffer:
            buffer_range = set(range(int(buffer[0]), int(buffer[1]) + 1))
            current_range = set(range(int(lower), int(upper) + 1))
            intersection = buffer_range.intersection(current_range)
            if len(intersection):
                count += 1
            buffer = ()
        else:
            buffer = lower, upper
    return count


if __name__ == "__main__":
    main()
