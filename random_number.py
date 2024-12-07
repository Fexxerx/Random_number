"""
You are required to build a simple number guessing game where the computer randomly selects a number and the user has to guess it. The user will be given a limited number of chances to guess the number. If the user guesses the number correctly, the game will end, and the user will win. Otherwise, the game will continue until the user runs out of chances.

Requirements
It is a CLI-based game, so you need to use the command line to interact with the game. The game should work as follows:

When the game starts, it should display a welcome message along with the rules of the game.
The computer should randomly select a number between 1 and 100.
User should select the difficulty level (easy, medium, hard) which will determine the number of chances they get to guess the number.
The user should be able to enter their guess.
If the user’s guess is correct, the game should display a congratulatory message along with the number of attempts it took to guess the number.
If the user’s guess is incorrect, the game should display a message indicating whether the number is greater or less than the user’s guess.
The game should end when the user guesses the correct number or runs out of chances.
"""
import random
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
print("You have 5 chances to guess the correct number.\n")
def dificult_of_game():
    dificult = {
        "1": "Easy (10 chances)",
        "2": "Medium (5 chances)",
        "3": "Hard (3 chances)"
    }
    list_chances = {
        "1": 10,
        "2": 5,
        "3": 3
    }
    print("Please select the difficulty level:\n 1. Easy (10 chances)\n 2. Medium (5 chances)\n 3. Hard (3 chances)")
    level = input("Enter your choice: ")
    while True:
        if level in dificult:
            print(f"Great! You have selected {dificult[level]} level.")
            return list_chances[level]
        else:
            print("Invalid choice. Please select a valid option between 1, 2, or 3.")

def gues_the_number(chances, random_number):
    attempts = 0
    print(f"\nYou have {chances} chances to guess the number.")
    while chances > 0:
        try:
            user_number = int(input("Enter your guess: "))
            attempts += 1
        except ValueError:
            print("Please enter a valid number.")
            continue

        if user_number == random_number:
            print(f"Congratulations! You guessed the correct number in {attempts} attempts!")
            return
        elif user_number < random_number:
            print(f"Incorrect! The number is greater than {user_number}")
        else:
            print(f"Incorrect! The number is less than{user_number}")

        chances -= 1
        if chances > 0:
            print(f"You have {chances} chances left.")
        else:
            print(f"Sorry, you're out of chances! The correct number was {random_number}.")

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")


random_number = random.randint(1, 100)
chances = dificult_of_game()
gues_the_number(chances, random_number)