n = int(input("Enter a positive integer: "))
k = 1
summary = 1
if n <= 0:
    print("Input must be a positive integer")
else:
    while summary < n:
        k = k + 2
        summary += k

    print(f"{k} is the smallest k such 1+3+5+7+...+k >= {n}")
