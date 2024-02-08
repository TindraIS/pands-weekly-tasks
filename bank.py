#######################################################

# Name: bank.py
# Description: 
    ## The program prompts the user and reads in two money amounts (in cent)
    ## Adds the two amounts
    ## Prints out the answer in a human readable format with a € sign and decimal point between the euro and cent of the amount 
# Author: Irina Simoes
# Date created: 04/02/2024
# Version: 3.0

#######################################################


# prompt the user to insert the amounts & nest int() method to convert the string into an integer so that the user's input can be treated as numerical data
    ## as stated in https://www.w3schools.com/python/python_user_input.asp
amount1 = int(input("Please enter amount 1 (in cent): "))
amount2= int(input("Please enter amount 2 (in cent): "))

# sum the amounts and divide the result by 100 to convert the total from cents to euros, as 100 cents make up 1 euro
amounts_sum = (amount1 + amount2)/100

# print the result to the console ensuring its consistency and readbility: 
    # A. format it with the euro symbol with an f-string, which allows for embedding Python expressions inside string constants
        ## Reference: Python String Formatting Best Practices article by Dan Bader published in https://realpython.com/python-string-formatting/
    
    # B. use Python's Format Specification Mini-Language to set commas as thousands separators and 2 decimal points. 
        ## Setting the decimal precision will ensure consistency and uniformity in the output's floating-point values, regardless of users' input.
        ## Without the precision field, depending on how many cents are specified, the result could have either 1 or 2 decimal points 
        ## Formatting numbers with thousands separators will enhance readability when dealing with large numbers, making values more clear an understandable.
        ## Failing to do so will result in having to count digits to grasp the total number. E.g: Output would be €656654.33 instead of €656,654.33 
        ## Reference: Python's Format Mini-Language for Tidy Strings by Leodanis Pozo Ramos published in https://realpython.com/python-format-mini-language/
print(f'The sum of the two amounts is €{amounts_sum:,.2f}')