'''
----------------------------------------------------------------------
Name: weekday.py
Description: 
    - This program outputs whether or not today is a weekday
Author: Irina Simoes
Date created: 27/02/2024
Version: 1.0
References:
    * https://docs.python.org/3/library/datetime.html
    * https://docs.python.org/3/library/datetime.html#datetime.datetime.strftime

----------------------------------------------------------------------
''' 

# Import datetime module to get today's weekday
# I already knew this mod from previous readings so went straight to python's official documentation
from datetime import date

# Create list of weekend days to compare to today's weekday
weekend = ['Saturday','Sunday']

# Get today's weekday with .today() and format the output to get
# the weekday instead of the date
today = date.today().strftime('%A')

# Commented out print which was used for health check
# print(today)

# Use a for loop to go through the weekend list
for day in weekend:
    if today != day:
        print('Yes, unfortunately today is a weekday.')
        # I know you mentioned you don't like the break statement, 
        # but it's efficient here to get out of the loop on the first True :)
        break
    # If the statement is false and today is in fact one of them days in the weekend list
    else:
        print('It is the weekend, yay!')