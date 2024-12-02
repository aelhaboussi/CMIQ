# import des modules et classes
import pygame
from settings import parametres
from player import *
from level import *
import os
from buttons import *

# Initialisation de Pygame
pygame.init()

file_path = "GUI/main.py"               # chemin relatif du fichier main.py

# Création de la fenêtre de jeu
screen = pygame.display.set_mode((parametres.screen_width, parametres.screen_height))
pygame.display.set_caption(parametres.nom_jeu)
g = os.path.join("graphics","backgrounds", "background5.png")
bg = pygame.image.load(g).convert()

# Chargement des images des boutons
replay_button = button('graphics/end_screen/replay_button_normal.png','graphics/end_screen/replay_button_hover.png')
replay_button.resize(230,90)
replay_rect = replay_button.rect((parametres.screen_width//2,parametres.screen_height//1.5))  # Position centrale du bouton

pause_screen = pygame.image.load('graphics/pause_screen/pause_icon.png').convert_alpha()
pause_screen_rect = pause_screen.get_rect(center=(parametres.screen_width // 2, parametres.screen_height // 2))

# Initialisation de l'horloge pour gérer le taux de rafraîchissement
clock = pygame.time.Clock()

# Initialisation du niveau avec une carte et la surface d'affichage
level = Level(parametres.level_map[level_slct], screen)
paused = False
run = True
level.wahd(bg)

# boucle d'éxecution
while run:
    for event in pygame.event.get():
        # fermeture de l'écran par le boutton X de la fenêtre
        if event.type == pygame.QUIT:
            run = False
            
        if event.type == pygame.KEYDOWN:
            # fermeture de l'écran par le boutton "ECHAPE"
            if event.key == pygame.K_ESCAPE:
                run = False
                
        if event.type == pygame.KEYDOWN:
            # au cas d'un click sur le boutton "P"
            if event.key == pygame.K_p:
                if not paused and not level.isgameover:  # si le jeu est ni perdue ni en pause, le jeu se met en pause
                    level.pause = True
                    paused = True
                else:                       # si le jeu est en pause, le jeu se reprend
                    level.pause = False
                    paused = False
                    
        if event.type == pygame.MOUSEBUTTONDOWN and (level.isgameover or level.win):
            # au cas d'un click sur le boutton "PLAY AGAIN" dans le cas d'une perte ou d'une vectoire
            if replay_rect.collidepoint(event.pos):
                run = False
                # ouverture du fichier main.py qui relance le jeu
                with open(file_path) as f:
                    code = f.read()
                    exec(code)
    
    # Appel à la méthode pour dessiner le niveau
    level.draw_level(bg)
    
    if level.isgameover:
        # Gestion de l'état "game over" : vérifie si la souris survole le bouton
        level.pause = True
        mouse_pos = pygame.mouse.get_pos()  # Récupération de la position actuelle de la souris
        if replay_rect.collidepoint(mouse_pos):  # Si la souris survole le bouton
            replay_button.is_hovered = False
        else:
            replay_button.is_hovered = True
            
        replay_button.draw(screen, replay_rect.topleft)
    
    if level.win:
        # Gestion de l'état "victoire" : exécution d'un autre script
        with open("GUI/youwon.py") as f:
            code = f.read()
            exec(code)
            
    # Affichage de l'écran de pause
    if paused:
        screen.blit(pause_screen, pause_screen_rect.topleft)
    
    pygame.display.update()

    # Limitation du taux de rafraîchissement de l'écran
    clock.tick(parametres.fps)

# Fermeture de Pygame
pygame.quit()
