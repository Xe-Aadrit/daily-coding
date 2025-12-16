# OOP Concepts Practice 

import time
import winsound # Windows-Only

class Microwave: # It must be in pascal case

    POWER_CHART = {
            'A': 1000,
            'B': 900,
            'C': 800,
            'D': 700,
            'E': 600
        }
    # Initializers
    def __init__(self, brand, power_rating):
        self.brand = brand
        self.power_rating = power_rating
        self.turned_on = False

    # Methods
    def turn_on(self):
        if self.turned_on:
            print(f"Microwave ({self.brand}) is already turned on.")
        else:
            self.turned_on = True
            print(f"Microwave ({self.brand}) has been turned on.")
        
    def turn_off(self):
        if self.turned_on:
            self.turned_on = False
            print(f"Microwave ({self.brand}) has been turned off.")
        else:
            print(f"Microwave ({self.brand}) is already turned off.")

    def info(self):
        print(f"Power rating of Microwave ({self.brand}) is: {self.POWER_CHART[self.power_rating]}")

    def run(self, seconds: int, temp: float):
        # seconds indicate the amount of time needed to cook/warm the food, and temp indicates the temperature in degrees fahrenheit
        # although temperature has no use now, it will be used in the future
        if not self.turned_on:
            print(f"Please turn on the Microwave ({self.brand}) first!")
            return
        
        print("The process has started.")
        max_width = len(str(seconds))
        for i in range(seconds, -1, -1):
            print(f'{i:{max_width}d}', end = '\r', flush= True)
            time.sleep(1)
        print(' ' * (max_width + 2), end='\r')
        winsound.Beep(1000, 500)
        print("Done!")
    
    def __str__(self):
        return f'{self.brand} (Rating: {self.power_rating})'
    
    def __repr__(self):
        return f'Microwave (brand="{self.brand}", power_rating="{self.power_rating}")'
    
# Main (Procedural Part)

# Blueprint (Object) 1:
smeg = Microwave('Smeg', 'A')

# Blueprint (Object) 2:
bosch = Microwave('Bosch', 'B')

print(smeg)
print(bosch)