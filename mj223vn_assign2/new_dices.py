import random

result = {
    "2": 0,
    "3": 0,
    "4": 0,
    "5": 0,
    "6": 0,
    "7": 0,
    "8": 0,
    "9": 0,
    "10": 0,
    "11": 0,
    "12": 0    
}
for i in range(0, 10000):
    dice_one = random.randint(1, 6)
    dice_two = random.randint(1, 6)
    sum_dices = str(dice_one + dice_two)
    result[sum_dices] += 1

print("Frequency table (sum,count) for rolling two dices 10000 times")
for key, value in result.items():
    print(key, "\t\t", value)

