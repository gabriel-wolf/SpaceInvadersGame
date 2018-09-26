import pygame

class Settings():

    def __init__(self):
        readalineImageSettings = open("alienimage.txt", mode='r+')
        readimageLines = readalineImageSettings.readlines()
        print(readimageLines)
        if "True" in readimageLines:
            self.specialalienson = True
            pygame.display.set_caption("Space Invaders BARTEL EDITION")
        else:
            self.specialalienson = False
            pygame.display.set_caption("Space Invaders")
        readalineImageSettings.close()

        self.rapidfire = False
        try:
            if self.finalscore == None:
                print("SETTING FINAL SCORE")
                self.finalscore = 666
            else:
                print("not setting score because already set")
        except AttributeError as error:
            print("att error set")
        except Exception as exception:
            print("except error set")


        self.playerlist = []
        self.scorelist = []
        self.playerscores = {}
        with open('scores.txt') as f:
            for line in f:
                currplayer, currscore = line.strip().split(':')
                print(type(currscore))
                self.playerscores[currplayer] = currscore
                self.scorelist.append(currscore)
                self.playerlist.append(currplayer)


        # Screen settings.
        self.screen_width = 350 #int((1200 / 1.5))
        self.screen_height = 450 #int((800 / 1.5))
        self.bg_color = (0, 0, 0)

        # Ship settings.
        self.ship_limit = 1 ####3

        # Bullet settings.
        self.bullet_width = 2.5 #int((3 / 1.5))
        self.bullet_height = 10 #int(15 /1.5)
        self.bullet_color = 255, 255, 255
        if self.rapidfire == True:
            self.bullets_allowed = 10
        else:
            self.bullets_allowed = 3


        # Alien settings.
        self.fleet_drop_speed = 8

        # How quickly the game speeds up.
        self.speedup_scale = 1.1
        # How quickly the alien point values increase.
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def setbulletsettings(self):
        if self.rapidfire == True:
            self.bullets_allowed = 10
        else:
            self.bullets_allowed = 3
        if self.rapidfire == True:
            self.bullet_speed_factor = 15
        else:
            self.bullet_speed_factor = 5

    def initialize_dynamic_settings(self):
        if self.rapidfire == True:
            self.bullets_allowed = 10
        else:
            self.bullets_allowed = 3

        self.ship_speed_factor = 2.4
        if self.rapidfire == True:
            self.bullet_speed_factor = 15
        else:
            self.bullet_speed_factor = 5
        self.alien_speed_factor = 10 ######0.75
        self.mothership_speed_factor = 0.5

        # Scoring.
        self.alien_points = 50

        # fleet_direction of 1 represents right, -1 represents left.
        self.fleet_direction = 1
        self.mothership_direction = 1

    def increase_speed(self):
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale * 1.2

        self.alien_points = int(self.alien_points * self.score_scale)
