#######################################################

# Name: bank.py
# Description: 
    ## The program prompts the user and reads in two money amounts (in cent)
    ## Adds the two amounts
    ## Prints out the answer in a human readable format with a euro sign and decimal point between the euro and cent of the amount 
# Author: Irina Simoes
# Date created: 04/02/2024
# Version: 3.0

#######################################################


# prompt the user to insert the amounts & nest int() method to convert the string into an integer so that the user's input can be treated as numerical data
    # as stated in https://www.w3schools.com/python/python_user_input.asp
amount1 = int(input("Please enter amount 1 (in cent): "))
amount2= int(input("Please enter amount 2 (in cent): "))

# sum the amounts and divide the result by 100 to convert the total from cents to euros, as 100 cents make up 1 euro
amounts_sum = (amount1 + amount2)/100

# print the result to the console and format it with the euro symbol using an f-string, which allows for embedding Python expressions inside string constants
    # as explained in Python String Formatting Best Practices article by Dan Bader published in https://realpython.com/python-string-formatting/
print(f'The sum of the two amounts is €{amounts_sum}')
