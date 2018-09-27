import pygame as pg
import sys

from game_stats import GameStats
from scoreboard import Scoreboard
from settings import Settings


def startScoreboard():
    ai_settings = Settings()
    stats = GameStats(ai_settings)
    pg.init()
    (width, height) = (400, 300)
    screen = pg.display.set_mode((width, height))
    pg.display.set_caption('Enter player name')
    font = pg.font.Font(None, 32)
    clock = pg.time.Clock()
    input_box = pg.Rect(100, 100, 140, 32)
    color_inactive = pg.Color('lightskyblue3')
    color_active = pg.Color('dodgerblue2')
    color = color_inactive
    active = False
    text = ''
    done = False

    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True
                exit(0)
            if event.type == pg.MOUSEBUTTONDOWN:
                # If the user clicked on the input_box rect.
                if input_box.collidepoint(event.pos):
                    # Toggle the active variable.
                    active = not active
                else:
                    active = False
                # Change the current color of the input box.
                color = color_active if active else color_inactive
            if event.type == pg.KEYDOWN:
                if active:
                    if event.key == pg.K_RETURN:
                        global playername
                        playername = text
                        print(text)
                        global playerscore
                        playerscore = str(ai_settings.finalscore)
                        print(playerscore)

                        if playername in ai_settings.playerlist:
                            global dupindex
                            dupindex = ai_settings.playerlist.index(playername)
                            print("playername: " + str(playername) + " in list: " + str(ai_settings.playerlist[dupindex]))
                            if stats.intscorelist[dupindex] <= int(playerscore):
                                print("great or equal")
                                del stats.intscorelist[dupindex]
                                ai_settings.playerlist.remove(playername)
                                playerscore = str(playerscore) + "\n"
                                with open('scores.txt', 'a') as writenewscore:
                                    writenewscore.write(playername + ":" + playerscore)
                                ai_settings.playerscores[str(playername)] = str(playerscore)
                                playerscore = int(ai_settings.finalscore)
                                print(stats.intscorelist)
                                print(ai_settings.playerlist)
                                print(type(playerscore))
                                stats.intscorelist.append(playerscore)
                                ai_settings.playerlist.append(playername)
                            elif stats.intscorelist[dupindex] > int(playerscore):
                                print("less than")
                                playerscore = stats.intscorelist[dupindex]
                                print(stats.intscorelist)
                                print(ai_settings.playerlist)
                                print(type(playerscore))



                        global intscorelist
                        intscorelist = [int(s) for s in stats.intscorelist]
                        print(stats.intscorelist)
                        print(intscorelist)
                        global highscore
                        global highplayer
                        highscore = max(intscorelist)
                        print(highscore)
                        # keys=list(ai_settings.playerscores.keys())
                        # print(keys)
                        # values=list(ai_settings.playerscores.values())
                        global indexhigh
                        indexhigh = intscorelist.index(highscore)
                        highplayer = ai_settings.playerlist[indexhigh]
                        print(highplayer)


                        # indexhigh = ai_settings.playerscores.get()


                        openboard()
                        # player name entered


                    elif event.key == pg.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode

        screen.fill((30, 30, 30))
        # Render the current text.
        txt_surface = font.render(text, True, color)
        # Resize the box if the text is too long.
        width = max(200, txt_surface.get_width()+10)
        input_box.w = width
        # Blit the text.
        screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
        # Blit the input_box rect.
        pg.draw.rect(screen, color, input_box, 2)

        pg.display.flip()
        clock.tick(30)



