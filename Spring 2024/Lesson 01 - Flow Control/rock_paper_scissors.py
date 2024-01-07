import random

print("Welcome to the game of Rock, Paper, Scissors!")
user_guess = input("Enter a guess (rock, paper, scissors): ")
computer_guess = random.choice(["rock", "paper", "scissors"])

if user_guess == "rock":
    if computer_guess == "rock":
        print("The computer guessed rock. It's a tie!")
    elif computer_guess == "paper":
        print("The computer guessed paper. You lose!")
    elif computer_guess == "scissors":
        print("The computer guessed scissors. You win!")

elif user_guess == "paper":
    if computer_guess == "rock":
        print("The computer guessed rock. You win!")
    elif computer_guess == "paper":
        print("The computer guessed paper. It's a tie!")
    elif computer_guess == "scissors":
        print("The computer guessed scissors. You lose!")

elif user_guess == "scissors":
    if computer_guess == "rock":
        print("The computer guessed rock. You lose!")
    elif computer_guess == "paper":
        print("The computer guessed paper. You win!")
    elif computer_guess == "scissors":
        print("The computer guessed scissors. It's a tie!")
