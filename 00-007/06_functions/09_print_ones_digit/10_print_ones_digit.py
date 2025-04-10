def print_ones_digit(num):
    # Use modulo operator to find the ones digit
    ones_digit = num % 10
    print(f"The ones digit is {ones_digit}")

def main():
    # Prompt the user for a number
    num = int(input("Enter a number: "))
    
    # Call the print_ones_digit function to print the ones digit
    print_ones_digit(num)

# This is the entry point for the program
if __name__ == "__main__":
    main()
