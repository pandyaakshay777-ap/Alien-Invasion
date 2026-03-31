class GameStats:
    '''
    Tracks and Stores the Game Statistics
    '''
    def __init__(self, ai_game):
        '''
        Initializes the Game Statistics
        '''
        self.settings = ai_game.settings # Import Settings of The Game
        self._reset_stats() # Reset the Stats

    def _reset_stats(self):
        '''
        Resets the Statistics Of the Game
        '''
        self.ships_left = self.settings.ship_limit # Import the limit number of ships
        self.score = 0 # Initial Score