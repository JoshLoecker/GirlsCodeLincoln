# The following is pseudocode and not meant to be run
import re

Create a new function called 'strong_password_detection' that accepts an argument called 'password'
    Check if the length of the password is less than 8
        If so, return False
    Create a regex that checks for uppercase letters
        If the regex search returns None, return False

    Create a regex that checks for lowercase letters
        If the regex search returns None, return False

    Create a regex that checks for digits
        If the regex search returns None, return False

    Return True because the password is strong

Use the following test cases to test your function:
print(strong_password_detection('12345678'))
print(strong_password_detection('12345678a'))
print(strong_password_detection('12345678A'))
print(strong_password_detection('12345678aA'))
