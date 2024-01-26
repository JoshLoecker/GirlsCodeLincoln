"""
Have the computer create a random word and try to guess the word
If a letter is guessed correctly, reveal all locations that letter exists
"""

import random


def get_valid_guess(guessed_letters):
    valied_guess = False
    guess = input("Guess a letter: ")
    while not valied_guess:
        if guess.lower() in guessed_letters:
            print("You already guessed that letter")
            guess = input("Guess a letter: ")
        elif len(guess) != 1:
            print("Please enter a single letter")
            guess = input("Guess a letter: ")
        elif not guess.isalpha():
            print("Please enter a letter")
            guess = input("Guess a letter: ")
        else:
            valied_guess = True
            guess = guess.lower()
    guessed_letters.append(guess)
    return guessed_letters


# Create a list of words
words = ["humanity", "just", "machinery", "hypothesize", "see", "slime", "dark", "listen", "paint", "cat",
         "anticipation", "position", "drama", "defend", "explode", "sentence", "rest", "reservoir", "refuse",
         "nightmare"]

random_word = random.choice(words)
revealed_letters = "_" * len(random_word)
guessed_letters = []
continue_game = True
print(random_word)
while continue_game:
    guessed_letters = get_valid_guess(guessed_letters)
    guess = guessed_letters[-1]
    if guess in random_word:
        print("Correct!")
        for i in range(len(random_word)):
            if random_word[i] == guess:
                revealed_letters = revealed_letters[:i] + random_word[i] + revealed_letters[i + 1:]
                print(revealed_letters, end="")
            else:
                print("_", end="")
        print()
    else:
        print("Incorrect!")
