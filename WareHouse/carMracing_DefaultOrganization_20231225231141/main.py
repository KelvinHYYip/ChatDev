'''
This is the main file of the Mario Cart style car racing game.
'''
import pygame
from car import Car
from track import Track
import math
# Initialize the game
pygame.init()
# Set up the game window
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Mario Cart Racing Game")
# Create the track
track = Track(screen_width, screen_height)
# Create the player's car
player_car = Car(screen_width // 2, screen_height - 100, "player_car.png")
# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # Update the game state
    player_car.update()
    # Render the game
    screen.fill((255, 255, 255))
    track.draw(screen)
    player_car.draw(screen)
    pygame.display.flip()
# Quit the game
pygame.quit()