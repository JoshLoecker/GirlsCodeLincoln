"""
Have the computer create a random word and try to guess the word
If a letter is guessed correctly, reveal all locations that letter exists
"""
# The following is pseudocode that is not meant to be run
import random

Create a function called get_valid_guess that accepts an argument called 'guessed_letters'
    Create a new variable called 'valid_guess' and set it to False
    Create a new variable called 'guess' and set it to the user's input

    While valid_guess is False
        Test if 'guess.lower()' is in 'guessed_letters', and if it is, then
            Print "You already guessed that letter"
            Set 'guess' to the user's input
        Test if the length of 'guess' is not equal to 1, and if it is not, then
            Print "Please enter a single letter"
            Set 'guess' to the user's input
        Test if 'guess' is not a letter, and if it is not, then
            Print "Please enter a letter"
            Set 'guess' to the user's input
        Otherwise
            Set valid_guess to True
            Set 'guess' to 'guess.lower()'
    Append 'guess' to 'guessed_letters'
    Return 'guessed_letters'
    

# Create a list of words
words = ["humanity", "just", "machinery", "hypothesize", "see", "slime", "dark", "listen", "paint", "cat",
         "anticipation", "position", "drama", "defend", "explode", "sentence", "rest", "reservoir", "refuse",
         "nightmare"]

Use the 'random.choice(words)' code to get a random word from our list
Create a new variable called 'revealed_letters' and set it to "_" * len(random_word)
Create a new variable called 'guessed_letters' and set it to an empty list
Create a new variable called 'continue_game' and set it to True
while continue_game is True
    Set 'guessed_letters' to the result of calling 'get_valid_guess' with 'guessed_letters' as the argument
    Set 'guess' to the last item in 'guessed_letters'
    If 'guess' is in 'random_word', then
        Print "Correct!"
        For each index in the range of the length of 'random_word'
            If the letter at index 'i' in 'random_word' is equal to 'guess', then
        
                Set 'revealed_letters' to 'revealed_letters' up to index 'i' + 'random_word[i]' + 'revealed_letters' from index 'i' + 1 to the end
                Print 'revealed_letters' without a newline
            Otherwise
                Print "_", without a newline
        Print a newline
    Otherwise
        Print "Incorrect!"
