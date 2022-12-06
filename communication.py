from file_utils import read_input_file


def main():
    signal = read_input_file("resources/day_6_actual.txt")[0]
    start = find_message(signal)
    print(start)


def find_signal_start(signal):
    return find_distinct_section(signal, 4)


def find_message(signal):
    return find_distinct_section(signal, 14)


def find_distinct_section(signal, distinct_count):
    buffer = []
    count = 0
    for letter in signal:
        if len(set(buffer)) == distinct_count:
            return count

        if len(buffer) == distinct_count:
            del buffer[0]

        buffer.append(letter)

        count += 1


if __name__ == "__main__":
    main()