def openboard():
    DEMO_highplayer = 'Wan'
    DEMO_highscore = 200
    DEMO_dictlist = {'Gabe': 145, 'Wan': 200, 'John': 132, 'Mary': 133}
    DEMO_playernamelist = ['Wan', 'Gabe', 'Mary', 'John']
    DEMO_scorelist = [200,145,133,132]

    ai_settings = Settings()
    stats = GameStats(ai_settings)
    pg.init()#never forget this line
    color_inactive = pg.Color('lightskyblue3')
    color_active = pg.Color('dodgerblue2')
    color_white = pg.Color('white')
    color_red = pg.Color('red')
    color_yellow = pg.Color(255,255,112)
    color = color_active
    window=pg.display.set_mode((400, 500))
    titlefont=pg.font.SysFont(None, 42)
    highscorefont=pg.font.SysFont(None, 50)
    regfont=pg.font.SysFont(None, 38)

    windowrect = window.get_rect()
    windowwidth = windowrect.width
    window.fill((0, 0, 0))

    highscoretitletext=highscorefont.render('HIGHSCORES', True, color_white, (0, 0, 0))
    highscorerect=highscoretitletext.get_rect()
    highscorerect.y = 5
    highscorey = highscorerect.y
    print(highscorey)
    highscoreheight = highscorerect.height
    print(highscoreheight)
    highscorerect.centerx = windowwidth / 2
    window.blit(highscoretitletext, highscorerect)

    # playerhighscore=highscorefont.render(DEMO_highplayer.upper() + " : " + str(DEMO_highscore), True, color_red, (0, 0, 0))
    # playerhighscorerect=playerhighscore.get_rect()
    # playerhighscorerect.y = highscorerect.y + playerhighscorerect.height + 5
    # playerhighscorerect.centerx = windowwidth / 2
    # window.blit(playerhighscore, playerhighscorerect)

    ai_settings.playerscores.clear()

    global intscorelist

    #intscorelist, ai_settings.playerlist = zip(*sorted(zip(intscorelist, ai_settings.playerlist)))
    intscorelist, ai_settings.playerlist = (list(t) for t in zip(*sorted(zip(intscorelist, ai_settings.playerlist))))
    print("non reversed: ")
    print(*intscorelist, sep=', ')
    print("non reversed: ")
    print(*ai_settings.playerlist, sep=', ')
    intscorelist.reverse()
    ai_settings.playerlist.reverse()
    print(" reversed: ")
    print(*intscorelist, sep=', ')
    print(" reversed: ")
    print(*ai_settings.playerlist, sep=', ')

    # global final_player_list
    # final_player_list = []
    # global final_score_list
    # final_score_list = []
    # global duplicate_index
    # global new_index
    # for num in ai_settings.playerlist:
    #     duplicate_index = ai_settings.playerlist.index(num)
    #     if num not in final_player_list:
    #         final_player_list.append(num)
    #         final_score_list.append(intscorelist[duplicate_index])
    #         new_index = final_player_list.index(num)
    #         ai_settings.playerlist.remove(num)
    #         del intscorelist[duplicate_index]
    #
    #         while True:
    #             if num in ai_settings.playerlist:
    #                 if int(final_score_list[new_index]) > int(intscorelist[duplicate_index]):
    #                     ai_settings.playerlist.remove(num)
    #                     del intscorelist[duplicate_index]
    #                 elif int(final_score_list[new_index]) == int(intscorelist[duplicate_index]):
    #                     ai_settings.playerlist.remove(num)
    #                     del intscorelist[duplicate_index]
    #                 elif int(final_score_list[new_index]) < int(intscorelist[duplicate_index]):
    #                     final_player_list.remove(num)
    #                     del final_score_list[new_index]
    #                     final_player_list.append(num)
    #                     final_score_list.append(intscorelist[duplicate_index])
    #                     ai_settings.playerlist.remove(num)
    #                     del intscorelist[duplicate_index]
    #             else:
    #                 break
    #
    # print("final lists: ")
    # print(*final_player_list,sep=', ')
    # print(*final_score_list,sep=', ')
    #


    for z in range(len(intscorelist)):
        print("z: " + str(z))
        print("ai_settings.playerscores: " + str(ai_settings.playerscores))
        ai_settings.playerscores[ai_settings.playerlist[z]] = intscorelist[z]

    print(ai_settings.playerscores)

    placenum = 1
    placenumstr = ""
    currentypos = highscorey + 5
    print(" PLACE   NAME   SCORE    ")

    totalwindowx = windowrect.width - 30
    totalplacex = totalwindowx * 0.2
    totalnamex = totalwindowx * 0.45
    totalscorex = totalwindowx * 0.35
    placestartx = 20
    namestartx = totalplacex + totalplacex
    scorestartx = 40 + totalplacex + totalnamex


    placelabel=regfont.render("PLACE", True, color_white, (0, 0, 0))
    placelabelrect=placelabel.get_rect()
    placelabelrect.y = currentypos + placelabelrect.height + 10
    print(currentypos)
    print(int(placelabelrect.y))
    print(currentypos)
    placelabelrect.x = placestartx
    window.blit(placelabel, placelabelrect)

    namelabel=regfont.render("NAME", True, color_white, (0, 0, 0))
    namelabelrect=namelabel.get_rect()
    namelabelrect.y = currentypos + namelabelrect.height + 10
    print(currentypos)
    print(int(namelabelrect.y))
    print(currentypos)
    namelabelrect.x = namestartx
    window.blit(namelabel, namelabelrect)

    scorelabel=regfont.render("SCORE", True, color_white, (0, 0, 0))
    scorelabelrect=scorelabel.get_rect()
    scorelabelrect.y = currentypos + scorelabelrect.height + 10
    print(currentypos)
    print(int(scorelabelrect.y))
    print(currentypos)
    scorelabelrect.x = scorestartx
    window.blit(scorelabel, scorelabelrect)

    pg.draw.line(window, (255, 255, 255), (0, placelabelrect.y + placelabelrect.height), (windowrect.width, placelabelrect.y + placelabelrect.height))


    for x in ai_settings.playerscores.keys():
        if placenum == 1:
            placenumstr = str(placenum) + "st. "
        elif placenum == 2:
            placenumstr = str(placenum) + "nd. "
        elif placenum == 3:
            placenumstr = str(placenum) + "rd. "
        else:
            placenumstr = str(placenum) + "th. "

        print(" " + placenumstr + "  " + x + "   " + "   " + str(ai_settings.playerscores[x]))

        if x == playername:
            print("x is playername")
            placenumber=regfont.render(placenumstr, True, color_yellow, (0, 0, 0))
        else:
            placenumber=regfont.render(placenumstr, True, color_white, (0, 0, 0))
        placenumberrect=placenumber.get_rect()
        placenumberrect.y = ((placenum + 1) * (currentypos + placenumberrect.height + 10))
        print(currentypos)
        print(int(placenumberrect.y))
        print(currentypos)
        placenumberrect.x = placestartx
        window.blit(placenumber, placenumberrect)


        if x == playername:
            print("x is playername")
            namenumber=regfont.render(x, True, color_yellow, (0, 0, 0))
        else:
            namenumber=regfont.render(x, True, color_white, (0, 0, 0))
        namenumberrect=namenumber.get_rect()
        namenumberrect.y = ((placenum + 1) * (currentypos + namenumberrect.height + 10))
        print(currentypos)
        print(int(namenumberrect.y))
        print(currentypos)
        namenumberrect.x = namestartx
        window.blit(namenumber, namenumberrect)


        if x == playername:
            print("x is playername")
            scorenumber=regfont.render(str(ai_settings.playerscores[x]), True, color_yellow, (0, 0, 0))
        else:
            scorenumber=regfont.render(str(ai_settings.playerscores[x]), True, color_white, (0, 0, 0))
        scorenumberrect=scorenumber.get_rect()
        scorenumberrect.y = ((placenum + 1) * (currentypos + scorenumberrect.height + 10))
        print(currentypos)
        print(int(scorenumberrect.y))
        print(currentypos)
        scorenumberrect.x = scorestartx
        window.blit(scorenumber, scorenumberrect)

        placenum = placenum + 1





    pg.display.update()
    while True:
        for event in pg.event.get():
            if event.type==pg.QUIT:
                pg.quit()
                sys.exit()


####
startScoreboard()
