import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    '''
    Class that manages ship.
    '''

    def __init__(self, ai_game):
        '''
        Initializing Ship and its Position
        '''
        super().__init__() # Make it a Sprite
        #Initializing the Screen Dimensions
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings

        #Load Image
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        #Properties
        self._center_ship()
        self.speed = self.settings.ship_speed

        #Flags
        self.moving_right = False
        self.moving_left = False

    def blitme(self):
        '''
        Paints the ship on screen
        '''
        #Paint the ship
        self.screen.blit(self.image, self.rect)
    
    def update(self):
        '''
        Update the Aspects of Ship
        '''
        #Move the Ship
        if self.moving_right == True and self.rect.right < self.screen_rect.right:
            self.x += self.speed
        if self.moving_left == True and self.rect.left > 0:
            self.x -= self.speed
        #Update its Position
        self.rect.x = self.x

    def _center_ship(self):
        '''
        Positions the Ship in the Middle of the Screen
        '''
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)