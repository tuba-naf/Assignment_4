import random

# List of famous Urdu poets and poetic terms
poet_list = ["iqbal", "ghalib", "faiz", "faraz", "mir", "sufi", "bulleh", "nazir", "zafar"]

# Function to get a random poet or poetry term
def get_word():
    return random.choice(poet_list)

# Simple Hangman game
def hangman():
    word = get_word()  # Select a random word
    guessed_letters = []  # List to store guessed letters
    attempts = 6  # Number of attempts left

    print("Welcome to Urdu Poet's Hangman!")
    print("Guess the name of a famous Urdu poet or poetic term!")

    # Main loop for guessing
    while attempts > 0:
        # Display current word with guessed letters
        display = ''.join([letter if letter in guessed_letters else "_" for letter in word])
        print("\nCurrent word: " + display)
        print(f"Attempts left: {attempts}")

        guess = input("Guess a letter: ").lower()  # Get user's guess

        # Check if the input is valid
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter only one letter.")
            continue

        # If the letter has been guessed already
        if guess in guessed_letters:
            print("You've already guessed that letter!")
            continue

        # If the letter is in the word
        if guess in word:
            guessed_letters.append(guess)
            print(f"Good guess! '{guess}' is in the word.")
        else:
            attempts -= 1
            print(f"Wrong guess! '{guess}' is not in the word.")

        # Check if the word is completely guessed
        if all(letter in guessed_letters for letter in word):
            print(f"Congratulations! You've guessed the word '{word}' correctly!")
            break

    if attempts == 0:
        print(f"Sorry, you're out of attempts. The word was '{word}'.")

# Start the game
hangman()
