import pygame
from tiles import *
from settings import *
import os
from player import *

class Level:
    def __init__(self, map, screen):
        """
        Initialise un niveau avec une carte et un écran.

        Arguments :
        - map (list) : Une liste représentant la carte du niveau.
        - screen (pygame.Surface) : La surface d'affichage du jeu.

        Attributs :
        - window (pygame.Surface) : La surface d'affichage du jeu.
        - tiles (pygame.sprite.Group) : Groupe de sprites représentant les tuiles du niveau.
        - player (pygame.sprite.GroupSingle) : Groupe de sprite représentant le joueur.
        - bull (pygame.sprite.GroupSingle) : Groupe de sprite représentant le taureau.
        - deplacement (int) : Valeur de déplacement horizontale du niveau.
        - isincollisionh (bool) : Indicateur si le joueur est en collision horizentale.
        - deplacement (float) : 
        """
        self.window = screen
        self.loading_level(map)
        self.deplacement = 0
        self.isincollisionh = False
        self.bgx = 0  # Position horizontale du background
        self.isgameover =False




    def loading_level(self, map):
        """
        Charge le niveau en fonction de la carte donnée.
        Arguments :
        - map (list) : Une liste de strings représentant la carte.
        """
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        self.bull = pygame.sprite.GroupSingle()
        a= Bull(0,400,40,40)
        self.bull.add(a)
        n = len(map)
        m = len(map[0])
        for i in range(n):
            for j in range(m):
                if map[i][j] == "X":                             #X represente une tuile
                    pos = (j * tile_size, 250+i * tile_size)
                    tile = Tile(pos, tile_size)
                    self.tiles.add(tile)
                if map[i][j] == "P":                            #P represente le joueur
                    p = Player(j * tile_size,250+ i * tile_size)
                    self.player.add(p)

    def bordure_x(self):
        """
        Assure la gestion des limites horizontales du niveau pour le déplacement du joueur.
        """
        p = self.player.sprite
        if p.rect.centerx < screen_width / 2 and p.direction.x < 0:
            self.deplacement = vitesse_joueur
            p.v = 0
        elif p.rect.centerx >  screen_width / 2 and p.direction.x > 0:
            self.deplacement = -vitesse_joueur
            p.v = 0
        else:
            self.deplacement = 0
            p.v = vitesse_joueur

    def collision_hori(self):
        """
        Gère les collisions horizontales du joueur avec les tuiles du niveau et indique 
        s'il ya une collision horizentale dans l'attribu iscollisionh.
        """
        p = self.player.sprite
        p.rect.x += p.direction.x * p.v
        i=0
        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(p.rect):
                if p.direction.x < 0:
                    p.rect.left = sprite.rect.right
                    i+=1
                    self.isincollisionh=True
                elif p.direction.x > 0:
                    p.rect.right = sprite.rect.left
                    i+= 1
                    self.isincollisionh=True
        if i == 0:
            self.isincollisionh=False
            
            

    def collision_ver(self):
        """
        Gère les collisions verticales du joueur avec les tuiles.
        """
        p = self.player.sprite
        p.apply_gravity()
        frappe = [
            sprite for sprite in self.tiles.sprites() if sprite.rect.colliderect(p.rect)
        ]
        if p.direction.y > 0:
            for i in frappe[::-1]:
                p.rect.bottom = i.rect.top
                p.direction.y = 0
                p.terre = True
                break
        elif p.direction.y < 0:
            for i in frappe:
                p.rect.top = i.rect.bottom
                p.direction.y = 0
                p.terre = False
                break
        if len(frappe) == 0:
            p.terre = False
            if p.direction.y > p.gravity:
                p.status = "fall"
    
    
    def update_bgx(self,deplacement):
        '''
        Assure le défilment du background
        '''
        self.bgx += deplacement
        
    def collision_torro(self):
        """
        Gére la collision avec le taureau
        """
        p = self.player.sprite
        p.rect.x += p.direction.x * p.v
        for sprite in self.bull.sprites():
            if sprite.rect.colliderect(p.rect):
                if p.rect.left <= sprite.rect.right:
                    self.isgameover = True
                    
                 
    def draw_level(self,bg):
        """
        C'est la fonction qui fait tout.
        Dessine le niveau en mettant à jour les éléments et en gérant les collisions.
        """
        self.player.update()
        self.update_bgx(self.deplacement)
        self.collision_torro()
        self.window.blit(bg,(self.bgx,0))
        self.bull.update(self)
        self.bull.draw(self.window)
        self.tiles.draw(self.window)
        self.bordure_x()
        self.tiles.update(self.deplacement)
        self.collision_ver()
        self.collision_hori()
        self.player.draw(self.window)
