import math
import os
from integer_file_to_list import integer_file_to_list
"""
A python script reading a two files containing integers
and for each file computes and presents the average value and the standard deviation
"""


def mean(int_list):
    """
    Computes the mean value

    :param int_list: list of integers
    :return: mean value
    """
    if len(int_list) > 0:
        return sum(int_list) / len(int_list)


def variation(int_list):
    """
    Computes the variation

    :param int_list: list of integers
    :return: variation value
    """
    return sum((number - mean(int_list)) ** 2 for number in int_list) / len(int_list)


def std(int_list):
    """
    Computes the standard deviation

    :param int_list: list of integers
    :return: standard deviation value
    """
    return math.sqrt(variation(int_list))


def print_result(letter, mean_value, std_value):
    """
    Print the results in the terminal

    :param letter: A or B for the two different files
    :param mean_value: mean value for file
    :param std_value: standard deviation value for file
    """
    print(f"Average of the integers in file {letter} is: {mean_value} "
          f"and the standard deviation for file {letter} is {std_value} ")


def file_mean_and_std(file_path):
    """
    Computes the mean and std

    :param file_path: path to file
    :return: mean and std values rounded to 2 decimals
    """
    int_list = integer_file_to_list(file_path).file_to_int_list()
    return round(mean(int_list), 2), round(std(int_list), 2)


path_a = os.getcwd() + "/10000_integers/file_10000integers_A.txt"
path_b = os.getcwd() + "/10000_integers/file_10000integers_B.txt"

mean_a, std_a = file_mean_and_std(path_a)
mean_b, std_b = file_mean_and_std(path_b)

print_result("A", mean_a, std_a)
print_result("B", mean_b, std_b)
