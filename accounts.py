'''
----------------------------------------------------------------------
Name: accounts.py
Description: 
    - Prompts the user to enter a 10 digit account number and reads in.
    - Outputs the account number with only the last 4 digits showing, replacing the first 6 digits with Xs.
    - It is assumed that account numbers can only have 10 digits and that users' input may not comply with 
    such parameters, either because of type or length.
Author: Irina Simoes
Date created: 09/02/2024
Version: 2.0
References:
    * https://realpython.com/len-python-function/
    * https://docs.python.org/3/library/stdtypes.html#str.isdigit
    * https://www.w3schools.com/python/python_tuples_access.asp
    * https://www.w3schools.com/python/python_strings_escape.asp
    * https://realpython.com/python-while-loop/ 
    * https://realpython.com/python-strings/
    * https://docs.python.org/3/library/functions.html#len   
    * https://www.w3schools.com/python/python_strings_slicing.asp
----------------------------------------------------------------------
''' 

# With a while loop we repeatedly prompt the user to enter a 10 digit account no. until a valid input is provided
while True:
    # Keeping the input() function within the while loop allows an indefinite iteration until the account no. conditions are met:
        # the input should only contain digits -> checked with isdigit()
        # account no. shouldn't have more than 10 characters -> checked wioth len()
    # To avoid asking users to enter a valid account no. multiple times, a normalisation is computed:
        # .strip() method removes any leading or trailing whitespaces
        # .replace() method removes any remaining whitespace characters within the string
    account_no = input("Please enter a 10-digit account number: ").strip().replace(" ", "")

    if account_no.isdigit() and len(account_no) == 10:
    # If a valid input is provided, the first 6 digits are replaced with Xs and the concealed account no. is displayed
        concealed_account_no = 'X' * 6 + account_no[-4:]
        print("Concealed account number:", concealed_account_no)
        # The break statement is then used to exit the loop & finish the program, as the rest of the code won't apply
        break

    # If the provided account no. isn't valid, check if any of the below conditions are met and give instructions on how to fix the error
    elif not account_no.isdigit():
        print("Error: Account number contains non-digit characters.")

    elif len(account_no) > 10:
        print("Error: Account number contains more than 10 digits.")

    elif len(account_no) < 10:
        print("Error: Account number contains less than 10 digits.")
    
    elif len(account_no) == 0:
        print("Error: Account number field is empty.")

    # If the account no. isn't valid because of a constraint other than the ones specified above, a generic message is displayed
    else:
        print("Error: Please enter a valid 10-digit account number.")
