'''
This file contains the Car class.
'''
import pygame
import math
class Car:
    def __init__(self, x, y, image_path):
        self.x = x
        self.y = y
        self.image = pygame.image.load(image_path)
        self.speed = 0
        self.angle = 0
    def update(self):
        # Update car position based on user input or AI logic
        self.x += self.speed * math.cos(math.radians(self.angle))
        self.y -= self.speed * math.sin(math.radians(self.angle))
    def draw(self, screen):
        # Draw the car on the screen
        screen.blit(self.image, (self.x, self.y))
    def accelerate(self, acceleration):
        # Increase the car's speed
        self.speed += acceleration
    def decelerate(self, deceleration):
        # Decrease the car's speed
        self.speed -= deceleration
    def turn_left(self, angle):
        # Rotate the car to the left
        self.angle += angle
    def turn_right(self, angle):
        # Rotate the car to the right
        self.angle -= angle