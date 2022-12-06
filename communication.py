from file_utils import read_input_file


def main():
    signal = read_input_file("resources/day_6_actual.txt")[0]
    start = find_message(signal)
    print(start)


def find_signal_start(signal):
    buffer = []
    count = 0
    for letter in signal:
        if len(set(buffer)) == 4:
            return count

        if len(buffer) == 4:
            del buffer[0]

        buffer.append(letter)

        count += 1


def find_message(signal):
    buffer = []
    count = 0
    for letter in signal:
        if len(set(buffer)) == 14:
            return count

        if len(buffer) == 14:
            del buffer[0]

        buffer.append(letter)

        count += 1


if __name__ == "__main__":
    main()
