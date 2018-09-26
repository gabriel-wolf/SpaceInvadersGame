import pygame.font
from pygame.sprite import Group

from ship import Ship
import settings
from game_stats import GameStats

class Scoreboard():

    def __init__(self, ai_settings, screen, stats):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

        # Font settings for scoring information.
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 32)

        # Prepare the initial score images.
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()
        self.preb_lives(stats)

    def prep_score(self):
        print("score" )

        rounded_score = int(round(self.stats.score, -1))
        if rounded_score != 666 or rounded_score != 0:
            settings.Settings.finalscore = rounded_score
            print("rounded: " + str(rounded_score))
            print("round final: " + str(settings.Settings.finalscore))

        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color,
            self.ai_settings.bg_color)

        # Display the score at the top right of the screen.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 10
        self.score_rect.top = 20

    def preb_lives(self, stats):
        print("lives")
        lives_str = str(stats.ships_left)
        print(str(stats.ships_left))
        self.lives_image = self.font.render(str(lives_str + "x"), True, self.text_color,
            self.ai_settings.bg_color)

        # Display the score at the top right of the screen.
        self.lives_str_rect = self.lives_image.get_rect()
        # self.lives_str_rect.right = self.screen_rect.right - 10
        # self.lives_str_rect.top = 20
        self.lives_str_rect.x = 10 + 0 * self.lives_str_rect.width
        self.lives_str_rect.y = self.screen_rect.top + 15
        # self.lives_str_rect.x = self.screen_rect.left + self.lives_str_rect.width
        # self.lives_str_rect.y = self.screen_rect.bottom + self.lives_str_rect.height

    def prep_high_score(self):
        high_score = int(self.stats.high_score)
        high_score_str = "{:,}".format(high_score)
        high_score_player = GameStats(self.ai_settings).high_score_player
        self.high_score_image = self.font.render(high_score_player + " : " + high_score_str, True,
            self.text_color, self.ai_settings.bg_color)

        # Center the high score at the top of the screen.
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def prep_level(self):
        self.level_image = self.font.render(str(self.stats.level), True,
                self.text_color, self.ai_settings.bg_color)

        # Position the level below the score.
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_ships(self):
        self.ships = Group()
        ship = Ship(self.ai_settings, self.screen)
        ship.rect.x = 10 + 1 * ship.rect.width
        ship.rect.y = self.screen_rect.top + 5
        self.ships.add(ship)


    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.lives_image, self.lives_str_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        # Draw ships.
        self.ships.draw(self.screen)
