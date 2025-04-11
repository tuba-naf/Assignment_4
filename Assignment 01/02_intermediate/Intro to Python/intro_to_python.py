# Constants for the gravitational constants of the planets (compared to Earth's gravity)
MERCURY_GRAVITY = 0.376
VENUS_GRAVITY = 0.889
MARS_GRAVITY = 0.378
JUPITER_GRAVITY = 2.36
SATURN_GRAVITY = 1.081
URANUS_GRAVITY = 0.815
NEPTUNE_GRAVITY = 1.14
EARTH_GRAVITY = 1.0

def main():
    # Prompt the user for their weight on Earth
    earth_weight = float(input("Enter your weight on Earth: "))
    
    # Prompt the user for the name of a planet
    planet = input("Enter a planet: ")

    # Determine the gravitational constant for the selected planet
    if planet == "Mercury":
        gravity_constant = MERCURY_GRAVITY
    elif planet == "Venus":
        gravity_constant = VENUS_GRAVITY
    elif planet == "Mars":
        gravity_constant = MARS_GRAVITY
    elif planet == "Jupiter":
        gravity_constant = JUPITER_GRAVITY
    elif planet == "Saturn":
        gravity_constant = SATURN_GRAVITY
    elif planet == "Uranus":
        gravity_constant = URANUS_GRAVITY
    else:
        # Default to Neptune if the planet is not recognized (can assume it's one of the listed planets)
        gravity_constant = NEPTUNE_GRAVITY

    # Calculate the equivalent weight on the selected planet
    planetary_weight = earth_weight * gravity_constant

    # Round the result to two decimal places
    rounded_planetary_weight = round(planetary_weight, 2)
    #The line rounded_planetary_weight = round(planetary_weight, 2) is rounding the value of planetary_weight to 2 decimal places.

    # Print the result
    print(f"The equivalent weight on {planet} is: {rounded_planetary_weight}")

if __name__ == "__main__":
    main()
