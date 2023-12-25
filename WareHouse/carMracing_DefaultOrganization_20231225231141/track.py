'''
This file contains the Track class.
'''
import pygame
class Track:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.image = pygame.Surface((width, height))
        self.image.fill((0, 0, 0))
    def draw(self, screen):
        # Draw the track on the screen
        screen.blit(self.image, (0, 0))