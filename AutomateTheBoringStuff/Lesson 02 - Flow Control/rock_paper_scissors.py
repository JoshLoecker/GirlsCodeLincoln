# The following input is pseudo code and is not meant to be run as a Python script.

import random

print("Welcome to the game of Rock, Paper, Scissors!")
user_guess = input("Enter a guess (rock, paper, scissors): ")
computer_guess = random.choice(["rock", "paper", "scissors"])

while user_guess not in ["rock", "paper", "scissors"]:
    print("Invalid guess. Please try again.")
    
    Get user input again, the previous input was not correct

Test if the user's input was rock'
    Test if the computer's guess was rock'
        Print a tie message
    Test if the computer's guess was paper'
        Print a lose message
    Test if the computer's guess was scissors'
        Print a win message


Test if the user's input was paper'
    Test if the computer's guess was rock'
        Print a win message
    Test if the computer's guess was paper'
        Print a tie message
    Test if the computer's guess was scissors'
        Print a lose message

Test if the user's input was scissors'
    Test if the computer's guess was rock'
        Print a lose message
    Test if the computer's guess was paper'
        Print a win message
    Test if the computer's guess was scissors'
        Print a tie message
