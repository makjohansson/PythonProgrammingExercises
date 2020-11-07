sizeOfTriangle = int(input("Enter an odd positive integer: "))

if sizeOfTriangle < 0 or sizeOfTriangle % 2 == 0:
    print("Input must be an odd positive integer!!")
else:
    numOfStars = sizeOfTriangle
    numOfiterations = numOfStars
    numOfSpaces = 0
    print("\nRight-Angled Triangle:")
    while numOfiterations > 0:
        for i in range(numOfSpaces):
            print(" ", end="")
        for i in range(numOfStars):
            print("*", end="")
        print()
        numOfiterations -= 1
        numOfStars -= 1
        numOfSpaces += 1
    
    print("\nIsosceles Triangle:")
    numOfiterations = sizeOfTriangle // 2 + 1
    numOfSpaces = sizeOfTriangle // 2
    numOfStars = 1
    while numOfiterations > 0:
        for i in range(numOfSpaces):
            print(" ", end="")
        for i in range(numOfStars):
            print("*", end="")
        print()
        numOfiterations -= 1
        numOfSpaces -= 1
        numOfStars += 2
