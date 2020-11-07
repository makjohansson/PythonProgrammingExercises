import os
"""
A python script counting all the non-empty lines in all python files written in the 
course 1DV501
"""


def is_py_file(entity):
    """
    Check if file is a python file

    :param entity: a file
    :return: true if file is python file
    """
    return entity.name.endswith(".py")


def line_counter(file_path):
    """
    Counts number of non blank lines in a python file

    :param file_path: path to file
    :return: amount of non blank lines
    """
    non_blank_line = 0
    try:
        with open(file_path) as file:
            for line in file:
                if line.strip():
                    non_blank_line += 1
            return non_blank_line
    except IOError as e:
        print(e)


def count_py_lines(file_path):
    """
    Count number of non-empty lines in python files in Starting directory and subdirectories
    
    :param file_path:  path to file
    :return: amount of non-empty lines
    """
    path_content = os.scandir(file_path)
    counter = 0
    for file in path_content:
        if is_py_file(file):
            counter += line_counter(file)
        if file.is_dir() and not file.name.startswith("."):
            sub_dir = os.scandir(file.path)
            for the_file in sub_dir:
                if is_py_file(the_file):
                    counter += line_counter(the_file)
    return counter


path = "/Users/marcus/own_projects/1DV501"


print("Python Line Count:", count_py_lines(path))




