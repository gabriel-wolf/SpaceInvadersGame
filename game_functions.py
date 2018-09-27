import sys
import pygame
import random
from time import sleep
import itertools

from settings import Settings

fire_bullet_event = pygame.USEREVENT + 1
pygame.time.set_timer(fire_bullet_event, Settings().enemybulletfirerate)

# import scoreboardwindow
from button import Button
from bullet import Bullet
import alien
from enemybullet import EnemyBullet
from alien import Alien
from mothership import Mothership

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_r:
        if ai_settings.allowcheats == True:
            ai_settings.rapidfire = True
            ai_settings.setbulletsettings()
            ai_settings.setenemybulletsettings()
        else:
            None
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_s:
        if ai_settings.specialalienson == True:
            ai_settings.specialalienson = False
            writealienImage = open("alienimage.txt", mode='w+')
            writealienImage.writelines("False")
            writealienImage.close()
        else:
            ai_settings.specialalienson = True
            writealienImage = open("alienimage.txt", mode='w+')
            writealienImage.writelines("True")
            writealienImage.close()


    elif event.key == pygame.K_q:
        sys.exit()

def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(ai_settings, screen, stats, sb, play_button, ship, aliens,
        bullets, mothership, enemybullets):
    fire_bullet_event
    for event in pygame.event.get():
        if event.type == fire_bullet_event:
            print("event get fire enemy bullet")
            randenemyfire = random.randint(0,100)
            if randenemyfire >= 1 and randenemyfire <= 40:
                print("random correct fire bullet")
                fire_enemybullet(ai_settings,screen,ship,enemybullets,alien,mothership)
            else:
                print("not random")
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, sb, play_button,
                ship, aliens, bullets, mouse_x, mouse_y, mothership, enemybullets)


def check_play_button(ai_settings, screen, stats, sb, play_button, ship,
        aliens, bullets, mouse_x, mouse_y, mothership, enemybullets):
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        # Reset the game settings.
        ai_settings.initialize_dynamic_settings()

        # Hide the mouse cursor.
        pygame.mouse.set_visible(False)

        # Reset the game statistics.
        stats.reset_stats()
        stats.game_active = True

        # Reset the scoreboard images.
        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()
        sb.prep_ships()
        sb.preb_lives(stats)

        # Empty the list of aliens and bullets.
        aliens.empty()
        bullets.empty()
        enemybullets.empty()
        # TODO: empty enemy bullets

        # Create a new fleet and center the ship.
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()
        mothership.center_ship()

# TODO: fire enemy bullets
def fire_bullet(ai_settings, screen, ship, bullets):
    # Create a new bullet, add to bullets group.
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def fire_enemybullet(ai_settings, screen, ship, enemybullets, alien, mothership):
    # Create a new bullet, add to bullets group.
    if len(enemybullets) < ai_settings.enemybullets_allowed:
        print("fire enemy bullet len(enemybullets): " + str(len(enemybullets)))
        print("ai bullet allowed: " + str(ai_settings.enemybullets_allowed))
        new_enemybullet = EnemyBullet(ai_settings, screen, ship, alien, mothership)
        enemybullets.add(new_enemybullet)

def update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets,
        play_button, mothership, enemybullets):
    # Redraw the screen, each pass through the loop.
    background_image = pygame.image.load("images\space.png").convert()

    screen.blit(background_image, [0, 0])

    # TODO: draw enemy bullets
    # Redraw all bullets, behind ship and aliens.
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    for enemybullet in enemybullets.sprites():
        enemybullet.draw_enemybullet()
    ship.blitme()
    mothership.blitme()
    aliens.draw(screen)


        #fire_bullet(ai_settings,screen,ship,bullets)
        #time
        #if pygame.event.get(fire_bullet_event):
            #fire_enemybullet(ai_settings,screen,ship,enemybullets,alien,mothership)

    # else:
    #     print("don't fire enemy bullet")


    # Draw the score information.
    sb.show_score()

    # Draw the play button if the game is inactive.
    if not stats.game_active:
        if stats.score <= 0 or stats.score == None:
            play_button.draw_button()
        elif stats.ships_left <= 0:
            ai_settings.finalscore = stats.score
            print('game over')
            sleep(1)
            play_button.draw_button_gameover()
            sleep(3)
            import scoreboardwindow
            scoreboardwindow()
            #scoreboardwindow.startScoreboard

        else:
            play_button.draw_button()

    # Make the most recently drawn screen visible.
    pygame.display.flip()

