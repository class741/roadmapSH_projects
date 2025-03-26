# first project in pythone done, allhamdulillah (03/26/2025)!
import random

print("Welcome to the number game!\n I am thinking of a number between 1 and 100.\n Please select a difficuly level:\n easy (10 chances)\n medium (5 chances)\n hard (3 chances)\n")

difficulty_level = input("Enter your choice(type easy, medium, or hard): ")

print(f"Good choice! You have chosen {difficulty_level} difficulty level. \nLets start the game")

if difficulty_level == 'hard':
    attempts = 3
elif difficulty_level == 'medium':
    attempts = 5
else:
    attempts = 10

num = random.randint(1, 1000)
guess_counter = 0

while attempts != guess_counter:
    guess = input("enter your guess: ")
    if int(guess) < num:
        print(f"Incorrect! The number is greater than {guess}.")
        guess_counter += 1
    elif int(guess) > num:
        print(f"Incorrect! The number is less than {guess}.")
        guess_counter += 1
    else:
        guess_counter += 1
        print(f"Condratulations! You guess the correct number in {guess_counter} attempts.")
        break
