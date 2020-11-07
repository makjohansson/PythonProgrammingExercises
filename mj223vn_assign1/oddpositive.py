import random

randomNumber = random.randint(-10,10)

oddOrEven = "even" if randomNumber % 2 == 0 else "odd"
positiveOrNegative = "positive" if randomNumber >= 0 else "negative"

print(f"{randomNumber} is {oddOrEven} and {positiveOrNegative}")