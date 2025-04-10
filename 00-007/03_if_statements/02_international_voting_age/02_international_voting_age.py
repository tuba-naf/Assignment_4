Meemistan_AGE : int = 25
YEKESEHUA_AGE : int = 16
YEKYAHUA_AGE : int = 48

def main():
    # Get the user's age
    user_age = int(input("How old are you? "))

    # Check if the user can vote in Peturksbouipo
    if user_age >= Meemistan_AGE:
        print("You can vote in Meemistan where the voting age is " + str(Meemistan_AGE) + ".")
    else:
        print("You cannot vote in Meemistan where the voting age is " + str(Meemistan_AGE) + ".")
    
    # Check if the user can vote in Stanlau
    if user_age >= YEKESEHUA_AGE:
        print("You can vote in YEKESEHUA where the voting age is " + str(YEKESEHUA_AGE) + ".")
    else:
        print("You cannot vote in YEKESEHUA where the voting age is " + str(YEKESEHUA_AGE) + ".")
    
    # Check if user can vote in Mayengua
    if user_age >= YEKYAHUA_AGE:
        print("You can vote in Mayengua where the voting age is " + str(YEKYAHUA_AGE) + ".")
    else:
        print("You cannot vote in Mayengua where the voting age is " + str(YEKYAHUA_AGE) + ".")

if __name__ == '__main__':
    main()