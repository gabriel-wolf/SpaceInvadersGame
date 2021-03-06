import pygame.font
from game_stats import GameStats

class Button():

    def __init__(self, ai_settings, screen, msg):
        self.stats = GameStats
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # Set the dimensions and properties of the button.
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)
        self.button_gameover_color = (255, 0, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # Build the button's rect object, and center it.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # The button message only needs to be prepped once.
        self.prep_msg(msg)
        self.prep_msg_game_over()


    def prep_msg(self, msg):
        self.msg_image = self.font.render(msg, True, self.text_color,
            self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def prep_msg_game_over(self):
        self.msg_image_gameover = self.font.render("Game Over", True, self.text_color,
            self.button_gameover_color)
        self.msg_image_gameover_rect = self.msg_image_gameover.get_rect()
        self.msg_image_gameover_rect.center = self.rect.center

    def draw_button(self):
        # Draw blank button, then draw message.
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

    def draw_button_gameover(self):
        # Draw blank button, then draw message.
        self.screen.fill(self.button_gameover_color, self.msg_image_gameover_rect)
        self.screen.blit(self.msg_image_gameover, self.msg_image_gameover_rect)
