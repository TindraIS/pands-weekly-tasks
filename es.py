'''
----------------------------------------------------------------------
Name: es.py
Description: 
    - This program reads in a text file and outputs the number of e's it contains
    - The program also takes the filename from an argument on the command line. 
Author: Irina Simoes
Date created: 01/04/2024
Version: 2.0
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
    * https://docs.python.org/3/library/argparse.html
    # https://www.geeksforgeeks.org/count-the-number-of-times-a-letter-appears-in-a-text-file-in-python/
----------------------------------------------------------------------
''' 

import wikipedia as wiki
import os
import argparse


####### FUNCTION 1 #######
# Define function that gets the summary text of a given Wikipedia page and saves it in a txt file
def wikipedia_page_to_txt(QUERY, FILENAME):
    # Wrap the code in a try statement in case an error occurs while fetching the Wikipedia page
    try:
        # Declare container for Wikipedia's search results for the query specified in the cmd line
        search_results = wiki.search(QUERY)
        # While running the program with different queries, I've noticed that some of the pages do not have a summary, 
        # so indexing the first result could potentially throw an error, depending on the query. To address this issue,
        # the program loops through the search results until it finds a page with a summary.
        for result in search_results:
            try:
                summary = wiki.summary(result)
                # If a summary is successfully fetched, break out of the loop
                break
            except wiki.exceptions.PageError:
                # If no summary is available for the result being looped, continue to the next
                continue
        # This else block is computed if no break occurred, indicating no summary was found for the query
        else:
            print(f"No summary available for any search results of '{QUERY}. Please try again with another query'.")
    
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
        '''
        Use open() function in write ('w') mode to create the txt file jointly with 'with' keyword,
        so that the file is properly closed after the program finishes. According to Python's official documention, encoding is 
        recommended whenever we're using a text mode, otherwise te default encoding is platform dependent. "utf-8" is specified 
        as it's the modern de-facto standard.
        '''
        with open(FILENAME, 'w', encoding='utf-8') as writer:
            writer.write(summary)
            #print(f'Wikipedia page about {query}: {FILENAME}')


####### FUNCTION 2 #######
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


####### MAIN CODE #######
'''
Initialise the ArgumentParser object, will allows for cmd line arguments to be defined.
Customise thethe parser by:
    (1) specifying the program name that will be used in the usage message;
    (2) defining a general description for the program and a closing message.
The prog arg can be interpolated into the epilog string using the old-style string formatting operator %.
Given that f-strings replace names with their values as they run, the program will crashwith a NameError.
'''
parser = argparse.ArgumentParser(
    prog="es.py",
    description="This program searches a topic on Wikipedia, saves the summary in a text file, \
    and counts the occurrences of the letter 'e'.",
    epilog="Thanks for using %(prog)s!"
)

'''
Define optional arguments for the filename and the Wikipedia's query with the following params:
    (1) Set long and short form flags;
    (2) Set required to false so that the program don't throw an error if no arguments are provided in the cmd line, 
        but rather handle the error in the below try-except statement;
    (3) Set metavar to empty to clean up the -h message by not showing the uppercase dest values (FILENAME and QUERY);
    (4) Set the helper with a brief description of what the argument does.
'''
parser.add_argument("-f", "--filename", metavar="", required=False, help='required argument that defines the .txt filename, eg.: "moby_dick.txt"')
parser.add_argument("-q", "--query", metavar="", required=False, help="required argument that sets the .txt topic to be searched on Wikipedia, eg: moby dick")
args = parser.parse_args()

# Wrap code in a try-except statement to handle errors in case arguments are not provided in the cmd line
try:
    # Declare constant variables 
    FILENAME = args.filename    # Assign the filename provided in the cmd line to FILENAME using the dot notation on args
    QUERY = args.query          # Assign the query provided in the cmd line to QUERY using the dot notation on args
    LETTER = 'e'                # Define letter 

    # Call the Wikipedia function using the parsed arguments
    wikipedia_page_to_txt(QUERY, FILENAME)

    # Call the counter function using the parsed arguments and the default letter
    count_char(FILENAME,LETTER)

except: 
    # Print a help message, including the program usage and information about the arguments defined with the ArgumentParser
    parser.print_help()