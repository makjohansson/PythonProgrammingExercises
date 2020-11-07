#A program to simulate a cash register

price = float(input("Price: "))
payment = float(input("Payment: "))

#Calulate the change rounded to nearest integer
change = int(round((payment - price), 0))
print(f"\nChange: {change}kr ")

#Bills back calculation
thousandBills = change // 1000
change -= thousandBills * 1000
fiveHundredBills = change // 500
change -= fiveHundredBills * 500
twoHundredBills =  change // 200
change -= twoHundredBills * 200
oneHundredBills = change // 100
change -= oneHundredBills * 100
fifthyBills = change // 50
change -= fifthyBills * 50
twentyBills = change // 20
change -= twentyBills * 20
tenCoins = change // 10
change -= tenCoins * 10
fiveCoins = change // 5
change -= fiveCoins * 5
twoCoins = change // 2
change -= twoCoins * 2
oneCoins = change 

#Terminal print
print("1000kr bills: ", thousandBills)
print(" 500kr bills: ", fiveHundredBills)
print(" 200kr bills: ", twoHundredBills)
print(" 100kr bills: ",oneHundredBills)
print("  50kr bills: ", fifthyBills)
print("  20kr bills: ", twentyBills)
print("  10kr coins: ", tenCoins)
print("   5kr coins: ", fiveCoins)
print("   2kr coins: ", twoCoins)
print("   1kr coins: ", oneCoins)