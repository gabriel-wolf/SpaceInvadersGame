import pygame
from pygame.sprite import Group

from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
from mothership import Mothership
import game_functions as gf

def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Space Invaders")

    # play button
    play_button = Button(ai_settings, screen, "Play")



    # stats
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    lives_button = Button(ai_settings, screen, str(stats.ships_left))

    # make ship bullet and enemies
    ship = Ship(ai_settings, screen)
    mothership = Mothership(ai_settings, screen)
    bullets = Group()
    aliens = Group()



    # create alien group
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # mainloop
    while True:
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship,
            aliens, bullets, mothership)

        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens,
                bullets, mothership)
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens,
                bullets)
            gf.update_mothership(ai_settings, screen, stats, sb, ship, aliens,
                bullets, mothership)

        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens,
            bullets, play_button, mothership)

run_game()
