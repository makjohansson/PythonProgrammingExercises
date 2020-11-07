def is_positive_and_odd(n):
    if n > 0 and n % 2 != 0:
        return True
    else:
        return False

positiveAndOdd = False
rounds = 0
while not positiveAndOdd and rounds < 5:
    n = int(input("Enter a positive and odd integer: "))
    positiveAndOdd = is_positive_and_odd(n)
    rounds += 1


if rounds < 5:
    print("Nice you could do it, your input was", n)
else:
    print("This was apparently to hard for you")