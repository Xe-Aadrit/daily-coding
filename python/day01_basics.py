# OOP Concepts Practice 

import time
import winsound # Windows-only; will raise ImportError on non-Windows platforms

class Microwave:
    # Class-level power chart (constant)
    POWER_CHART = {
            'A': 1000,
            'B': 900,
            'C': 800,
            'D': 700,
            'E': 600
        }
    
    # -------- Initializers --------
    def __init__(self, brand: str, power_rating: str):
        """Initialize Microwave with brand and power_rating.

        power_rating should be a key from POWER_CHART ('A'-'E').
        """
        self.brand = brand
        self.power_rating = power_rating
        self.turned_on = False

    # -------- Methods --------
    # Turns on the microwave
    def turn_on(self):
        if self.turned_on:
            print(f"Microwave ({self.brand}) is already turned on.")
        else:
            self.turned_on = True
            print(f"Microwave ({self.brand}) has been turned on.")
        
    # Turns off the microwave
    def turn_off(self):
        if self.turned_on:
            self.turned_on = False
            print(f"Microwave ({self.brand}) has been turned off.")
        else:
            print(f"Microwave ({self.brand}) is already turned off.")

    # Microwave Info
    def info(self):
        """Print information about the microwave."""
        print("\nViewing Info:\n")
        print(f"-------- Microwave --------\n • Brand: {self.brand}\n • Power Rating: {self.POWER_CHART[self.power_rating]} ({self.power_rating})\n")

    def run(self, seconds: int):
        """Run the microwave countdown.
        
        seconds: countdown duration in seconds (non-negative).
        Side effects:
            - prints countdown
            - sleeps for each second
            - plays a beep when finished
        """
        if not self.turned_on:
            print(f"Please turn on the Microwave ({self.brand}) first!")
            return

        if seconds < 0:
            print("Invalid time: 'seconds' must be non-negative.")
            return
        
        print("The process has started.")
        max_width = len(str(seconds))
        for i in range(seconds, -1, -1):
            print(f' {i:{max_width}d}', end = '\r', flush= True)
            time.sleep(1)
        print(' ' * (max_width + 2), end='\r')
        winsound.Beep(1000, 500)
        print("Done!")
    
    def __str__(self):
        return f'{self.brand} (Rating: {self.power_rating})'
    
    def __repr__(self):
        return f'Microwave (brand="{self.brand}", power_rating="{self.power_rating}")'
    
# -------- Main (Procedural Part) --------

mic_brand = input("Enter the brand of the microwave: ")

# validating the microwave power_rating
while True:
    mic_power = input("Enter the power rating (A, B, C, D, E): ").upper()
    if mic_power not in Microwave.POWER_CHART.keys():
        print("Invalid Power rating. Please re-enter a valid power rating.")
        continue
    break

my_microwave = Microwave(mic_brand, mic_power)

print("Microwave Operation Menu:")
while True:
    print("1. Turn ON \n2. Run \n3. Turn OFF \n4. Info \n5. Exit") # Menu
    choice = input("Enter your choice (1-5): ")
    match choice:

        case '1':
            my_microwave.turn_on()

        case '2':
            if not my_microwave.turned_on:
                print("Please turn on the microwave first!")
                continue

            # validating number of seconds
            while True:
                try:
                    time_sec = int(input("Enter time in seconds: "))
                    if time_sec < 0:
                        print("Please enter a non-negative integer for seconds.")
                        continue
                    break
                except ValueError:
                    print("Invalid input. Please enter an integer number of seconds.")

            my_microwave.run(time_sec)

        case '3':
            my_microwave.turn_off()

        case '4':
            my_microwave.info()

        case '5':
            # Auto turn-off feature
            if my_microwave.turned_on:
                print("You tried to exit without turning off the microwave. Microwave automatically turning off.")
                my_microwave.turn_off()
            print("\nExiting...")
            break

        case _:    # Default case
            print("Invalid choice. Please select one of the 5 options given above.")
