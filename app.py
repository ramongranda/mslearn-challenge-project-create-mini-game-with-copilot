# Game Rock, Scissors and Paper
# Game rules
# Rock beats Scissors
# Scissors beats Paper
# Paper beats Rock
# Multiplayer user to system

import random
import os

# Function to clear the screen
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Function to print the game menu
def print_menu():
    print("Welcome to the Rock, Scissors and Paper game")
    print("1. Play / Replay the game")
    print("0. Exit")

# Initialize the scores
user_score = 0
system_score = 0

clear()
print_menu()

# When 1 then play the game and when 2 then exit
# Summarize score for the user and the system, and print the result
option = input("Choose an option: ")
while option != "0":
    if option == "1":
        clear()
        print("Choose Rock, Scissors or Paper")
        print("1. Rock")
        print("2. Scissors")
        print("3. Paper")
        user = input("Choose an option: ")
        if user == "1":
            user = "Rock"
        elif user == "2":
            user = "Scissors"
        elif user == "3":
            user = "Paper"
        else:
            print("Invalid option")
            break
        clear()
        print("You choose: " + user)
        system = random.choice(["Rock", "Scissors", "Paper"])
        print("The system choose: " + system)
        if user == "Rock" and system == "Scissors":
            print("You win")
            user_score += 1
        elif user == "Scissors" and system == "Paper":
            print("You win")
            user_score += 1
        elif user == "Paper" and system == "Rock":
            print("You win")
            user_score += 1
        else:
            print("System wins")
            system_score += 1

    # Print the scores at the end of the loop
    print("User score: ", user_score)
    print("System score: ", system_score)
    option = input("Choose another option : ")
# End the game print the final score
print("Game over")
print("User score: ", user_score)
print("System score: ", system_score)1


