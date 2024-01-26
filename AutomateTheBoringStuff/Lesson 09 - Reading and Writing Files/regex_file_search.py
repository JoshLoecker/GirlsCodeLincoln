"""
Write a program that opens all .txt files in a folder and searches
    for any line that matches a user-supplied regular expression.

The results should be printed to the screen.
"""

import os
import re

# Get the folder path from the user
folder_path = input("Enter the folder path: ")

# Get the regex from the user
regex = input("Enter the regex: ")

# Compile the regex
regex = re.compile(regex)

# Loop through the files in the folder
for file in os.listdir(folder_path):
    # Check if the file is a .txt file
    if file.endswith(".txt"):
        # Open the file
        file_path = os.path.join(folder_path, file)
        file_obj = open(file_path, "r")
        # Loop through the file
        for line in file_obj.readlines():
            # Check if the line matches the regex
            if regex.search(line):
                # Print the line
                print(line)
        # Close the file
        file_obj.close()
