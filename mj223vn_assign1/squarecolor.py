letters = "abcdefgh"
squareId = input("Enter a chess square identifier (e.g. e5): ")
letterId, numberId = squareId[0], int(squareId[1])

index = letters.index(letterId) + 1

if numberId % 2 == 0 and index % 2 == 0:
    color = "Black"
elif numberId % 2 != 0 and index % 2 != 0:
    color = "Black"
else:
    color = "White"

print(f"{squareId} is {color}")