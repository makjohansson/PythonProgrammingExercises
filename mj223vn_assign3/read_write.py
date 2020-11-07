import os
"""
A python script reading and then copying a file
"""


def read_file(file_path):
    """
    Reads a file and returning it as a str list

    :param file_path: path to file to read
    :return: file as a list of type str
    :except IOError
    """
    lines = []
    try:
        with open(file_path, "r") as file:
            for line in file:
                lines.append(line)
    except IOError as e:
        print(e)

    return lines


def write_file(lines, file_path):
    """
    Takes a str list and write that list to a file

    :param lines: list to write to file
    :param file_path: path to where the file will be written
    :except IOError
    """
    try:
        with open(file_path, "w") as file:
            for line in lines:
                file.write(line)
    except IOError as e:
        print(e)


path_to_read = os.getcwd() + "/the_road"
path_to_write = os.getcwd() + "/the_road_copy"

text_file = read_file(path_to_read)
write_file(text_file, path_to_write)

