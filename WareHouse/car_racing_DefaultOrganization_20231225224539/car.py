'''
This file contains the Car class.
'''
class Car:
    def __init__(self, car_type):
        self.car_type = car_type
    def accelerate(self):
        '''
        Accelerates the car.
        '''
        print(f"The {self.car_type} is accelerating.")
    def brake(self):
        '''
        Applies brakes to the car.
        '''
        print(f"The {self.car_type} is braking.")
    def turn(self, direction):
        '''
        Turns the car in the specified direction.
        '''
        print(f"The {self.car_type} is turning {direction}.")