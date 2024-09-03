import pytest

class Car:
    def __init__(self, make, model, year):  #Initializes a Car object with make, model, and year.

        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Car Info: {self.year} {self.make} {self.model}") #Prints the car's information.

