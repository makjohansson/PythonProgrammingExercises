n = int(input("Enter a positive integer: "))
k = 0
summary = 0
if n <= 0:
    print("Input must be a positive integer")
else:
    while summary < n:
        k += 2
        summary += k
        
    k -= 2
    print(f"{k} is the smallest k such 0+2+4+6+...+k < {n}")