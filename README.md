<picture align="center">
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/TindraIS/pands-weekly-tasks/main/Images/readme-header-dark.png">
  <img alt="Pandas Logo" src="https://raw.githubusercontent.com/TindraIS/pands-weekly-tasks/main/Images/readme-header-light.png">
</picture>


###### __This repository contains the solutions for the weekly tasks of Programme & Scripting module @ ATU__


## Table of contents

* [Weekly Tasks](#Weekly-Tasks)
    * [01: helloworld.py](#01-helloworldpy)
    * [02: bank.py](#02-bankpy)
    * [03: accounts.py](#03-accountspy)
    * [04: collatz.py](#04-collatzpy)

<br>

## Weekly Tasks

### 01: helloworld.py

<br>

---

### 02: bank.py

    When Banks are storing currency figures, they store them as integers (usually in cent). 
    This is to avoid rounding errors. Write a program called bank.py The program should:
        * Prompt the user and read in two money amounts (in cent)
        * Add the two amounts
        * Print out the answer in a human readable format with a 
        euro sign and decimal point between the euro and cent of the amount 


##### Rationale

Problem solving approach based on a [Stack Overflow question](https://stackoverflow.com/questions/71041895/using-floor-division-and-modulo-together)


##### References
<details>
           <summary>The below resources were used to solve the task:</summary>
           <p>

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

    </p>
</details>

<br>

---

### 03: accounts.py

    Bank account numbers can stored as 10 character strings, for security reasons some 
    applications only display the last 4 characters (with the other other characters replaced with Xs).
    Write a python program called accounts.py that reads in a 10 character account number and outputs 
    the account number with only the last 4 digits showing (and the first 6 digits replaced with Xs).


##### Rationale
Problem solving approach based on the ```len()``` function article in [Real Python](https://realpython.com/len-python-function/) which contains a few examples with while loops. Having some experience with JS coding, I was already familiarised with while loops, so the logic came naturally when looking through the documentation of week 3's topics.


##### References
<details>
           <summary>The below resources were used to solve the task:</summary>
           <p>
* https://realpython.com/len-python-function/
* https://docs.python.org/3/library/stdtypes.html#str.isdigit
* https://www.w3schools.com/python/python_tuples_access.asp
* https://www.w3schools.com/python/python_strings_escape.asp
* https://realpython.com/python-while-loop/ 
* https://realpython.com/python-strings/
* https://docs.python.org/3/library/functions.html#len   
    </p>
</details>

<br>

---

### 04: collatz.py

    Ask the user to input any positive integer and outputs the successive values of the following calculation.
    At each step calculate the next value by taking the current value and, if it is even, divide it by two, but 
    if it is odd, multiply it by three and add one.
    End the program if the current value is one.
