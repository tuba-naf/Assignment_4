import random

def main():
    # Generate 10 random numbers between 1 and 100
    random_numbers = [random.randint(1, 100) for _ in range(10)]
    
    # Print the generated random numbers
    print("Random Numbers:", random_numbers)

if __name__ == '__main__':
    main()
#for i in range(10): means you care about the value of i (0, 1, 2, ... 9).

#for _ in range(10): means you don’t care about the value, just want to repeat the action 10 times.
