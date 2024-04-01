'''
----------------------------------------------------------------------
Name: es.py
Description: 
    - This program reads in a text file and outputs the number of e's it contains
    - The program also takes the filename from an argument on the command line. 
Author: Irina Simoes
Date created: 01/04/2024
Version: 1.0
References:
    * https://medium.com/codex/26-python-tricks-to-show-off-to-your-colleagues-397587769b4c
    * https://wikipedia.readthedocs.io/en/latest/code.html#api
    * https://docs.python.org/3/tutorial/errors.html
    * https://www.w3schools.com/python/python_try_except.asp
    * https://docs.python.org/3/library/functions.html#open
    * https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
    * https://realpython.com/read-write-files-python/
----------------------------------------------------------------------
''' 

import wikipedia as wiki
import os
import argparse

# Function 1: define function that gets the summary text of a given Wikipedia page and saves it in a txt file
def wikipedia_page_to_txt(query, FILENAME):
    # Wrap the code in a try statement in case an error occurs while fetching the Wikipedia page
    try:
        # Declare variable that will store the search query
        search_results = wiki.search(query) 

        # Get the summary of the first result 
        summary = wiki.summary(search_results[0]) 
        print(f'Summary: \n{summary}')
    
    # As per Wikipedia Python's library official documentation referenced above, define an exception 
    # block to handle any errors that may occur:
    except wiki.exceptions.DisambiguationError as e:                
        print('DisambiguationError: Multiple options have been found.')
    except wiki.exceptions.HTTPTimeoutError as e:
        print('HTTPTimeoutError: Request to the servers has timed out.')
    except wiki.exceptions.PageError as e:
        print('PageError: No Wikipedia matched a query.')
    except wiki.exceptions.RedirectError as e:
        print('RedirectError: Page title unexpectedly resolved to a redirect.')
    # Finally, use 'Exception' wildcard to catch any other error that may occur
    except Exception as e:
        print("An unknown error occurred:", str(e))

    # Following Python's best practices, the 'else' clause is preferred than adding additional code to the try statement,
    # as it avoids catching an exception than wasn't actually raised by Wikipedia query code
    else:
        # Use open() function in write ('w') mode to create the txt file jointly with 'with' keyword,
        # so that the file is properly closed after the program finishes.
        # According to Python's official documention, encoding is recommended 
        # whenever we're using a text mode, otherwise te default encoding is platform dependent. 
        # "utf-8" is specified as it's the modern de-facto standard.
        with open(FILENAME, 'w', encoding='utf-8') as writer:
            writer.write(summary)
            print(f'Wikipedia page about {query}: {FILENAME}')

# Function 2: define function that gets the summary text of a given Wikipedia page and saves it in a txt file
def move_txt_directory():

# Function 3: define function to count the occurrences of the letter 'e' in a txt file
def count_letter_e(FILENAME):


# Main code
FILENAME = 'python_programming_language.txt'
query = 'python programming language'

wikipedia_page_to_txt(query, FILENAME)
