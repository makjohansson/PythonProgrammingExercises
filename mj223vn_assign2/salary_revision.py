def median(lst):
    list_sorted = sorted(lst)
    middle_value = (len(list_sorted) + 1) / 2
    if (len(list_sorted) + 1) % 2 == 0:
        return int(round(list_sorted[int(middle_value) - 1], 0))
    else:
        return int(round((list_sorted[int(middle_value) - 1] + list_sorted[int(middle_value)]) / 2, 0))


def average(lst):
    return int(round(sum(lst) / len(lst), 0))


def gap(lst):
    return int(round(max(lst) - min(lst), 0))


user_input = input("Provide salaries (separated by one whitespace): ").split()
salaries = [int(salary) for salary in user_input]

print("Median:", median(salaries))
print("Average:", average(salaries))
print("Gap:", gap(salaries))







