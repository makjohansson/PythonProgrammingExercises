#A program that convert seconds entered by a user to Hours, minutes and seconds.

#Constant values
SECONDS_PER_HOUR = 3600
SECONDS_PER_MINUTE = 60

#Computation of seconds to hours, minutes, seconds
seconds = int(input("Give a number of seconds: "))
hours = seconds // SECONDS_PER_HOUR
seconds %= SECONDS_PER_HOUR
minutes = seconds // SECONDS_PER_MINUTE
seconds %=  SECONDS_PER_MINUTE

print(f"This corresponds to: {hours} hours, {minutes} minutes and {seconds} seconds.")