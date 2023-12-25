def play_turn(self, word):
    player = self.players[self.current_player]
    score = self.board.calculate_score(word)
    player.update_score(score)
    self.update_player_labels()  # Remove player_labels parameter
    self.switch_player()