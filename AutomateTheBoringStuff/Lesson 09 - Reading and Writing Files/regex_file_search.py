# The following is pseudocode and is not meant to be run

import os
import re

Create a new variable called 'folder_path' that accepts a folder path from the user

Create a new variable called 'regex' that asks the user for a regex

# Compile the regex
regex = re.compile(regex)

# Loop through the files in the folder
for each file in 'os.listdir(folder_path)':
    Check if the file '.endswith(".txt")', and if so:
        Create the file path: 'os.path.join(folder_path, file)'
        Open the file
        for each line in the file:
            Check if the line matches the regex
            If it does, print the line
            
        Close the file
