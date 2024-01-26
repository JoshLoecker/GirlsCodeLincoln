# The following is pseudocode that is not meant to be run
import re

Collect input from the user telling them to enter a date in the format DD/MM/YYYY

Create a new variable called 'date_search' equal to a regex search to search for a date in the format DD/MM/YYYY
Use the regex: r"(\d\d)/(\d\d)/(\d\d\d\d)"

While the length of 'date_search.groups()' is not equal to 3:
    Collect input from the user telling them to enter a date in the format DD/MM/YYYY
    Create a new variable called 'date_search' equal to a regex search to search for a date in the format DD/MM/YYYY

Create a new variable called 'day' equal to the first group of 'date_search'
Create a new variable called 'month' equal to the second group of 'date_search'
Create a new variable called 'year' equal to the third group of 'date_search'

Convert 'day', 'month', and 'year' to integers

If 'month' is equal to 4, 6, 9, or 11:
    If 'day' is greater than 30:
        Print "Invalid date"
Else if 'month' is equal to 2:
    If 'year' is divisible by 4:
        If 'day' is greater than 29:
            Print "Invalid date"
    Else:
        If 'day' is greater than 28:
            Print "Invalid date"
Else:
    If 'day' is greater than 31:
        Print "Invalid date"
