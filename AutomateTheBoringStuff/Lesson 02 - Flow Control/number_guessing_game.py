# Note: The following is pseudocode. It will not run in this format.

# Pick a random number between 1 and 10
computer_choice = random_number_between_1_and_10()

# Set the initial number of guesses to 0
guesses = 0

# Keep asking the player to guess until they get it right
while True:
    # Ask the player to guess a number
    user_choice = get_user_input()

    # Check if the guess is correct
    if user_choice equals computer_choice:
        # Tell the player they guessed it and end the game
        print("You guessed it!")
        break
    # Check if the guess is too high
    elif user_choice is greater than computer_choice:
        print("You guessed too high!")
    # Check if the guess is too low
    elif user_choice is less than computer_choice:
        print("You guessed too low!")

    # Increase the number of guesses by 1
    guesses = guesses + 1

# Tell the player how many guesses it took to get it right
print("It took you " + guesses + " guesses.")

# Thank the player for playing
print("Thanks for playing!")
