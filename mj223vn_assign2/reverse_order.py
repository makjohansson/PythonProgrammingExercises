counter = 1
user_input = int(input(f"Enter positive integers. End by giving a negative integer\nInteger {counter}: "))
integer_list = []

while user_input > 0:
    counter += 1
    integer_list.append(user_input)
    user_input = int(input(f"Integer {counter}: "))

print(f"\nNumber of positive integers: {counter - 1}\nIn reverse order: {integer_list[::-1]}", )

