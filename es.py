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
    * https://realpython.com/command-line-interfaces-python-argparse/
    * https://stackoverflow.com/questions/1009860/how-can-i-read-and-process-parse-command-line-arguments
    * https://docs.python.org/3/howto/argparse.html
    # https://www.geeksforgeeks.org/count-the-number-of-times-a-letter-appears-in-a-text-file-in-python/
----------------------------------------------------------------------
''' 

import wikipedia as wiki
import os
import argparse

# FUNCTION 1
# Define function that gets the summary text of a given Wikipedia page and saves it in a txt file
def wikipedia_page_to_txt(QUERY, FILENAME):
    # Wrap the code in a try statement in case an error occurs while fetching the Wikipedia page
    try:
        # Declare variable that will store the search query
        search_results = wiki.search(QUERY) 

        # Get the summary of the first result 
        summary = wiki.summary(search_results[1],sentences=10) 
        #print(f'Summary: \n{summary}')
    
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
            #print(f'Wikipedia page about {query}: {FILENAME}')


# FUNCTION 2
# Define function that counts occurrences of letter parsed in cmd line
def count_char(FILENAME, LETTER):
    char = LETTER.lower()       # Convert letter to uppercase as Python is case-sensitive
    total_count = 0             # Initialise counter

    # Open file in reading mode
    with open(FILENAME, "rt", encoding="utf8") as file:
        # Iterate through each character with a for loop
        for line in file:
            total_count += line.lower().count(char) # Again convert line to lowercase and count occurrences of the character parsed in cmd line
    
    print(f'The letter "{LETTER}" appears {total_count} times in {FILENAME}.')


# MAIN CODE
# Initialise the ArgumentParser object, will allows for cmd line arguments to be defined
parser = argparse.ArgumentParser(
    prog="es.py",
    description="This script counts the occurrences of the letter e.",
    epilog="Thanks for using %(prog)s! :)")

# Define arguments
parser.add_argument("-f", "--file", type=str, required=False, help='text file name with extension, eg.: "moby_dick.txt"')
parser.add_argument("-q", "--query", type=str, required=False, help="file's topic which will searched in Wikipedia")
args = parser.parse_args()

# Declare variables 
FILENAME = args.file  # Assign the filename provided in the cmd line to FILENAME
QUERY = args.query    # Assign the query provided in the cmd line to QUERY
LETTER = 'e'          # Define a default letter 

# Wrap functions in -try-except statement
try:
    # Call the Wikipedia function using the parsed arguments
    wikipedia_page_to_txt(QUERY, FILENAME)

    # Call the counter function using the parsed arguments and the default letter
    count_char(FILENAME,LETTER)

except: 
    print('\nERROR: arguments missing.\n')