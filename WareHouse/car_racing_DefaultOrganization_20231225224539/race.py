'''
This file contains the Race class.
'''
class Race:
    def __init__(self, race_route, car):
        self.race_route = race_route
        self.car = car
    def start(self):
        '''
        Starts the race with the specified car on the race route.
        '''
        print(f"Starting race on {self.race_route} with a {self.car.car_type} car.")
        self.car.accelerate()
        self.car.turn("left")
        self.car.turn("right")
        self.car.brake()
        print("Race finished!")