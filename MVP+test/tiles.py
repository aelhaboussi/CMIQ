import pygame


class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        """
        Initialise un objet Tile.

        Args:
        - pos (tuple): Position (x, y) de l'objet Tile.
        - size (int): Taille de l'objet Tile.

        Attributes:
        - image (pygame.Surface): Surface représentant l'image de la tile.
        - rect (pygame.Rect): Rectangle de collision pour la tile.

        Cette classe représente une tuile dans un jeu. Elle crée une surface
        rectangulaire remplie de couleur verte pour simuler une tuile c'est la base de notre map.
        """
        super().__init__()
        self.image = pygame.Surface((size, size))
        self.image.fill("green")
        self.rect = self.image.get_rect(topleft=pos)

    def update(self, deplacement):
        """
        Met à jour la position horizontale de la tuile en fonction du déplacment du joueur.
        """
        self.rect.x += deplacement