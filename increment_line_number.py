def read_file(file_name):
    with open(file_name, 'r') as file:
        return [line.rstrip() for line in file.readlines()]

def increment_line_number(file_name):
    pass
