'''
This file contains the main entry point of the 2D car racing game.
'''
from car import Car
from race import Race
# Create a car object
car = Car("Type A")
# Create a race object with a race route and the car
race = Race("Route 1", car)
# Start the race
race.start()