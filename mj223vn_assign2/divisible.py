numbers = []
for i in range(100, 200):
    if i % 4 == 0 or i % 5 == 0: 
        if i % 4 == 0 and i % 5 == 0:
            continue
        else:
            numbers.append(i)

lineBreaker = 0
for i in range(len(numbers)):
    number = str(numbers[i])
    if lineBreaker == 10:
        print("\n", end="")
        lineBreaker = 0
    print(number + " ", end="")
    lineBreaker += 1
