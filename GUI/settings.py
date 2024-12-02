import pygame
class Settings:
    def __init__(self):
        self.GRAVITY=1
        self.vitesse_joueur = 6
        self.nom_jeu = "CATCH ME ILA QEDDITI"
        self.jump_speed = -20
        self.fps = 60
        self.level_map = [[
    "G                                                                                                                                                                            Y",
    "G                                                                                                                                                                            Y",
    "G                                                                                                                                                                            Y",
    "G                        1                                 1                                       1                                1                                1       Y",
    "G                               0                                                0                                                 1                                       Y Y",
    "G              X     X      XX  XX             0        X       X       X    1   XX   1    X           X   0       X          X          X         X              XX       Y Y",
    "G    P   0  X  X     X  X   XX  XX  X    XX    XX       X       X0      X        XX   X    X     0     X  XX       X    0     X1         X         X     0         XX   1   YYY",
    "GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG"
], [
    "G                                                                                                                             W                   S               W          Y",
    "G                                                              111111                                    11                                                                  Y",
    "G                                                              XXXXXX                     0                         S                                  M                     Y",
    "G            S X  0     1       0               A        XX    XXXXXX         1         XXXX         XX             X        A           1    X       XXX                    Y",
    "G              X        X      XXX  X          XXX       XX 0                XXX        X          B                X                    M    X   X                        Y Y",
    "G           X  X     X  X      XXX  X     XX   XXX     XXXX               0        XX   X                      XX   X                         X                            Y Y",
    "G    P   0  X  X     X  X   XXXXXX  X  M  XX    XX     XXXX    1   0      X        XX 1 X                      XX   X         1               X   11  11   11              YYY",
    "GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG"
]]
        self.tile_size = 50
        self.coin_size = 40
        self.screen_height=500
        self.screen_width = 800



parametres=Settings()


    








#screen_height = len(level_map) * tile_size
