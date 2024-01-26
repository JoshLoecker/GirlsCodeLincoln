"""
Create a Mad Libs program that reads in text files and lets the user add their own text anywhere
    the word ADJECTIVE, NOUN, ADVERB, or VERB appears in the text file. For example, a text file may look like this:

The ADJECTIVE panda walked to the NOUN and then VERB. A nearby NOUN was unaffected by these events.

The program would find these occurrences and prompt the user to replace them.

The following text file would then be created:
The silly panda walked to the chandelier and then screamed. A nearby pickup truck was unaffected by these events.


The results should be printed to the screen and saved to a new text file
"""

import re

# Open the file
mad_libs_file = open('mad_libs.txt', 'r')
# Read the file
mad_libs_text = mad_libs_file.read()
# Close the file
mad_libs_file.close()

# Create a regex for the words to be replaced
regex = re.compile(r'ADJECTIVE|NOUN|ADVERB|VERB')

# Find all the matches
matches = regex.findall(mad_libs_text)

# Loop through the matches
for match in matches:
    # Prompt the user to replace the match
    replacement = input('Enter a ' + match.lower() + ': ')
    # Replace the match with the user input
    mad_libs_text = regex.sub(replacement, mad_libs_text, 1)

# Print the results
print(mad_libs_text)

# Open a new file
new_file = open('new_mad_libs.txt', 'w')
# Write the results to the new file
new_file.write(mad_libs_text)
# Close the new file
new_file.close()
