def mad_libs():
    # Ask the user for words
    adjective = input("Enter an adjective: ")
    animal = input("Enter an animal: ")
    verb = input("Enter a verb (past tense): ")
    exclamation = input("Enter an exclamation (like Wow!, Oops!): ")
    noun = input("Enter a noun: ")
    place = input("Enter a place: ")

    # Story using the inputs
    story = f"""
    {exclamation} I can't believe it! 
    Yesterday, I saw a {adjective} {animal} in the {place}.
    It suddenly {verb} right in front of me and dropped a {noun}!
    What a wild day!
    """

    # Print the funny story
    print("\nHere's your Mad Libs story:")
    print(story)

# Call the function to start the game
mad_libs()
