# import des modules et classes
import pygame
from settings import parametres
from buttons import*

pygame.init()
vitesse_boat = 0.25                                                     # vitesse d'animation du bateau

# Création de la fenêtre de jeu
screen = pygame.display.set_mode((parametres.screen_width, parametres.screen_height))
pygame.display.set_caption(parametres.nom_jeu)

# initialisation des variables de position et transparence
x,y =(0,0)
transparance = 0

# chargement et configuration des icons des bouttons
replay_button = button('graphics/end_screen/replay_button_normal.png','graphics/end_screen/replay_button_hover.png')
replay_button.resize(230,90)
replay_rect = replay_button.rect((parametres.screen_width//2,parametres.screen_height//1.7))  # Center the button

levels_button = button('graphics/game_won_icons/levels_normal.png','graphics/game_won_icons/levels_hover.png')  
levels_button.resize(230,90)
levels_rect = levels_button.rect((parametres.screen_width//2,parametres.screen_height//1.3))  # Center the button

# chargement et configuration des images
runner_inboat = pygame.image.load('graphics/game_won_icons/runner_inboat.png').convert_alpha()
win_background = pygame.image.load('graphics/game_won_icons/win_background.png').convert_alpha()
won_icone = pygame.image.load('graphics/game_won_icons/won_icone.png').convert_alpha()

# Définir les rectangles pour centrer les images
runner_inboat_rect = runner_inboat.get_rect(center=(parametres.screen_width // 2, parametres.screen_height // 2))
win_background_rect = win_background.get_rect(center=(parametres.screen_width // 2, parametres.screen_height // 2))
won_icone_rect = won_icone.get_rect(center=(parametres.screen_width // 2, parametres.screen_height // 2))

run = True

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
                
        if event.type == pygame.MOUSEBUTTONDOWN :
             # au cas d'un click sur le boutton "PLAY AGAIN"
            if replay_rect.collidepoint(event.pos):
                run = False
                # ouverture du fichier main.py qui relance le jeu
                with open("GUI/main.py") as f:
                    code = f.read()
                    exec(code)  
                    
        if event.type == pygame.MOUSEBUTTONDOWN :
            # au cas d'un click sur le boutton "LEVEL"
            if levels_rect.collidepoint(event.pos):
                run = False
                # ouverture du fichier select_level.py qui relance l'écran de choix du niveau
                with open("GUI/select_level.py") as f:
                    code = f.read()
                    exec(code)  
                       
    # vérifie si la souris est sur le boutton           
    mouse_pos = pygame.mouse.get_pos()       # donne la position actuelle de la souris
    
    if replay_rect.collidepoint(mouse_pos):  # si la souris est sur le boutton
        replay_button.is_hovered = True
    else:
        replay_button.is_hovered = False 
        
    if levels_rect.collidepoint(mouse_pos):  # si la souris est sur le boutton
        levels_button.is_hovered = True
    else:
        levels_button.is_hovered = False         
                
    if x < 460 :                             # tant que le bateau est sur l'écran
        x += vitesse_boat
        screen.blit(win_background,(0,y))            
        screen.blit(runner_inboat,(x,y))
    else:    
        # affichage progressive de l'écran de victoire                                
        screen.blit(win_background,(0,y))           
        screen.blit(won_icone,(0,-100))
        transparance+=1
        if transparance > 255 :
            transparance = 255
            
        # affichage des élements de l'écran
        won_icone.set_alpha(transparance)
        font = pygame.font.Font("pixel_font.ttf", 36)                   # configuration du font du texte
            # affichage du score
        text_button = font.render(str(level.score), True, (0,0,0))
        text_button.set_alpha(transparance) 
        screen.blit(text_button,(494, 182))
        
            # affichage des bouttons
        replay_button.draw(screen, replay_rect.topleft)
        levels_button.draw(screen, levels_rect.topleft)    

    # mise à jour de l'écran
    pygame.display.update()           
                
                
pygame.quit()