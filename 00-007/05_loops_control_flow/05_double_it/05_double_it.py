def main():
    # Ask the user for a number
    curr_value = int(input("Enter a number: "))
    
    # Loop until the current value is 100 or greater
    while curr_value < 100:
        # Double the current value
        curr_value *= 2
        # Print the current value followed by a space
        print(curr_value, end=" ")

# Call the main function
if __name__ == "__main__":
    main()
