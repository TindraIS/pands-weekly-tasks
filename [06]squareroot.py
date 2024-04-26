'''
----------------------------------------------------------------------
Name: squareroot.py
Description: 
    - This program takes a positive floating-point number as input and outputs an approximation of its square root.
    - Formula: root = 0.5 * (X + (N / X)) where X is any guess which can be assumed to be N or 1. 
Author: Irina Simoes
Date created: 09/03/2024
Version: 1.1
References:
    * https://stackoverflow.com/questions/19473770/how-to-avoid-floating-point-errors
    * https://www.geeksforgeeks.org/find-root-of-a-number-using-newtons-method/
    * https://en.wikipedia.org/wiki/Newton%27s_method
    * https://patrickwalls.github.io/mathematicalpython/root-finding/newton/
    * https://realpython.com/python-f-strings/#formatting-strings-with-pythons-f-string
    * https://regex101.com/
----------------------------------------------------------------------
''' 

# Import the regex module to handle the pattern specified in read_number()
import re 

# Define function to read in a positive floating-point number from user input with a default message
def read_number(message = "Please enter a positive floating-point number: "):
    while True:
        # Prompt the user to enter a number and store it in the variable
        user_input = input(message)

        # Verify if the input meets the below conditions:
        # It matches the regex pattern for a positive floating-point number: digits, decimal point, digits
        # It's greater than 0
        if (re.match(r"^\d+\.\d+",user_input) and float(user_input) > 0):
            break # If the above conditions are true break out of the loop
        else: # If conditions are false print an error message
            print("That was not a valid floating-point number.")
    # Once while is false, exit function and return the value stored in user_input, which is converted from str to float so it can be called by sqrt() function
    return float(user_input)  

def sqrt(guessed_sqrt):
    guessed_sqrt = input_value  # Declare variable to store the guessed square root, which starts as the user input
    tolerance_allowed = 0.01 # Declare variable that stores the max difference between the successive guessed square root (number)

    while tolerance_allowed: 
        # Variable that stores Newton method formula
        root_calculation = 0.5 * (guessed_sqrt + (input_value/guessed_sqrt))

        # Check if the difference between the square root guess is within the tolerance
        if (abs(root_calculation-guessed_sqrt) < tolerance_allowed):
            break

        # Re-declare the variable to update with the new guess before the next loop iteration
        guessed_sqrt = root_calculation

    return root_calculation

input_value = read_number()
square_root = sqrt(input_value)

print(f'The square root of {input_value} is approx. {square_root:.2f}')