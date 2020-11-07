import random


def random_list(n):
    list_to_return = []
    for i in range(n):
        random_int = random.randint(1, 100)
        list_to_return.append(random_int)
    return list_to_return


def average(lst):
    avg = sum(lst) / float(len(lst))
    return int(round(avg, 0))


def only_odd(lst):
    only_odd_values = []
    for value in lst:
        if not value % 2 == 0:
            only_odd_values.append(value)
    return only_odd_values


def to_string(lst):
    return_string = "\"["
    for value in lst:
        if value == lst[-1]:
            return_string += str(value) + "]\""
        else:
            return_string += str(value) + ", "
    return return_string


def contains(lst, a, b):
    a_b_following = False
    for i in range(len(lst) - 1):
        if lst[i] == a and lst[i + 1] == b:
            a_b_following = True
    return a_b_following


def has_duplicates(lst):
    list_as_set = set(lst)
    return len(lst) != len(list_as_set)


