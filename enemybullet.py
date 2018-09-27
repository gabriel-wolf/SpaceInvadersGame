import pygame
from pygame.sprite import Sprite

class EnemyBullet(Sprite):

    def __init__(self, ai_settings, screen, ship, alien, mothership):
        super(EnemyBullet, self).__init__()
        self.screen = screen

        # Create bullet rect at (0, 0), then set correct position.
        self.rect = pygame.Rect(0, 0, ai_settings.enemybullet_width,
            ai_settings.enemybullet_height)
        self.rect.centerx = mothership.rect.centerx
        self.rect.top = mothership.rect.top

        # Store a decimal value for the bullet's position.
        self.y = float(self.rect.y)

        self.color = ai_settings.enemybullet_color
        self.enemyspeed_factor = ai_settings.enemybullet_speed_factor

    def update(self):
        # Update the decimal position of the bullet.
        self.y += self.enemyspeed_factor
        # Update the rect position.
        self.rect.y = self.y

    def draw_enemybullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
