import pygame
from pygame.sprite import Sprite

class Mothership(Sprite):

    def __init__(self, ai_settings, screen):
        super(Mothership, self).__init__()
        self.broken = False
        self.screen = screen
        self.ai_settings = ai_settings

        # Load the ship image, and get its rect.
        if ai_settings.specialalienson == False:
            self.image = pygame.image.load('images/mothership.gif')
        else:
            self.image = pygame.image.load('images/bartellargebroken.png')
            self.image = pygame.image.load('images/bartellarge.png')

        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.top = self.screen_rect.top + 40


        # self.rect.x = self.rect.width
        # self.rect.y = self.rect.height

        # Store a decimal value for the ship's center.
        self.center = float(self.rect.centerx)
        self.x = float(self.rect.x)

        # Movement flags.
        self.moving_right = False
        self.moving_left = False

    def center_ship(self):
        self.center = self.screen_rect.centerx

    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def breakship(self, ai_settings):
        if ai_settings.specialalienson == True:
            self.broken = True
            self.image = pygame.image.load('images/bartellargebroken.png')
            self.screen.blit(self.image, self.rect)
        else:
            None

    def update(self):
        # Update the ship's center value, not the rect.
        if self.broken == True:
            None
        else:
            self.x += (self.ai_settings.mothership_speed_factor *
                            self.ai_settings.mothership_direction)
            self.rect.x = self.x

    def blitme(self):
        self.screen.blit(self.image, self.rect)
