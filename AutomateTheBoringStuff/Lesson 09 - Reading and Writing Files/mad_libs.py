# The following is pseudocode and is not meant to be run
import re

# Open, read, and then close the mad_libs.txt file
mad_libs_file = open('mad_libs.txt', 'r')
mad_libs_text = mad_libs_file.read()
mad_libs_file.close()

# Create a regex for the words to be replaced
regex = re.compile(r'ADJECTIVE|NOUN|ADVERB|VERB')

# Find all the matches
matches = regex.findall(mad_libs_text)

# Loop through the matches
for each match in the 'matches' list:
    ask the user what to replace the match with. Make sure to include the match in the prompt
    replace the match with the user input using the following code
    mad_libs_text = regex.sub(replacement, mad_libs_text, 1)

# Print the results
print(mad_libs_text)

# Open a new file to write to
new_file = open('new_mad_libs.txt', 'w')
# Write the results to the new file
new_file.write(mad_libs_text)
# Close the new file
new_file.close()
