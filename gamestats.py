class GameStats:
    '''
    Tracks and Stores the Game Statistics
    '''
    def __init__(self, ai_game):
        '''
        Initializes the Game Statistics
        '''
        self.settings = ai_game.settings # Import Settings of The Game
        self.score = 0 # Initial Score
        self.high_score = 0 # Initial High Score
        self._reset_stats() # Reset the Stats

    def _reset_stats(self):
        '''
        Resets the Statistics Of the Game
        '''
        self.ships_left = self.settings.ship_limit # Import the limit number of ships
        self.score = 0 # Initial Score
        self.level = 1 # Initial Level
    
    def _check_high_score(self):
        '''
        Checks if the Current Score is Higher than the High Score
        '''
        if self.score > self.high_score:
            self.high_score = self.score