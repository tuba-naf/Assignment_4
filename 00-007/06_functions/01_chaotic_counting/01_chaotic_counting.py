import random

# This variable controls how likely the counting will stop early.
# For example, 0.3 means there's a 30% chance it will stop at each step.
DONE_LIKELIHOOD = 0.3

def chaotic_counting():
    for i in range(10):  # Try to count from 1 to 10
        curr_num = i + 1
        if done():
            return  # Stop early if done() returns True
        print(curr_num)

def done():
    """ Returns True with a probability of DONE_LIKELIHOOD """
    if random.random() < DONE_LIKELIHOOD:
        return True
    return False

def main():
    print("I'm going to count until 10 or until I feel like stopping, whichever comes first.")
    chaotic_counting()
    print("I'm done")

if __name__ == "__main__":
    main()
