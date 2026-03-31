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
        super().__init__()

        self.screen = ai_game.screen
        self.settings = ai_game.settings
        
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)
    
    def update(self):
        '''
        Move the alien ship horizontally
        '''
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x
    

    def check_edges(self):
        '''
        Checks if An Alien is at edge
        '''
        screen_rect = self.screen.get_rect()
        return (self.rect.left <= 0) or (self.rect.right >= screen_rect.right)