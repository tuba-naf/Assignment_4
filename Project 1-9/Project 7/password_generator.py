import string
import random

def generate_password(length, use_uppercase=True, use_digits=True, use_special_chars=True):
    # Initialize the characters with lowercase letters
    characters = string.ascii_lowercase
    
    # Add uppercase letters if user wants them
    if use_uppercase:
        characters += string.ascii_uppercase
        
    # Add digits if user wants them
    if use_digits:
        characters += string.digits
        
    # Add special characters if user wants them
    if use_special_chars:
        characters += string.punctuation
        
    # Generate the password by picking random characters from the characters set
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

# Ask the user for the password length and preferences
password_length = int(input("Enter the length of the password: "))
include_uppercase = input("Include uppercase letters? (yes/no): ").lower() == 'yes'
include_digits = input("Include digits? (yes/no): ").lower() == 'yes'
include_special_chars = input("Include special characters? (yes/no): ").lower() == 'yes'

# Generate the password
password = generate_password(password_length, include_uppercase, include_digits, include_special_chars)

# Display the generated password
print(f"Your generated password is: {password}")
