import os
import traceback
"""
A python script counting number of subdirectories and python files in a specific directory
"""


def count_directories(dir_path):
    """
    Count number of subdirectories

    :param dir_path: path to main directory
    :return: number of subdirectories
    """
    num_of_dir = 0
    try:
        content = os.scandir(dir_path)
        for entity in content:
            if entity.is_dir():
                num_of_dir += 1
    except IOError:
        traceback.print_exc()
        print("Problem when reading path")
    return num_of_dir


def count_py_files(dir_path):
    """
    Count number of python files in a specific directory

    :param dir_path: path to specific directory
    :return: number of python files
    """
    num_of_py_files = 0
    try:
        content = os.listdir(dir_path)
        for entity in content:
            if entity.endswith(".py"):
                num_of_py_files += 1
    except IOError:
        traceback.print_exc()
        print("Problem when reading path")
    return num_of_py_files


path = os.getcwd()
print("Dir Count:", count_directories(path))
print("Py-file Count:", count_py_files(path))