#A program that picks the largest number from three Integers and displays that number 
#to the user
print("Please provide three integers A, B, C.")
A = int(input("Enter A: "))
B = int(input("Enter B: "))
C = int(input("Enter C: "))

largest = 0
if A > B and A > C:
    largest = A
elif B > A and B > C:
    largest = B
else:
    largest = C

print("The largest number is:", largest)