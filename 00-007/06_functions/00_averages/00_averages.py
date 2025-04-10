def find_average(num1, num2):
    average = (num1 + num2) / 2
    return average

def main():
    # Example usage
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    
    avg = find_average(num1, num2)
    print(f"The average of {num1} and {num2} is {avg}")

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()
