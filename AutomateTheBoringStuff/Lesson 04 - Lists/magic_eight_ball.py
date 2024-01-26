# The following is pseudocode and is not meant to be run as a program

# Import the random module
import random

# Create a list named "messages" with predefined strings
messages = ['It is certain', 'It is decidedly so', 'Yes definitely', 'Reply hazy try again', 'Ask again later',
            'Concentrate and ask again', 'My reply is no', 'Outlook not so good', 'Very doubtful']


Create a function called "get_random_message"
    # Use random.randint to generate a random index within the range of the list
    random_index = random.randint(0, len(messages) - 1)
    Return messages at the random_index position

Use the input function to get user input for the question

Get a random message from the get_random_message function

Print the randomly selected message to the screen
