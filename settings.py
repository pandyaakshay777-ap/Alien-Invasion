class Settings:
    '''
    Define the Settings
    '''

    def __init__(self):
        '''
        Initializing Game
        '''
        # Scale Factor for Level Up
        self.speed_scale = 1.1

        # Screen Settings
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (230, 230, 230)

        # Ship Settings
        self.ship_limit = 3
        
        # Bullet Settings
        self.bullet_allowed = 3
        self.bullet_color = (60,60,60)
        self.bullet_width = 3
        self.bullet_height = 15

        # Alien Settings
        self.fleet_drop_speed = 10
        self.fleet_direction = 1

        # Button Settings
        self.button_width = 200
        self.button_height = 50
        self.button_color = (255, 0, 0) 
        self.button_text_color = (255, 255, 255)
        self.button_text_size = 48

        # Dynamic Settings
        self._initialize_dynamic_settings()

    def _initialize_dynamic_settings(self):
        '''
        Initializes Dynamic Settings
        '''
        self.ship_speed = 1.5
        self.alien_speed = 1.0
        self.bullet_speed = 3.0
    
    def increase_speed(self):
        '''
        Increases Speed
        '''
        self.ship_speed *= self.speed_scale
        self.bullet_speed *= self.speed_scale
        self.alien_speed *= self.speed_scale