# import des modules et classes
from buttons import *
from settings import parametres


def display():
    """
    mis à jour l'affichage de l'écran
    """
    bg.draw(win, (0, 0))
    play_button.draw(win, play_rect.topleft) 
    game_name.draw(win, game_name_rect.topleft)
    sound_button.draw(win, (25,25))
    pygame.display.update()

file_path = "GUI/select_level.py"                        # chemin relatif du fichier select_level.py

# initialisation de pygame
pygame.init()
pygame.mixer.init()

# configuration de la music du jeu
pygame.mixer.music.load("music/track1.mp3")              # chargement du fichier de la music
pygame.mixer.music.set_volume(1.0)                       # configuration du volume
pygame.mixer.music.play(-1)                              # le -1 signifie que la music se joue infiniment

# configuration de la fenêtre
win = pygame.display.set_mode((parametres.screen_width, parametres.screen_height))
pygame.display.set_caption(parametres.nom_jeu)
# souris predéfinie
pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_CROSSHAIR)

# chargement et configuration de l'arrière plan
bg = button('graphics/images_start_screen/resized_image.png','graphics/images_start_screen/resized_image.png')
bg.resize(parametres.screen_width, parametres.screen_height)
bg_rect = bg.rect((parametres.screen_width // 2, parametres.screen_height // 2))

# chargement et configuration des icons des bouttons
play_button = button('graphics/images_start_screen/button_normal.png','graphics/images_start_screen/button_hover.png')
play_button.resize(200,90)
play_rect = play_button.rect((parametres.screen_width//2, parametres.screen_height//1.5))

sound_on_button = button("graphics/images_start_screen/sound_on.png","graphics/images_start_screen/sound_hover.png")
sound_on_button.resize(50, 50)
sound_rect = sound_on_button.rect((50,50))

sound_mute_button = button("graphics/images_start_screen/sound_off.png","graphics/images_start_screen/sound_off.png")
sound_mute_button.resize(50, 50)

game_name = button("graphics/images_start_screen/game_name.png","graphics/images_start_screen/game_name.png")
# chargement et configuration de l'image du nom du jeuG
game_name = button("graphics/images_start_screen/game_name.png","graphics/images_start_screen/game_name.png")
game_name.resize(400, 200)
game_name_rect = game_name.rect((parametres.screen_width//2, parametres.screen_height//4))

# initialisation du boutton de son à l'état ON
sound_button = sound_on_button
sound_on = True

# boucle d'éxecution
run = True
while run:
    for event in pygame.event.get():
        # fermeture de l'écran par le boutton X de la fenêtre
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            pygame.mixer.music.stop()           
            quit()
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            if play_rect.collidepoint(event.pos):
                # au cas d'un click sur le boutton "START"
                run = False
                # ouverture du fichier qui contient l'écran de selection du niveau
                with open(file_path) as f:
                    code = f.read()
                    exec(code)
                
            if sound_rect.collidepoint(event.pos) and sound_on:
                # au cas d'un click sur le boutton du son à l'état ON
                sound_button = sound_mute_button
                sound_on = False
                pygame.mixer.music.pause()
                
            elif sound_rect.collidepoint(event.pos) and not sound_on:
                # au cas d'un click sur le boutton du son à l'état OFF
                sound_button = sound_on_button
                sound_on = True
                pygame.mixer.music.unpause()
                    
    # vérifie si la souris est sur le boutton
    mouse_pos = pygame.mouse.get_pos()  # donne la position actuelle de la souris
    if play_rect.collidepoint(mouse_pos):  # si la souris est sur le boutton
        play_button.is_hovered = True
    else:
        play_button.is_hovered = False
        
    if sound_rect.collidepoint(mouse_pos) and sound_on:  # If mouse is over the button
        sound_button.is_hovered = True
    elif sound_rect.collidepoint(mouse_pos) and not sound_on:
        sound_button.is_hovered = True
    elif sound_on:
        sound_button.is_hovered = False
        
    # affichage
    display()                
    
    
pygame.quit()
