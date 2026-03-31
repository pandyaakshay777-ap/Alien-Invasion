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
        pygame.init() # WELCOME PYGAME

        #Backend
        self.clock = pygame.time.Clock() 
        self.settings = Settings()

        #Frontend
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption('Alien Invasion')
        self.stats = GameStats(self)
        self.game_active = True

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
            self._check_events() # Examines All Events
            if self.game_active == True:
                self.ship.update() # Updates the Ship
                self._update_bullet()  # Updates the Bullet
                self._update_aliens() # Updates Alien
            self._update_screen() # Refreshes The Screen
            self.clock.tick(60) # Sets Refresh Rate
    
    def _check_events(self):
        '''
        Respond to Keyboard and Mouse Movement
        '''
        #Examines all Events
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
        #Moves the Ship Right
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        #Moves the Ship Left
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        #Fires Bullet
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        #Exit The Game on Q-Press
        elif event.key == pygame.K_q:
            sys.exit()
        
    def _key_up(self, event):
        '''
        Responds to key up events
        '''
        #Stops the ship from moving right
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        #Stops the ship from moving left
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        '''
        Fires Bullets
        '''
        #Fires bullet ONLY IF there are less than 3 Active Bullets
        if len(self.bullets.sprites()) < self.settings.bullet_allowed:
            #Creates a Bullet
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
        
        #Detect and Respond to Collisions withh Alien
        self._bullet_alien_collide()

    def _bullet_alien_collide(self):
        '''
        Detect Collison of Alien with Bullet and Respond Appropriately
        '''
        #Records Collisions
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)\
        #Resets Screen
        if not self.aliens.sprites():
            self._create_fleet()
            self.ship._center_ship()


    def _create_fleet(self):
        '''
        Creates a Fleet of Aliens
        '''
        #Creates an Instance of Alien
        alien = Alien(self)
        
        #Retrieves Position and Size of Alien
        alien_width, alien_height = alien.rect.size
        current_x, current_y = alien_width, alien_height

        #Creates a Fleet
        while current_y < self.settings.screen_height - 3 * alien_height:
            #Creates a Row
            while current_x < self.settings.screen_width - 2 * alien_width:
                self._create_alien(current_x, current_y) #Create an Alien
                current_x += 2 * alien.rect.width #Next Column
            #Next Row
            current_x = alien.x
            current_y += 2 * alien.rect.height

    def _create_alien(self, x_position, y_position):
        '''
        Create an Alien
        '''
        #Create one new alien
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)

    def _update_aliens(self):
        '''
        Update the position of an Alien
        '''
        self._check_fleet_edges() # Checks if fleet crosses right-left edges
        self._check_alien_bottom() # Checks if Alien Touches Bottom and if TRUE => reset ship
        self.aliens.update() # Alien's Position is updated

        # Checks if Colliding with Ship
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit() # Resets Screen Aptly
    
    def _check_alien_bottom(self):
        '''
        Check if Alien Touches Bottom of the Screen and Responds Appropriately
        '''
        #Check for Each Alien
        for alien in self.aliens.sprites():
            #Checks if Any Crosses Bottom Edge
            if alien.rect.bottom >= self.screen.get_rect().bottom:
                self._ship_hit() # Resets Screen Aptly
                break 

    def _ship_hit(self):
        '''
        Resets the Game on Ship Hit
        '''
        # Checks if any Ship Left
        if self.stats.ships_left > 0:
            self.stats.ships_left -= 1 # Update the Number of Ships
            self.ship._center_ship() # Repositions the Ship

            self.bullets.empty() # Delete all Current Bullets
            self.aliens.empty() # Delete all Current Alien

            sleep(0.5) #Pause for 1/2 Seconds
        else:
            self.game_active = False # Game Over

    def _check_fleet_edges(self):
        '''
        Checks if fleet is at edge
        '''
        #Checks for Every Alien
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction() # Bouncing off The Edge
                break
    
    def _change_fleet_direction(self):
        '''
        Changes the direction of fleet and drops it
        '''
        #Drop The Entire Fleet a Bit
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1 # Reverse the Fleet Direction
        
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

#THIS FILE IS RUN => RUN the GAME
if __name__ == '__main__':
    ai = AlienInvasion() # Creates an Instance of the Game
    ai.run_game() # Runs the Game