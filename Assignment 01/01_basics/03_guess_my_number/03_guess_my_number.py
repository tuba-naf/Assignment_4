def main():
    # Generate the secret number at random!
    secret_number: int = 5

    print("I am thinking of a number between 1 and 99...")

    # Get user's guess
    guess = int(input("Enter a guess: "))
    if guess == secret_number:
        print("Congrats! The number was: " + str(secret_number))
    elif guess < secret_number:
        print("Your guess is too low")
    elif guess > secret_number:
        print("Your guess is too high")
    else:
        print("Try your luck next time")

    print()  # Empty line for neatness
    guess: int = int(input("Enter a new guess: "))

# This runs the main function
if __name__ == '__main__':
    main()
