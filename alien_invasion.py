import sys
from time import sleep

import pygame

from settings import Settings
from gamestats import GameStats
from ship import Ship
from bullet import Bullet
from alien import Alien

class AlienInvasion:
    '''
    Overall Game Window
    '''
    def __init__(self):
        '''Initializing System'''
        pygame.init()

        #Backend
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        #Frontend
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption('Alien Invasion')
        self.stats = GameStats(self)

        #Objects
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._create_fleet()

    def run_game(self):
        '''
        All methods to loop while the game runs
        '''
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullet()
            self._update_aliens()
            self._update_screen()
            self.clock.tick(60)
    
    def _check_events(self):
        '''
        Respond to Keyboard and Mouse Movement
        '''
        for event in pygame.event.get():
            #Close the game on QUIT
            if event.type == pygame.QUIT:
                sys.exit()
            #Respond to Key Down Events
            elif event.type == pygame.KEYDOWN:
                self._key_down(event)
            #Responds to Key Up events
            elif event.type == pygame.KEYUP:
                self._key_up(event)
    
    def _key_down(self, event):
        '''
        Responds to key down events
        '''
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_q:
            sys.exit()
        
    def _key_up(self, event):
        '''
        Responds to key up events
        '''
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        '''
        Fires Bullets
        '''
        if len(self.bullets.sprites()) < self.settings.bullet_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
    
    def _update_bullet(self):
        '''
        Makes the bulets fly upto the top
        '''
        #Makes the Bullets Fly
        self.bullets.update()
        
        #Make the bullets disappear as soo as they touch top edge
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

    def _create_fleet(self):
        '''
        Creates a Fleet of Aliens
        '''
        alien = Alien(self)
        
        alien_width, alien_height = alien.rect.size
        current_x, current_y = alien_width, alien_height
        while current_y < self.settings.screen_height - 3 * alien_height:
            while current_x < self.settings.screen_width - 2 * alien_width:
                self._create_alien(current_x, current_y)
                current_x += 2 * alien.rect.width
            current_x = alien.x
            current_y += 2 * alien.rect.height

    def _create_alien(self, x_position, y_position):
        '''
        Create an Alien
        '''
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)

    def _update_aliens(self):
        '''
        Update the position of an Alien
        '''
        self._check_fleet_edges()
        self.aliens.update()
    
    def _check_fleet_edges(self):
        '''
        Checks if fleet is at edge
        '''
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break
    
    def _change_fleet_direction(self):
        '''
        Changes the direction of fleet and drops it
        '''
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1
        
    def _update_screen(self):
        '''
        Updates the screen
        '''
        #BG COLOUR
        self.screen.fill(self.settings.bg_color)
        #PAINT BULLETS
        for bullet in self.bullets.sprites():
            bullet.draw()
        #PAINT SHIP
        self.ship.blitme()
        #PAINT ALIEN
        self.aliens.draw(self.screen)
        #FLIP DISPLAY
        pygame.display.flip()
    
if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()