#######################################################

# Name: accounts.py
# Description: 
    ## Prompts the user to enter a 10 digit account number and reads in
    ## Outputs the account number with only the last 4 digits showing, replacing the first 6 digits with Xs
    ## It is assumed that users' input may not comply with the requested parameter, either because of data type or length
# Author: Irina Simoes
# Date created: 09/02/2024
# Version: 1.0

#######################################################


account_no = input("Please enter a 10 digit account number: ")

# Reference: https://docs.python.org/3/library/stdtypes.html#str.isdigit
if not account_no.isdigit():
    print("Error: Account number contains non-digit characters.")

elif len(account_no) > 10:
    print("Error: Account number contains more than 10 digits.")

elif len(account_no) < 10:
    print("Error: Account number contains less than 10 digits.")

# References: https://docs.python.org/3/library/functions.html#len + https://www.geeksforgeeks.org/python-string-length-len/
else:
    concealed_account_no = 'X' * (len(account_no) - 4) + account_no[-4:]
    print(concealed_account_no)
