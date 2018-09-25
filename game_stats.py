import settings

class GameStats():

    def __init__(self, ai_settings):
        self.ai_settings = ai_settings
        self.reset_stats()

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
        self.score = 0
        self.level = 1
