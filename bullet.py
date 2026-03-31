import pygame

from pygame.sprite import Sprite

class Bullet(Sprite):
    '''
    Class to Manage Bullets
    '''
    
    def __init__(self, ai_game):
        '''
        Initializing Attributes
        '''
        #Inheriting from SPRITE
        super().__init__()

        #Loading Resources from Alien Invasion Game
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        #Properties
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop
        self.color = self.settings.bullet_color
        self.speed = self.settings.bullet_speed
        self.y = float(self.rect.y)
    
    def update(self):
        '''
        Flying Upto the Top
        '''
        #Changing the bullet's position-y
        self.y -= self.speed
        self.rect.y = self.y
    
    def draw(self):
        '''
        Drawing the Bullet
        '''
        #Draw the Bullet
        pygame.draw.rect(self.screen, self.color, self.rect)