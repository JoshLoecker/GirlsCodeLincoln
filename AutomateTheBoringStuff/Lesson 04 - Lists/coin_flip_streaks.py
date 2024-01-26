# The following is pseudocode and is not meant to be run as a program.


import random

Create a variable called "number_of_streams" equal to 0.
# This variable will keep track of the number of streaks of 6 heads or tails in a row.

numberOfStreaks = 0

For each number in the range "range(10000)":
    Create a list called "heads_or_tails"
    For each number in the range "range(100)":
        Append to the list a random integer between 0 and 1.

    Create a variable called "streak" equal to 0.
    for each number in the range "range(len(heads_or_tails) - 1)":
        If the current item in the list is equal to the next item in the list:
            Add 1 to the variable "streak".
        Else:
            Set the variable "streak" equal to 0.
        If the variable "streak" is equal to 6:
            Add 1 to the variable "number_of_streaks".
            Break out of the loop.
