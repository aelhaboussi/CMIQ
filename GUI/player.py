import pygame
from settings import parametres
import random
from audio import *
from import_images import import_images
run_folder_path = "./graphics/runner_animation/dust_particles/run"

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y,surface):
        """
        Initialise un objet Player.
        Args:
        - x (int): Position x initiale du joueur.
        - y (int): Position y initiale du joueur.
        - surface (pygame.Surface): Surface d'affichage du joueur.
        - jump_particules (function): Fonction pour générer des particules de saut.
        """
        super().__init__()
        self.import_character_assets()
        self.x=x
        self.y=y
        self.surface = surface
        self.terre = False
        self.image = pygame.Surface((2*parametres.tile_size, 2*64))
        self.image.fill("red")
        self.rect = self.image.get_rect(topleft=(x, y))
        self.gravity = parametres.GRAVITY
        self.direction = pygame.math.Vector2(0, 0)
        self.jump_speed = parametres.jump_speed
        self.face = "right"
        self.particles=[]
        self.particle_timer = 0
        self.width=50
        self.height=64
        self.v=parametres.vitesse_joueur
        self.status="idle"
        self.terre = False
        self.animation_speed = 0.1
        self.frame_index=0
        self.has_shield = False  # Indique si le joueur a un bouclier
        self.is_magnet_active = False  # Le magnétisme est inactif au début
        self.magnet_range = 250  # Portée du magnétisme
        self.magnet_duration = 5000  # Durée du magnet (en millisecondes)
        self.magnet_timer = 0  # Timer pour gérer l'expiration du magnet
        
            
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
                music('./music/jumping.wav',0.5)

    def etat_joueur(self):
        """
        Détermine l'état actuel du joueur (immobile, en mouvement, en saut).
        """
        if self.direction.y < 0:
            self.status = "jumping"
        #elif self.direction.y > self.gravity:
        #    self.status = "fall"
        elif self.direction.x != 0:
            if self.direction.x == 1:
                self.face = "right"
            else:
                self.face = "left"
            self.status = "run"
        else:
            self.status = "idle"
            #if not self.terre:
            #  self.status = "fall"
        
    def import_character_assets(self):
        """
        Importe les images pour les différentes animations du personnage.
        """
        character_path = "./graphics/runner_animation"
        self.animations = {"idle": [], "run": [], "jumping": [], "fall": []}
        scale = 2
        for animation in self.animations.keys():
            full_path = f"{character_path}/{animation}/"
            animation_images = import_images(full_path)
            scaled_images = [
                pygame.transform.scale(
                    image, (parametres.tile_size*scale, 64*scale)
                )
                for image in animation_images
            ]
            self.animations[animation] = scaled_images

    def animate(self):
        """
        Anime le joueur en fonction de son état (immobile, course, saut, chute).
        """
        animation = self.animations[self.status]

        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0

        image = animation[int(self.frame_index)]
        if self.face == "right":
            self.image = image
        else:
            flipped_image = pygame.transform.flip(image, True, False)
            self.image = flipped_image

    def activate_magnet(self):
        """Active le magnétisme."""
        self.is_magnet_active = True
        music('./music/power_up.wav', 0.3)
        self.magnet_timer = pygame.time.get_ticks()  # Début du timer

    def deactivate_magnet(self):
        """Désactive le magnétisme."""
        self.is_magnet_active = False

    def update(self):
        """
        Met à jour les mouvements et animations du joueur en fonction de ses actions et de son état.
        """
        self.entree_joueur()
        self.etat_joueur()
        if self.is_magnet_active:
            if pygame.time.get_ticks() - self.magnet_timer > self.magnet_duration:
                self.deactivate_magnet()  # Désactivation automatique du magnétisme après la durée
        self.animate()





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
        """
        Initialise un ennemi qui se déplace à une vitesse constante.
        
        Args:
        - x (int): Position initiale en x.
        - y (int): Position initiale en y.
        - width (int): Largeur du rectangle.
        - height (int): Hauteur du rectangle.
        """

        super().__init__()
        self.import_character_assets()
        self.image = pygame.Surface((width*0.80, height*0.80))
        self.image.fill("grey")
        self.x = x
        self.y = y
        self.rect = self.image.get_rect(topleft=(self.x, self.y))
        self.width = width
        self.height = height
        self.vel = parametres.vitesse_joueur
        self.animation_speed = 0.25
        self.frame_index=0
        self.status="fer3awn"

        # Speed of the bull
    
    
    def entree_(self,level):
        """
        Gère les mouvements de l'ennemi en fonction des conditions du niveau.
        
        Args:
        - level: Instance du niveau actuel pour vérifier les collisions.
        """
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.vel = parametres.vitesse_joueur + 2
            
        elif keys[pygame.K_RIGHT]:
            if self.rect.x > -50  and not (level.isincollisionh):
                self.vel = -2
            elif level.isincollisionh:
                self.vel = parametres.vitesse_joueur
            else:
                self.vel = 0
        else:
            self.vel = parametres.vitesse_joueur
            
    def import_character_assets(self):
        """
        Importe les images pour les différentes animations du personnage.
        """
        character_path = "./graphics/bull_animation"
        self.animations = {"fer3awn": []}
        scale =5
        for animation in self.animations.keys():
            full_path = f"{character_path}/{animation}/"
            animation_images = import_images(full_path)
            scaled_images = [
                pygame.transform.scale(
                    image, (150*0.80, 450*0.80)
                )
                for image in animation_images
            ]
            self.animations[animation] = scaled_images
    def animate(self):
        """
        Anime l'ennemi .
        """
        animation = self.animations[self.status]

        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0

        image = animation[int(self.frame_index)]
        self.image=image


    def update(self,level):
        """
        Met à jour le déplacement et l'animation du taureau.
        
        Args:
        - level: Instance du niveau actuel pour gérer les collisions.
        """

        self.entree_(level)
        self.animate()
        self.rect.x +=self.vel
            # Gestion de l'image selon la direction
    #if self.vel > 0:
     #   self.image = pygame.transform.flip(self.image, True, False)  # Image pour la droite
    #elif self.vel < 0:
     #   self.image = pygame.transform.flip(self.image, False, False)  # Image pour la gauche

        
