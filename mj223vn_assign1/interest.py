#A program that calculate the amount on a savings account. The user provides the initial savings and then the
# interest rate in percentages. The output is the amount on the account after five years. 
savings = float(input("Initial savings: "))

R = float(input("Interest rate (in percentages): ")) / 100

for i in range(5):
    savings += savings * R

savings = int(round(savings, 0))
print("\nThe value of your savings after 5 years is: ", savings)