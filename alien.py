import pygame

from pygame.sprite import Sprite

class Alien(Sprite):
    '''
    Class to Manage Aliens
    '''
    def __init__(self, ai_game):
        '''
        Initializing Alien and its position
        '''
        super().__init__() # Make it A Sprite

        #Import Screen and Settings of Game
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        
        #Properties
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
    
    def update(self):
        '''
        Move the alien ship horizontally
        '''
        #Moving the Alien
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x
    

    def check_edges(self):
        '''
        Checks if An Alien is at edge
        '''
        screen_rect = self.screen.get_rect() #Get Shape and Size of Screen
        return (self.rect.left <= 0) or (self.rect.right >= screen_rect.right) #Returns TRUE if at Edge