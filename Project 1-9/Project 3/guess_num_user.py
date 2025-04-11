import random

def guess_the_number():
    print("Welcome to the 'Guess My Number' game!")
    print("Please think of a number between 1 and 10, and I'll try to guess it.")
    
    # Get the user's number
    user_number = int(input("Enter your number (I won't peek!): "))
    
    # Initializing computer's guess range
    low, high = 1, 10
    attempts = 0
    
    while True:
        # Computer makes a guess
        guess = random.randint(low, high)
        attempts += 1
        print(f"\nComputer's guess: {guess}")
        
        # Check if the guess is correct
        if guess == user_number:
            print(f"\n Yay! I guessed it right in {attempts} attempts. ")
            break  # End the game when the computer guesses correctly
        else:
            print("Hmm, not quite. Let me try again!")
    
guess_the_number()