# TODO: update alien bullets
def update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets, mothership):
    # Update bullet positions.
    bullets.update()

    # Get rid of bullets that have disappeared.
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    # TODO: check bullet ship collision
    check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship,
        aliens, bullets, mothership)

def update_enemybullets(ai_settings, screen, stats, sb, ship, aliens, enemybullets, mothership):
    # Update bullet positions.
    enemybullets.update()

    # Get rid of bullets that have disappeared.
    for enemybullet in enemybullets.copy():
        if enemybullet.rect.bottom >= ai_settings.screen_height:
            enemybullets.remove(enemybullet)

    # TODO: check bullet ship collision
    check_enemybullet_ship_collisions(ai_settings, screen, stats, sb, ship,
        aliens, mothership, enemybullets)

def check_high_score(stats, sb):
    if stats.score > stats.high_score:
        print("check high score: " + str(stats.score))
        None

def check_enemybullet_ship_collisions(ai_settings, screen, stats, sb, ship,
    aliens, mothership, enemybullets):
    # Remove any bullets and aliens that have collided.
    collisions = pygame.sprite.spritecollide(ship, enemybullets, True)

    if collisions:

        if stats.ships_left > 0:
            print("ships die but not all")
            # Decrement ships_left.
            stats.ships_left -= 1

            # Update scoreboard.
            sb.prep_ships()
            sb.preb_lives(stats)

        else:
            print("else ships hit")
            stats.game_active = False
            pygame.mouse.set_visible(True)

        # Empty the list of aliens and bullets.
        aliens.empty()
        enemybullets.empty()

        # Create a new fleet, and center the ship.
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()
        mothership.center_ship()

        # Pause.
        sleep(0.5)
    check_high_score(stats, sb)


# TODO: bullet ship collision
def check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship,
        aliens, bullets, mothership):
    # Remove any bullets and aliens that have collided.
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    collisionsmother = pygame.sprite.spritecollide(mothership, bullets, True)

    if collisions:
        for aliens in collisions.values():
            stats.score += ai_settings.alien_points * len(aliens)
            sb.prep_score()
            sb.preb_lives(stats)
        check_high_score(stats, sb)

    if collisionsmother:
        mothership.breakship(ai_settings)

    if len(aliens) == 0:
        # If the entire fleet is destroyed, start a new level.
        bullets.empty()
        ai_settings.increase_speed()

        # Increase level.
        stats.level += 1
        sb.prep_level()

        create_fleet(ai_settings, screen, ship, aliens)

def check_fleet_edges(ai_settings, aliens):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break

def check_mothership_edges(ai_settings, mothership):
    if mothership.check_edges():
        change_mothership_direction(ai_settings, mothership)

def change_fleet_direction(ai_settings, aliens):
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1

def change_mothership_direction(ai_settings, mothership):
    ai_settings.mothership_direction *= -1

def ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets, mothership):
    if stats.ships_left > 0:
        print("ships die but not all")
        # Decrement ships_left.
        stats.ships_left -= 1

        # Update scoreboard.
        sb.prep_ships()
        sb.preb_lives(stats)

    else:
        print("else ships hit")
        stats.game_active = False
        pygame.mouse.set_visible(True)

    # Empty the list of aliens and bullets.
    aliens.empty()
    bullets.empty()

    # Create a new fleet, and center the ship.
    create_fleet(ai_settings, screen, ship, aliens)
    ship.center_ship()
    mothership.center_ship()

    # Pause.
    sleep(0.5)

def check_aliens_bottom(ai_settings, screen, stats, sb, ship, aliens,
        bullets, mothership):
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            # Treat this the same as if the ship got hit.
            ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets, mothership)
            break

def update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets, mothership):
    check_fleet_edges(ai_settings, aliens)
    aliens.update()

    # Look for alien-ship collisions.
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets, mothership)

    # Look for aliens hitting the bottom of the screen.
    check_aliens_bottom(ai_settings, screen, stats, sb, ship, aliens, bullets, mothership)

def get_number_aliens_x(ai_settings, alien_width):
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x

def get_number_rows(ai_settings, ship_height, alien_height):
    available_space_y = (ai_settings.screen_height -
                            (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows

def update_mothership(ai_settings, screen, stats, sb, ship, aliens, bullets, mothership):
    check_mothership_edges(ai_settings, mothership)
    mothership.update()

def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = (alien.rect.height + 2 * alien.rect.height * row_number) + 80
    aliens.add(alien)


def create_fleet(ai_settings, screen, ship, aliens):
    # Create an alien, and find number of aliens in a row.
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height,
        alien.rect.height) - 5


    # Create the fleet of aliens.
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number,
                row_number)
