import random

numOfInts = int(input("Enter number of integers to be generated: "))
if numOfInts < 0:
    print("The input integer must be positive")
else:
    values = ""
    arrOfValues = []
    print(len(arrOfValues))
    for i in range(numOfInts):
        rand = random.randint(1,100)
        arrOfValues.append(rand)
        values += str(rand) + " "
    print("\nGenerated values:", values)
    mean = sum(arrOfValues) / len(arrOfValues)
    smallest = min(arrOfValues)
    largest = max(arrOfValues)
    print(f"Average, min and max are {mean}, {smallest}, and {largest}")