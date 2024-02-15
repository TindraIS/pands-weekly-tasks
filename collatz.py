'''
----------------------------------------------------------------------
Name: collatz.py
Description: 
    - Ask the user to input any positive integer and outputs the successive values of the following calculation.
    - At each step calculate the next value by taking the current value and, if it is even, divide it by two, but 
    if it is odd, multiply it by three and add one.
    - End the program if the current value is one.
Author: Irina Simoes
Date created: 13/02/2024
Version: 1.0
References:
    * https://www.geeksforgeeks.org/python-program-to-check-if-a-number-is-odd-or-even/
    * https://pythonguides.com/python-program-for-even-or-odd/
    * https://sparkbyexamples.com/python/python-print-list-without-brackets/
----------------------------------------------------------------------
''' 
# Ask the user to input a positive integer - look into error handling in case is negative
number = int(input("Please enter a positive integer: "))

# Create an empty array (list) to store the numbers computed in each iteration
# Quite familiarised with using empty arrays in JS to store iterations in API requests
arr = []

# As we are processing a sequence, loop through the rules below until the result becomes 1
while number != 1:
    # Append to the array all computed numbers, the first one being the user input and the remaining ones
    # the result of the rules below
    arr.append(str(number))

    # The modulo operator returns the remainder when divided by any number, so if the result 
    # of (number % 2) is 0 then the number is even otherwise it's an odd number
    # Reference above
    if number % 2 == 0:
        # If number is even we divide it by 2, as per task requirement
        number = number//2

    else:
        # If number is odd we multiply it by 3 and add 1, as per task requirement
        number = number*3+1   

# Loop is finished whevener number = 1, so we add the final 1 to the array
arr.append(str(1))

# To reproduce the output as in the example given by Andrew, use the join() method to combine all the numbers
# into a single string without the brackets
print(" ".join(arr))

        
