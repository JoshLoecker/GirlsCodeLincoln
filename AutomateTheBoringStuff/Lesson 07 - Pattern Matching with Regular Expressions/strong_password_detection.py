"""
Write a function that uses regular expressions to make sure the password string it is passed is strong.

A strong password is defined as one that is at least eight characters long,
    contains both uppercase and lowercase characters,
    and has at least one digit.
    
You may need to test the string against multiple regex patterns to validate its strength.
"""

import re


def strong_password_detection(password):
    # Check password length
    if len(password) < 8:
        return False
    
    # Check for uppercase
    uppercase_regex = re.compile(r'[A-Z]+')
    if uppercase_regex.search(password) is None:
        return False
    
    # Check for lowercase
    lowercase_regex = re.compile(r'[a-z]+')
    if lowercase_regex.search(password) is None:
        return False
    
    # Check for digit
    digit_regex = re.compile(r'\d+')
    if digit_regex.search(password) is None:
        return False
    
    return True


print(strong_password_detection('12345678'))
print(strong_password_detection('12345678a'))
print(strong_password_detection('12345678A'))
print(strong_password_detection('12345678aA'))
