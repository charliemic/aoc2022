def read_input_file(filename):
    lines = []
    with open(filename) as file:
        for line in file:
            lines.append(line)
    return lines
