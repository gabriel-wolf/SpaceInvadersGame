import pygame
import random
from pygame.sprite import Sprite

import settings

class Alien(Sprite):

    def __init__(self, ai_settings, screen):
        super(Alien, self).__init__()

        self.screen = screen
        self.ai_settings = ai_settings

        self.image = pygame.image.load('images/ship.png')
        self.shiprect = self.image.get_rect()

        # Load the alien image, and set its rect attribute.
        self.image = pygame.image.load('images/myalien.png')
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact position.
        self.x = float(self.rect.x)
        if ai_settings.specialalienson == True:
            available_space_x = ai_settings.screen_width - 2 * self.rect.width
            number_aliens_x = int(available_space_x / (2 * self.rect.width))
            aliensinwidth = number_aliens_x
            available_space_y = (ai_settings.screen_height - (3 * self.rect.height) - self.shiprect.height)
            number_rows = int(available_space_y / (2 * self.rect.height))
            aliensinheight = number_rows - 5
            self.alienrandomimage = random.randint(0,(aliensinwidth * aliensinheight))
            self.blitme()
        else:
            None

    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        self.x += (self.ai_settings.alien_speed_factor *
                        self.ai_settings.fleet_direction)
        self.rect.x = self.x

    def blitme(self):
        print("random: " + str(self.alienrandomimage))
        if self.alienrandomimage == 1:
            print("kasp")
            self.image = pygame.image.load('images/kaspersky.png')
            self.screen.blit(self.image, self.rect)
        elif self.alienrandomimage == 2:
            print("net")
            self.image = pygame.image.load('images/netsupport.png')
            self.screen.blit(self.image, self.rect)
        elif self.alienrandomimage == 3:
            print("bar")
            self.image = pygame.image.load('images/bartel.png')
            self.screen.blit(self.image, self.rect)
        else:
            print("alien")
            self.image = pygame.image.load('images/myalien.png')
            self.screen.blit(self.image, self.rect)
