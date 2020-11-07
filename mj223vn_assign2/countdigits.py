num = input("Enter a large positive integer: ")

zeros = 0
odd = 0
even = 0

for i in range(len(num)):
    if int(num[i]) == 0:
        zeros += 1
    elif int(num[i]) % 2 == 0:
        even += 1
    else:
        odd += 1

print(f"Zeros: {zeros}\nOdd: {odd}\nEven: {even}")
