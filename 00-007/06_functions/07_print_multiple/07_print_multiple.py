def print_multiple(message, repeats):
    # Print the message the specified number of times
    for _ in range(repeats):
        print(message)

def main():
    # Prompt the user for a message and number of repeats
    message = input("Please type a message: ")
    repeats = int(input("Enter a number of times to repeat your message: "))
    
    # Call the print_multiple function with the inputs
    print_multiple(message, repeats)

# This is the entry point for the program
if __name__ == "__main__":
    main()
