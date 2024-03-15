import random
import os

# Function to clear the screen
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Function to print the game menu
def print_menu():
    clear()
    print("Welcome to the Rock, Scissors and Paper game")

# Function to get user's choice
def get_user_choice():
    while True:
        print("Choose Rock, Scissors or Paper")
        print("1. Rock")
        print("2. Scissors")
        print("3. Paper")
        user_choice = input("Choose an option: ")
        if user_choice in ["1", "2", "3"]:
            return user_choice
        else:
            print("Invalid option. Please choose 1, 2, or 3.")

# Function to determine the winner
def determine_winner(user_choice, system_choice):
    if user_choice == system_choice:
        return "It's a tie!"
    elif (user_choice == "1" and system_choice == "2") or (user_choice == "2" and system_choice == "3") or (user_choice == "3" and system_choice == "1"):
        return "You win"
    else:
        return "System wins"

# Function to play the game
def play_game():
    user_score = 0
    system_score = 0

    clear()
    print_menu()

    while True:
        option = input("You play (y/n): ")
        if option.lower() == "n":
            break
        elif option.lower() == "y":
            clear()
            user_choice = get_user_choice()
            if user_choice == "1":
                user_choice = "Rock"
            elif user_choice == "2":
                user_choice = "Scissors"
            elif user_choice == "3":
                user_choice = "Paper"
            else:
                print("Invalid option")
                break
            clear()
            print("You choose:", user_choice)
            system_choice = random.choice(["Rock", "Scissors", "Paper"])
            print("The system choose:", system_choice)
            result = determine_winner(user_choice, system_choice)
            print(result)
            if result == "You win":
                user_score += 1
            elif result == "System wins":
                system_score += 1

        print("User score:", user_score)
        print("System score:", system_score)

    clear()
    print("Game Over!!")
    print("User score:", user_score)
    print("System score:", system_score)

    if user_score > system_score:
        print("Congratulations! You are the winner!")
    elif user_score < system_score:
        print("Sorry, the system wins!")
    else:
        print("It's a tie!")

play_game()
