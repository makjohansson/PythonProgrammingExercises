#A program that takes a three digit number as an input and sum the three digits, then displays the sum for the user.

value = input("Provide a three digit number: ")

one = int(value[0])
two = int(value[1])
three = int(value[2])

sum = one + two + three
print("Sum of digits:", sum)