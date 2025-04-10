def main():
    try:
        fahrenheit = float(input("\033[1;3mEnter temperature in Fahrenheit: \033[0m"))
        celsius = (fahrenheit - 32) * 5.0/9.0
        print(f"\033[1;32mTemperature: {fahrenheit}°F = {celsius:.2f}°C\033[0m")
    except ValueError:
        print("\033[1;31mError: Please enter a valid number\033[0m")

if __name__ == '__main__':
    main()
    