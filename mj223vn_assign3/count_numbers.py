import os
from integer_file_to_list import integer_file_to_list
"""
A python script that computes and presents the number of different integers and
computes and presents the most frequently occurring number in a text file containing integers
"""


def count_different(lst):
    """Compute the number of different integers

    :param lst: list to use for computation
    """
    return len(set(lst))


def count_occurrences(lst):
    """Computes and presents the most frequently occurring number in a list

    :param lst: list to use for computation
    """
    lst_as_set = set(lst)
    return_dict = {}
    for key in lst_as_set:
        return_dict[key] = lst.count(key)
    return return_dict
    

path_a = os.getcwd() + "/10000_integers/file_10000integers_A.txt"
path_b = os.getcwd() + "/10000_integers/file_10000integers_B.txt"

int_list_a = integer_file_to_list(path_a).file_to_int_list()
int_list_b = integer_file_to_list(path_b).file_to_int_list()

print(f"File A contains {count_different(int_list_a)} different integers")
print(f"File B contains {count_different(int_list_b)} different integers")

dict_a = count_occurrences(int_list_a)
dict_b = count_occurrences(int_list_b)

most_occurring_number_dict_a = max(dict_a, key=dict_a.get)
most_occurring_number_dict_b = max(dict_b, key=dict_b.get)

print(f"\nThe most frequently occurring number in File A is "
      f"{most_occurring_number_dict_a}, it occurs {dict_a[most_occurring_number_dict_a]} times")

print(f"The most frequently occurring number in File B is "
      f"{most_occurring_number_dict_b}, it occurs {dict_b[most_occurring_number_dict_b]} times")
