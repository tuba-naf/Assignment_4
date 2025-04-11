import random

def guess_the_number():
    # Computer chooses a random number between 1 and 10
    number_to_guess = random.randint(1, 10)
    print("The computer has chosen a number between 1 and 10.")

    # User's turn
    user_guess = int(input("Your turn! Guess the number: "))
    if user_guess == number_to_guess:
        print("You guessed it! The number was", number_to_guess)
    else:
        print(f"Oops! The number was {number_to_guess}. Better luck next time!")

    # Now, it's the computer's turn to guess
    print("Now it's the computer's turn to guess.")
    computer_guess = random.randint(1, 10)
    print(f"The computer guessed: {computer_guess}")

    if computer_guess == number_to_guess:
        print(f"The computer guessed correctly! The number was {number_to_guess}")
    else:
        print(f"The computer guessed wrong! The number was {number_to_guess}")

guess_the_number()
