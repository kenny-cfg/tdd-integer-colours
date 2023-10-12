def read_file(file_name):
    with open(file_name, 'r') as file:
        return [line.rstrip() for line in file.readlines()]


def increment_line_number(file_name):
    file_contents = read_file(file_name)
    number = int(file_contents.pop().split('.')[0])
    return number + 1