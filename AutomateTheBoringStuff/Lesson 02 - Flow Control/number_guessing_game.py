import random

computer_choice = random.randint(1, 10)

guesses = 0

while True:
    user_choice = int(input("Guess a number between 1 and 10: "))
    if user_choice == computer_choice:
        print("You guessed it!")
        break
    elif user_choice > computer_choice:
        print("You guessed too high!")
    elif user_choice < computer_choice:
        print("You guessed too low!")
    
    guesses += 1  # OR: guesses = guesses + 1

print("It took you " + str(guesses) + " guesses.")
print("Thanks for playing!")
