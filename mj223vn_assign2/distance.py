import math as m

def distance(x1,y1,x2,y2):
    distance = m.sqrt(m.pow(x1 - x2, 2) + m.pow(y1 - y2, 2))
    return distance

x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

theDistance = round(distance(x1,y1,x2,y2), 3)

print(f"The distance between ({x1},{y1}) and ({x2},{y2}) is {theDistance}")