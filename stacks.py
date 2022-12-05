from file_utils import read_input_file

NUMBERS = "123456789"


def main():
    read_input = read_input_file("resources/day_5_actual.txt")
    model = model_stacks(read_input)
    model = reverse_stacks(model)

    commands = get_command_list(read_input)

    for command in commands:
        model = move(model, command)

    message = ""
    for stack in model:
        message += model[stack][-1]

    print(model)
    print(message)


def model_stacks(input_data):
    stacks = {}
    for line in input_data:
        width = len(line)
        if line[5] in NUMBERS:
            return stacks
        for i in range(0, (width // 4)):
            stack = i + 1
            entry = line[(i * 4) + 1]
            if stack not in stacks.keys():
                stacks[stack] = []
            if not entry == " ":
                stacks[stack].append(entry)


def reverse_stacks(stacks):
    for stack in stacks:
        stacks[stack].reverse()
    return stacks


def move(stacks, command):
    words = command.split(" ")
    quantity = int(words[1])
    source = int(words[3])
    destination = int(words[5])
    buffer = []

    for item in range(0, quantity):
        reverse_index = len(stacks[source]) - (quantity - item)
        buffer.append(stacks[source].pop(reverse_index))

    stacks[destination].extend(buffer)

    return stacks


def get_command_list(input_data):
    commands = []
    for line in input_data:
        if line.startswith("move"):
            commands.append(line)
    return commands


if __name__ == "__main__":
    main()
