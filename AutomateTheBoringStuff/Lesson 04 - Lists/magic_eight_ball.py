"""
Using lists and the “random” module, we can create a Magic 8 Ball program
Create a list named “messages” with the following strings in it
'It is certain', 'It is decidedly so', 'Yes definitely', 'Reply hazy try again', 'Ask again later', 'Concentrate and ask again', 'My reply is no', 'Outlook not so good', 'Very doubtful'

Tell the user to ask a question, then pick a random string from the list and print it to the screen

Hints
You will need to import the “random” module at the top of the program
random.randint(0, len(messages) - 1) will select a random message from the list (as will random.choice(messages))
Creating a function to pick a random message may be helpful, but not required
"""

# Import the random module
import random

# Create a list named "messages" with predefined strings
messages = ['It is certain', 'It is decidedly so', 'Yes definitely', 'Reply hazy try again', 'Ask again later',
            'Concentrate and ask again', 'My reply is no', 'Outlook not so good', 'Very doubtful']


# Define a function to get a random message from the list
def get_random_message():
    # Use random.randint to generate a random index within the range of the list
    random_index = random.randint(0, len(messages) - 1)
    # Return the randomly selected message
    return messages[random_index]


# Get user input for the question
question = input("Ask a question: ")

# Call the get_random_message function to get a random message
random_message = get_random_message()

# Print the randomly selected message to the screen
print(random_message)
