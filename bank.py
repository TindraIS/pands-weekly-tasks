#######################################################

# Name: bank.py
# Description: 
    ## The program prompts the user and reads in two money amounts (in cent)
    ## Adds the two amounts
    ## Prints out the answer in a human readable format with a euro sign and decimal point between the euro and cent of the amount 
# Author: Irina Simoes
# Version: 1.0
# Date: 04/02/2024

#######################################################



# prompt the user to insert first amount & nest variable with int() method to convert string into integer
amount1 = int(input("Please enter amount 1 (in cent): "))

# nest float() to get the floating point value, divide amount1 by 100 to convert from cents to euros, and use an f-string formatting to display the amount with two decimal places
amount1_float = float(f'{amount1/100:.2f}')
print(amount1_float)

# prompt the user to insert second amount & nest variable with int() method to convert string into integer
amount2= int(input("Please enter amount 2 (in cent): "))

# nest float() to get the floating point value, divide amount1 by 100 to convert from cents to euros, and use an f-string formatting to display the amount with two decimal places
amount2_float = float(f'{amount2/100:.2f}')

# sum the amounts
amounts_sum = amount1_float + amount2_float

# print the above float number in a human readable format and format it with the euro symbol using an f-string
print(f'The sum of the two amounts is €{amounts_sum}')
