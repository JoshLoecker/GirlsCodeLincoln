import random


def password_generator(length, use_numbers, use_special_characters):
    password = ""
    for i in range(length):
        if use_numbers and use_special_characters:
            password += random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()")
        elif use_numbers:
            password += random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890")
        elif use_special_characters:
            password += random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()")
        else:
            password += random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
    print("Your password is: " + password)


use_numbers = input("Do you want to use numbers? (y/n) ")
while use_numbers.lower() != "y" or use_numbers.lower() != "n":
    use_numbers = input("Do you want to use numbers? (y/n) ")
use_numbers = use_numbers.lower()
if use_numbers == "y":
    use_numbers = True
else:
    use_numbers = False

use_special_characters = input("Do you want to use special characters? (y/n) ")
while use_special_characters.lower() != "y" or use_special_characters.lower() != "n":
    use_special_characters = input("Do you want to use special characters? (y/n) ")
use_special_characters = use_special_characters.lower()
if use_special_characters == "y":
    use_special_characters = True
else:
    use_special_characters = False

length = input("How long do you want your password to be? ")
while not length.isdigit():
    length = input("How long do you want your password to be? ")

password_generator(length, use_numbers, use_special_characters)
