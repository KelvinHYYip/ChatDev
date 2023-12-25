'''
This file contains the ScrabblePlayer class which represents a player in the game.
'''
class ScrabblePlayer:
    def __init__(self, name):
        self.name = name
        self.score = 0
    def update_score(self, score):
        self.score += score