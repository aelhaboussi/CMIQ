import pygame
from settings import *


class Player(pygame.sprite.Sprite):
    """
    Classe représentant le joueur dans le jeu.

    Attributes:
        x (int): Position horizontale initiale du joueur.
        y (int): Position verticale initiale du joueur.
        terre

    Methods:
        jump(): Fait sauter le joueur si celui-ci est au sol.
        apply_gravity(): Applique la gravité au joueur.
        entree_joueur(): Gère les entrées du joueur (mouvements et saut).
        etat_joueur(): Détermine l'état actuel du joueur (immobile, en mouvement, en saut).
        update(): Met à jour les états et les actions du joueur en fonction des entrées.
    """

    def __init__(self, x, y):
        """
        Initialise un joueur avec une position et des caractéristiques de mouvement.

        Args:
            x (int): Position horizontale initiale du joueur.
            y (int): Position verticale initiale du joueur.
        """
        super().__init__()
        self.image = pygame.Surface((tile_size, 64))
        self.image.fill("red")
        self.rect = self.image.get_rect(topleft=(x, y))
        self.v = vitesse_joueur
        self.gravity = GRAVITY
        self.direction = pygame.math.Vector2(0, 0)
        self.jump_speed = jump_speed
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.face = "right"
        self.terre = False
        

    def jump(self):
        """Fait sauter le joueur si celui-ci est au sol."""
        self.direction.y = self.jump_speed

    def apply_gravity(self):
        """Applique la gravité au joueur."""
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def entree_joueur(self):
        """Gère les entrées du joueur (mouvements et saut)."""
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.direction.x = -1
        elif keys[pygame.K_RIGHT]:
            self.direction.x = 1
        else:
            self.direction.x = 0
        if keys[pygame.K_SPACE]:
            if self.terre:
                self.jump()

    def etat_joueur(self):
        """
        Détermine l'état actuel du joueur (immobile, en mouvement, en saut).
        """
        if self.direction.y < 0:
            self.status = "jumping"
        elif self.direction.y > self.gravity:
            self.status = "fall"
        elif self.direction.x != 0:
            if self.direction.x == 1:
                self.face = "right"
            else:
                self.face = "left"
            self.status = "run"
        else:
            self.status = "idle"

    def update(self):
        """Met à jour les états et les actions du joueur en fonction des entrées."""
        self.entree_joueur()
        self.etat_joueur()



class Bull(pygame.sprite.Sprite):
    """
        Initialise un taureau qui se déplace à une vitesse constante.

        Args:
            x (int): Position initiale en x.
            y (int): Position initiale en y.
            width (int): Largeur du rectangle.
            height (int): Hauteur du rectangle.
            vel (int): Vitesse constante de déplacement en pixels par frame.
        """
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pygame.Surface((tile_size, 64))
        self.image.fill("grey")
        self.x = x
        self.y = y
        self.rect = self.image.get_rect(topleft=(self.x, self.y))
        self.width = width
        self.height = height
        self.vel = vitesse_joueur              # Speed of the bull
        
    
    
    def entree_(self,level):
        """Gère les mouvement du taureau en fonction des entrées du joueur (mouvements droit ,gauche et collision horizentales)."""
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.vel = vitesse_joueur + 2
        elif keys[pygame.K_RIGHT]:
            if self.rect.x>0 and not(level.isincollisionh):
                self.vel= (-2)
            elif level.isincollisionh:
                self.vel =vitesse_joueur
            else:
                self.vel =0
        else:
            self.vel = vitesse_joueur
    def update(self,level):
        """Mettre à jour les taureau"""
        self.entree_(level)
        self.rect.x +=self.vel


        
