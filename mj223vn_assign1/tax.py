#A program calculating the tax corresponding to the income with three different tax thresholds
income = int(input("Please provide monthly income: "))

thresholdOne = 38000
thresholdTwo = 50000
interval = 12000
taxThresholdOne = 0.3
taxInIntervall = 0.35
taxThresholdTwo = 0.4
tax = 0


if income > thresholdTwo:
    temp = income - thresholdTwo
    tax = temp * taxThresholdTwo
    tax += interval * taxInIntervall
    tax += thresholdOne * taxThresholdOne
elif income <= thresholdTwo and income >= thresholdOne:
    temp = income - thresholdOne
    tax += temp * taxInIntervall
    tax += thresholdOne * taxThresholdOne
else:
    tax = income * taxThresholdOne

print("Corresponding income tax:", int(tax))