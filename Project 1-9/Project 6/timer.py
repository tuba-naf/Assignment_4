import time

def countdown_timer(seconds):
    while seconds > 0:
        print(f"Time remaining: {seconds} seconds")
        time.sleep(1)
        seconds -= 1
    print("Time's up!")

# Ask the user for the countdown time
time_in_seconds = int(input("Enter the time for countdown in seconds: "))
countdown_timer(time_in_seconds)
