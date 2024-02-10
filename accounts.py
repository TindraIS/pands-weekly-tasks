'''
----------------------------------------------------------------------
Name: accounts.py
Description: 
    - Prompts the user to enter a 10 digit account number and reads in.
    - Outputs the account number with only the last 4 digits showing, replacing the first 6 digits with Xs.
    - It is assumed that account numbers can only have 10 digits and that users' input may not comply with 
    such parameters, either because of type or length.
# Author: Irina Simoes
# Date created: 09/02/2024
# Version: 1.0
# References:
    *
----------------------------------------------------------------------
'''

# Normalising the output by:
    ## Using .strip() method to remove any leadingor trailing whitespaces
    ## Using .replace() method to remove any remaining whitespace characters within the string
account_no = input("Please enter a 10 digit account number: ").strip().replace(" ","")

# References: 
    ## https://realpython.com/python-strings/
    ## https://docs.python.org/3/library/functions.html#len  
concealed_account_no = 'X' * (len(account_no) - 4) + account_no[-4:]

# Reference: https://docs.python.org/3/library/stdtypes.html#str.isdigit
if account_no.isdigit() and len(account_no) == 10:
    print(concealed_account_no)

elif not account_no.isdigit():
    print("Error: Account number contains non-digit characters.")

elif len(account_no) > 10:
    print("Error: Account number contains more than 10 digits.")

elif len(account_no) < 10:
    print("Error: Account number contains less than 10 digits.")

# References: https://www.w3schools.com/python/python_strings_slicing.asp

    
    










