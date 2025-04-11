import random

def play_rock_paper_scissors():
    print("Welcome to Rock, Paper, Scissors!")

    # Define the choices
    choices = ["rock", "paper", "scissors"]
    
    # Get the user's choice
    user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()

    # Ensure the user input is valid
    while user_choice not in choices:
        user_choice = input("Invalid choice! Please choose rock, paper, or scissors: ").lower()

    # Let the computer make a random choice
    computer_choice = random.choice(choices)

    print(f"\nYou chose {user_choice}.")
    print(f"The computer chose {computer_choice}.")

    # Determine the winner
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        print("You win!")
    else:
        print("You lose!")

# Run the game
play_rock_paper_scissors()
