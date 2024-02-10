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
# Version: 5.0
# References: 
    * https://www.w3schools.com/python/python_user_input.asp
    * https://www.w3schools.com/python/python_casting.asp
    * https://realpython.com/python-string-formatting/ 
    * https://realpython.com/python-format-mini-language/
    * https://www.geeksforgeeks.org/python-operators/?ref=lbp 
    * https://realpython.com/python-modulo-operator/ 
    * https://www.geeksforgeeks.org/how-to-add-leading-zeros-to-a-number-in-python/
    * https://docs.python.org/3/library/functions.html#divmod
    * https://stackoverflow.com/questions/71041895/using-floor-division-and-modulo-together 
    * https://www.w3schools.com/python/python_tuples_access.asp
------------------------------------------------------------------------------------------------------
'''
# Import template class from Python’s built-in string module to print the final result
from string import string

# Prompt the user to insert the amounts and cast the variable into a integer so that the user's input 
# can be treated as numerical data
amount1 = int(input("Please enter amount 1 (in cent): "))
amount2= int(input("Please enter amount 2 (in cent): "))

# We make use of divmod() built-in function to get the quotient and the remainder of dividing the inputs by 100,
# as 100 cents make up 1 euro. This ensures floating point numbers are not used, even if indirectly.
# The floor division (first element) ouputs the euro value:
    # The logic is that this operator returns the same type of the argument passed by default and since
    # we have above converted the variable to an integer, the output will be forcibly  be an integer as well. 
# The modulus operator (second element) on the other hand computes cents:
    # Again we take 100 as our second operator, as 100 cents make up 1 euro.
    # The result will be the remainder left over the amounts_sum/100 division, ie, the cents total
amounts_sum = divmod((amount1 + amount2), 100)

# The code below makes use of f-strings, allowing Python expressions to be embedded inside string constants.
# We then proceed to store euros and cents in different variables using indexing to access divmod() tuple elements.
# For readability and uniformity, Python's Format Specification Mini-Language is employed to set commas as thousands separators & two decimal points:
    # 1. Formatting numbers with thousands separators enhances readability when dealing with large numbers, 
    # making values clearer and more understandable. Failing to do so will require counting digits to 
    # grasp the total number. For example, the output would be €656,654.33 instead of €656654.33.
    # 2. Setting the decimal precision ensures consistency and uniformity in the output's values, adding 
    # a leading zero if the result is less than 10. Without the precision field, depending on how many cents are 
    # specified, the result could have either one or two decimal points.
euros = f'{(amounts_sum[0]):,}'
cents = f'{(amounts_sum[1]):02}'

# For security reasons, print the result with a template string as per Python String Formatting Rule of Thumb
output_template = string.Template('The sum of the two amounts is €${euros}.${cents}')
output = output_template.substitute(euros=euros, cents=cents)
print(output)