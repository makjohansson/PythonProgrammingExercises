import math as m
#A program that compute the area of a cirle using radius.
PI = m.pi
radius = float(input("Provide radius: "))
area = PI * m.pow(radius, 2)
print("Corresponding area is:", round(area, 1))