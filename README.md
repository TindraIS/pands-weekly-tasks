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
    * [05: weekday.py](#05-weekdaypy)
    * [06: squareroot.py](#06-squarerootpy)
    * [07: es.py](#07-espy)
    * [08: plottask.py](#08-plottaskpy)
* [Acknowledgements](#Acknowledgements)

<br>

## Weekly Tasks

### 01: helloworld.py

    Write a program called `helloworld.py` that displays Hello World! when it is run.

---

### 02: bank.py

    When Banks are storing currency figures, they store them as integers (usually in cent). 
    This is to avoid rounding errors. Write a program called `bank.py` The program should:
        * Prompt the user and read in two money amounts (in cent)
        * Add the two amounts
        * Print out the answer in a human readable format with a 
        euro sign and decimal point between the euro and cent of the amount 


##### Rationale

The problem solving approach was mainly based on a [Stack Overflow question](https://stackoverflow.com/questions/71041895/using-floor-division-and-modulo-together), which asked how to find the positive remainder of a floor division without having to perform two different operations. 


##### References
<details>
           <summary>Apart from Stack Overflow, the below resources were used to solve the task:</summary>
           <p>

* https://www.w3schools.com/python/python_user_input.asp
* https://www.w3schools.com/python/python_casting.asp
* https://realpython.com/python-string-formatting/ 
* https://realpython.com/python-format-mini-language/
* https://www.geeksforgeeks.org/python-operators/?ref=lbp 
* https://realpython.com/python-modulo-operator/ 
* https://www.geeksforgeeks.org/how-to-add-leading-zeros-to-a-number-in-python/
* https://docs.python.org/3/library/functions.html#divmod
* https://www.w3schools.com/python/python_tuples_access.asp

    </p>
</details>

<br>

---

### 03: accounts.py

    Bank account numbers can stored as 10 character strings, for security reasons some 
    applications only display the last 4 characters (with the other other characters replaced with Xs).
    Write a python program called `accounts.py` that reads in a 10 character account number and outputs 
    the account number with only the last 4 digits showing (and the first 6 digits replaced with Xs).


##### Rationale
Problem solving approach based on the ```len()``` function article in [Real Python](https://realpython.com/len-python-function/) which contains a few examples with while loops. Having some experience with JS coding on Google products, I was already familiarised with while loops, so the logic came naturally when looking through the documentation of week 3's topics.


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

##### Rationale

The logic for solving this program was based on the references below, even though I already had in mind to use a while loop with an empty array to store all the sucessive iterations.


##### References
<details>
           <summary>The below resources were used to solve the task:</summary>
           <p>

* https://www.geeksforgeeks.org/python-program-to-check-if-a-number-is-odd-or-even/
* https://pythonguides.com/python-program-for-even-or-odd/
* https://sparkbyexamples.com/python/python-print-list-without-brackets/

    </p>
</details>

<br>

---

### 05: weekday.py

    Write a program that outputs whether or not today is a weekday. (The program should be called `weekday.py`)

##### Rationale

I was already familiarised with the datetime module from a personal a personal project, so directly researched the module parameters and wraped the logic in a if statement to verify if the current day matches the days in the weekend list.

##### References
<details>
           <summary>The below resources were used to solve the task:</summary>
           <p>

* https://docs.python.org/3/library/datetime.html
* https://docs.python.org/3/library/datetime.html#datetime.datetime.strftime

    </p>
</details>

<br>

---

### 06: squareroot.py

    Write a program that takes a positive floating-point number as input and outputs an approximation of its square root. You should create a function called <tt>sqrt</tt> that does this.
    
    I am asking you to create your own sqrt function and not to use the built in functions x ** .5 or math.sqrt(x). This is to demonstrate that you can research and code a process (If you really needed the square root you would use one of the above methods). I suggest that you look at the newton method at estimating square roots. 

##### Rationale

In terms of solving the mathematical expression, I mainly used the [Geeks for Geeks article](https://www.geeksforgeeks.org/find-root-of-a-number-using-newtons-method/) as an inspiration and then proceeded to read the other referenced sources to understand the problem itself. As regards as the user input, I thought of different ways of verifying if the user input was valid, but ended up using a simple 'greater than 0' check jointly with  regular expression for the number format, which I'm already familiarised from using bGenius, a management software for marketing campaigns.

##### References
<details>
           <summary>The below resources were used to solve the task:</summary>
           <p>

* https://stackoverflow.com/questions/19473770/how-to-avoid-floating-point-errors
* https://www.geeksforgeeks.org/find-root-of-a-number-using-newtons-method/
* https://en.wikipedia.org/wiki/Newton%27s_method
* https://patrickwalls.github.io/mathematicalpython/root-finding/newton/
* https://realpython.com/python-f-strings/#formatting-strings-with-pythons-f-string
* https://regex101.com/

    </p>
</details>

<br>

---

### 07: es.py

    Write a program that reads in a text file and outputs the number of e's it contains. Think about what is being asked here, document any assumptions you are making.
    
    The program should take the filename from an argument on the command line. I have not shown you how to do this, you need to look it up.

##### Rationale

This was the most fun task for me to do. I have a subscription to [Medium.com](https://medium.com/) and in one of daily digests sent to my email was an article with [26 Python tricks](https://medium.com/codex/26-python-tricks-to-show-off-to-your-colleagues-397587769b4c), one of them being the Wikipedia module, which stayed at the back of my mind waiting for an opportunity to use it. When I read the task brief, immediately thought of integrating the sample code provided in the article.

With regards the command line arguments, that took quite a bit of research, as I had no knowledge of such functionality. Ended up deciding to use argparse over sys.argv as it seemed to provide more options to incorporate the Wikipedia query.

##### References
<details>
           <summary>The below resources were used to solve the task:</summary>
           <p>

* https://medium.com/codex/26-python-tricks-to-show-off-to-your-colleagues-397587769b4c
* https://wikipedia.readthedocs.io/en/latest/code.html#api
* https://docs.python.org/3/tutorial/errors.html
* https://www.w3schools.com/python/python_try_except.asp
* https://docs.python.org/3/library/functions.html#open
* https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
* https://realpython.com/read-write-files-python/
* https://realpython.com/command-line-interfaces-python-argparse/
* https://stackoverflow.com/questions/1009860/how-can-i-read-and-process-parse-command-line-arguments
* https://docs.python.org/3/library/argparse.html
* https://www.geeksforgeeks.org/count-the-number-of-times-a-letter-appears-in-a-text-file-in-python/

    </p>
</details>

<br>

---

### 08: plottask.py

    Write a program called plottask.py that displays:
        * a histogram of a normal distribution of a 1000 values with a mean of 5 and standard deviation of 2,
        * and a plot of the function  h(x)=x3 in the range 0 to 10 on the one set of axes.

##### Rationale

The main inspiration to solve this task was Matplotlib's documentation on [plots with different scales](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/two_scales.html), which details how two different axes can be generated by calling the `Axes.twinx` method. The remaining plots customisation was based on the referenced [cheat sheet](https://s3.amazonaws.com/assets.datacamp.com/blog_assets/Python_Matplotlib_Cheat_Sheet.pdf), combined with Matplotlib's documentation for a better understanding on the required parameters.
 

##### References
<details>
           <summary>The below resources were used to solve the task:</summary>
           <p>

* https://numpy.org/doc/stable/reference/random/generated/numpy.random.normal.html
* https://www.geeksforgeeks.org/python-h_function-function/
* https://s3.amazonaws.com/assets.datacamp.com/blog_assets/Python_Matplotlib_Cheat_Sheet.pdf
* https://matplotlib.org/stable/gallery/subplots_axes_and_figures/two_scales.html
* https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots
* https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/writing-mathematical-expres
* https://matplotlib.org/stable/users/explain/colors/colors.html#sphx-glr-users-explain-colors-colors-py
* https://matplotlib.org/stable/api/markers_api.html#module-matplotlib.markers
* https://matplotlib.org/stable/users/explain/text/annotations.html

    </p>
</details>

<br>

---

## Acknowledgements

This README file was formatted using [GitHub's flavour of MarkDown](https://github.github.com/gfm/) and [MarkDown Guide Basic Synthax](https://www.markdownguide.org/basic-syntax/).