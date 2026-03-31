class Settings:
    '''
    Define the Settings
    '''

    def __init__(self):
        '''
        Initializing Game
        '''
        #Screen Settings
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (230, 230, 230)

        #Ship Settings
        self.ship_speed = 3.5
        
        #Bullet Settings
        self.bullet_speed = 4.5
        self.bullet_allowed = 3
        self.bullet_color = (60,60,60)
        self.bullet_width = 3
        self.bullet_height = 15

        #Alien Settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        self.fleet_direction = 1