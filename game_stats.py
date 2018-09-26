import settings

class GameStats():

    def __init__(self, ai_settings):
        self.ai_settings = ai_settings

        self.reset_stats()
        try:
            print("game: reg: " + str(self.score))
        except AttributeError as error:
            print("att error 2")
        except Exception as exception:
            print("except error 2")
        try:
            print("game: final: " + str(ai_settings.finalscore))
        except AttributeError as error:
            print("att error")
        except Exception as exception:
            print("except error")

        # Start game in an inactive state.
        self.game_active = False

        # High score should never be reset.
        if(max(ai_settings.scorelist) == None or max(ai_settings.scorelist) == "" or int(max(ai_settings.scorelist))< int(self.score)):
            self.high_score_player = "You"
            self.high_score = 0
        else:
            self.high_score = int(max(ai_settings.scorelist))
            print(ai_settings.scorelist)
            self.high_index = ai_settings.scorelist.index(str(self.high_score))
            self.high_score_player = ai_settings.playerlist[self.high_index]

    def reset_stats(self):
        self.ships_left = self.ai_settings.ship_limit
        try:
            print("reset stats: " + str(self.score))
        except AttributeError:
            None
        try:
            if self.score != 0:
                print("score not 0")
            else:
                self.score = 0
        except AttributeError as error:
            print("att error reset")
            self.score = 0
        except Exception as exception:
            print("except error reset")
            self.score = 0

        self.level = 1
