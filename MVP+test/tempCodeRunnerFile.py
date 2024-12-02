import pygame
from settings import *
from player import *
from level import *
from settings import level_map
import os

# Initialisation de Pygame
pygame.init()

# Création de la fenêtre de jeu
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption(nom_jeu)
g = os.path.join('projet','MVP','background5.png')
bg = pygame.image.load(g).convert()


# Initialisation de l'horloge pour gérer le taux de rafraîchissement
clock = pygame.time.Clock()

# Initialisation du niveau avec une carte et la surface d'affichage
level = Level(level_map, screen)
run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
    
    # Remplissage de l'écran avec une couleur noire
    # Appel à la méthode pour dessiner le niveau
    level.draw_level(bg)

    # Mise à jour de l'affichage de l'écran
    pygame.display.update()

    # Limite le taux de rafraîchissement de l'écran
    clock.tick(fps)

# Fermeture de Pygame
pygame.quit()