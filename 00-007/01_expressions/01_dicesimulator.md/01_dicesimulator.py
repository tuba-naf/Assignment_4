
# Import the random library which lets us simulate random things like dice!
import random

# Number of sides on each die to roll
NUM_SIDES = 6

def roll_dice():
    """
    Simulates rolling two dice and prints their total
    """
    die1: int = random.randint(1, NUM_SIDES)
    #This line uses the random.randint(a, b) function, which returns a random integer between a and b inclusive (meaning both ends are included).
    die2: int = random.randint(1, NUM_SIDES)
    total: int = die1 + die2
    print("Total of two dice:", total)

def main():
    die1: int = 10
    print("die1 in main() starts as: " + str(die1))
    roll_dice()
    roll_dice()
    roll_dice()
    print("die1 in main() is: " + str(die1))

# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
    #'''Variable Scope
#ariables declared inside a function (like die1 in roll_dice()) are local to that function and do not interfere with variables outside it (like die1 in main()).
#Even if two variables have the same name, they are entirely independent if defined in different scopes.'''