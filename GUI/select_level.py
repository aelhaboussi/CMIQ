# import des modules et classes
import pygame
from settings import parametres
from buttons import *

file_path = "GUI/main.py"                 # chemin relatif du fichier main.py

# initialisation de pygame
pygame.init()

screen = pygame.display.set_mode((parametres.screen_width, parametres.screen_height))
screen = pygame.display.set_mode((parametres.screen_width, parametres.screen_height))                 # configuration de la fenêtre

bg = button('graphics/images_start_screen/resized_image.png','graphics/images_start_screen/resized_image.png')
bg.resize(parametres.screen_width, parametres.screen_height)  # Scale background to fit the window size
bg_rect = bg.rect((parametres.screen_width // 2, parametres.screen_height // 2))
# chargement et configuration de l'arrière plan
bg = button('graphics/images_start_screen/resized_image.png','graphics/images_start_screen/resized_image.png')
bg.resize(parametres.screen_width, parametres.screen_height)  # Scale background to fit the window size
bg_rect = bg.rect((parametres.screen_width // 2, parametres.screen_height // 2))

level1_button= button('graphics/images_start_screen/level1_normal.png','graphics/images_start_screen/level1_hover.png')
level1_rect = level1_button.rect((parametres.screen_width//2,100))  # Center the button
# chargement et configuration des icons des bouttons
level1_button= button('graphics/images_start_screen/level1_normal.png','graphics/images_start_screen/level1_hover.png')
level1_rect = level1_button.rect((parametres.screen_width//2,100))  # Center the button

level2_button = button('graphics/images_start_screen/level2_normal.png','graphics/images_start_screen/level2_hover.png')
level2_rect = level1_button.rect((parametres.screen_width//2,180))  # Center the button

# initialisation du niveau à 0 et de la variable "run"
level_slct = 0
run = True

# boucle d'éxecution
while run:   
    for event in pygame.event.get():
        # fermeture de l'écran par le boutton X de la fenêtre
        if event.type == pygame.QUIT:
            run = False
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            # au cas d'un click sur le boutton "LEVEL 1"
            if level1_rect.collidepoint(event.pos):
                run = False
                level_slct = 0
                # ouverture du fichier du jeu avec le niveau 0
                with open(file_path) as f:
                    code = f.read()
                    exec(code)
                    
            elif level2_rect.collidepoint(event.pos):
                # au cas d'un click sur le boutton "LEVEL 2"
                run = False
                level_slct = 1
                # ouverture du fichier du jeu avec le niveau 0
                with open(file_path) as f:
                    code = f.read()
                    exec(code)
                    
    # vérifie si la souris est sur le boutton
    mouse_pos = pygame.mouse.get_pos()  # donne la position actuelle de la souris
    if level1_rect.collidepoint(mouse_pos):  # si la souris est sur le boutton
        level1_button.is_hovered = True
    else:
        level1_button.is_hovered = False
        
    if level2_rect.collidepoint(mouse_pos):  # si la souris est sur le boutton
        level2_button.is_hovered = True
    else:
        level2_button.is_hovered = False
        
    # affichage des élements de l'écran
    bg.draw(screen, (0,0))
    level1_button.draw(screen, level1_rect.topleft)
    level2_button.draw(screen, level2_rect.topleft)
         
    pygame.display.update()
            

pygame.quit()