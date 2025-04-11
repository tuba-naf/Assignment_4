def main():
    # Ask the user for a number and convert it to an integer
    curr_value = int(input("Enter a number: "))

    # Double and print the value until it's 100 or more
    while curr_value < 100:
        curr_value = curr_value * 2
        print(curr_value)

# Run the main function
if __name__ == '__main__':
    main()
