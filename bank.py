'''
------------------------------------------------------------------------------------------------------
Name: bank.py
Description: 
    - While ensure floating-values are not computed due to loss of precision, 
    prompt the user and read in two money amounts (in cent) and add the two amounts.
    - Print out the answer in a human readable format with a € sign and decimal point 
    between the euro and cent of the amount.
    - Problem statement references: 
        * https://realpython.com/python-fractions/
        * https://docs.python.org/3/tutorial/floatingpoint.html
# Author: Irina Simoes
# Date created: 04/02/2024
# Version: 4.0
# References: 
    * https://www.w3schools.com/python/python_user_input.asp
    * https://www.w3schools.com/python/python_casting.asp
    * https://realpython.com/python-string-formatting/ 
    * https://www.geeksforgeeks.org/division-operators-in-python/?ref=lbp
    * https://realpython.com/python-format-mini-language/
    * https://www.geeksforgeeks.org/python-operators/?ref=lbp 
    * https://realpython.com/python-modulo-operator/ 
    * https://www.geeksforgeeks.org/how-to-add-leading-zeros-to-a-number-in-python/
    * https://realpython.com/python-string-formatting/ 
------------------------------------------------------------------------------------------------------
'''

import string


# Prompt the user to insert the amounts and cast the variable into a integer so that the user's input 
# can be treated as numerical data
amount1 = int(input("Please enter amount 1 (in cent): "))
amount2= int(input("Please enter amount 2 (in cent): "))


# Sum the amounts before further processing
amounts_sum = (amount1 + amount2)


# The below code makes use of f'strings which allow Python expressions to be embedded inside string constants. 
# Calculate euros with floor division to ensure the output is an integer:
    # We divide the result by 100 to convert the total from cents to euros, as 100 cents make up 1 euro.
    # The logic is that this operator returns the same type of the argument passed by default and since
    # we have above converted the variable to an integer, the output will be forcibly  be an integer as well. 
# Use Python's Format Specification Mini-Language to set commas as thousands separators: 
    # Formatting numbers with thousands separators will enhance readability when dealing with large numbers, 
    # making values more clear an understandable. Failing to do so will result in having to count digits to 
    # grasp the total number. E.g: Output would be €656654.33 instead of €656,654.33 
euros = f'{(amounts_sum//100):,}'


# Calculate cents with modulus to compute the remainder of amounts_sum:
    # Again we take 100 as our second operator, aas 100 cents make up 1 euro.
    # The result will be the remainder left over the amounts_sum/100 division, ie, cents
# Use Python's Format Specification Mini-Language to set 2 decimal points:
    # Setting the decimal precision will ensure consistency and uniformity in the output's values, adding 
    # a leading zero if the result is <10. Without the precision field, depending on how many cents are 
    # specified, the result could have either 1 or 2 decimal points.
cents = f'{(amounts_sum%100):02d}'


# For security reasons, print the result with a template string, as per Python String Formatting Rule of Thumb
output_template = string.Template('The sum of the two amounts is €${euros}.${cents}')
output = output_template.substitute(euros=euros, cents=cents)
print(output)