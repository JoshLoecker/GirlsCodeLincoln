# The following is pseudocode and is not meant to be run.
import random

Create a function called 'password_generator' that takes three parameters: length, use_numbers, use_special_characters
    Create a variable called password and set it to an empty string
    Create a for loop that loops 'length' times
        If use_numbers and use_special_characters are both true
            Add a random character from the string "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()" to the password variable
        Else if use_numbers is true
            Add a random character from the string "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890" to the password variable
        Else if use_special_characters is true
            Add a random character from the string "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()" to the password variable
        Else
            Add a random character from the string "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ" to the password variable
    
    Print the following phrase
    print("Your password is: " + password)


Ask the user if they want to use numbers
Ask the user if they want to use special characters
Ask the user how long the password should be
length = input("How long do you want your password to be? ")

Call the 'password_generator' function and pass in the length, use_numbers, and use_special_characters variables
