'''
This file contains the ScrabbleGame class which represents the game logic.
'''
import tkinter as tk
from board import ScrabbleBoard
from player import ScrabblePlayer
class ScrabbleGame:
    def __init__(self, root):
        self.root = root
        self.board = ScrabbleBoard()
        self.players = [ScrabblePlayer("Player 1"), ScrabblePlayer("Player 2")]
        self.current_player = 0
    def start(self):
        self.root.title("Scrabble Game")
        self.root.geometry("800x600")
        self.board.create_board(self.root)
        self.board.place_tiles()
        self.create_player_labels()
    def create_player_labels(self):
        self.player_labels = []  # Create a list to store player labels
        for i, player in enumerate(self.players):
            label = tk.Label(self.root, text=player.name)
            label.place(x=20, y=20 + i * 30)
            self.player_labels.append(label)  # Add label to player_labels list
        self.update_player_labels()  # Call update_player_labels without parameter
    def update_player_labels(self):
        for i, player in enumerate(self.players):
            self.player_labels[i].config(text=f"{player.name}: {player.score}")
    def switch_player(self):
        self.current_player = (self.current_player + 1) % len(self.players)
    def play_turn(self, word):
        player = self.players[self.current_player]
        score = self.board.calculate_score(word)
        player.update_score(score)
        self.update_player_labels()
        self.switch_player()
class ScrabbleBoard:
    def __init__(self):
        self.tiles = []
    def create_board(self, root):
        # Code to create the game board GUI
        # Implement the logic to create the game board GUI using tkinter
        board_frame = tk.Frame(root, width=600, height=600, bg="white")
        board_frame.pack()
        for i in range(15):
            for j in range(15):
                tile_frame = tk.Frame(board_frame, width=40, height=40, bg="light gray", highlightbackground="black", highlightthickness=1)
                tile_frame.grid(row=i, column=j, padx=1, pady=1)
    def place_tiles(self):
        # Code to place the initial tiles on the board
        # Implement the logic to place the initial tiles on the board
        pass
    def calculate_score(self, word):
        # Code to calculate the score for a given word
        # Implement the logic to calculate the score for a given word
        pass
class ScrabblePlayer:
    def __init__(self, name):
        self.name = name
        self.score = 0
    def update_score(self, score):
        self.score += score