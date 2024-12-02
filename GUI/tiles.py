import pygame

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, size, transparency=True, is_moving=False):
        """
        Initialise un objet Tile.

        Args:
            pos (tuple): Position (x, y) de la tuile.
            size (int): Taille de la tuile.
            transparency (bool): Détermine si la tuile est transparente. Par défaut True.
            is_moving (bool): Indique si la tuile est mobile. Par défaut False.

        Attributes:
            image (pygame.Surface): Surface graphique de la tuile.
            rect (pygame.Rect): Rectangle pour la gestion des collisions.
            x (int): Coordonnée x de la tuile.
            y (int): Coordonnée y de la tuile.
            direction (int): Direction du mouvement vertical de la tuile.
            move (bool): Indique si la tuile est mobile, False par défaut.
            direction (int): direction de deplacement de la tuile.
        """
        super().__init__()
        if transparency:
            self.image = pygame.Surface((size, size), pygame.SRCALPHA)
        else:
            self.image = pygame.Surface((size, size))
            self.image.fill("green")
        self.rect = self.image.get_rect(topleft=pos)
        self.x = pos[0]
        self.y = pos[1]
        self.direction = 2
        self.move = is_moving

    def update(self, deplacement):
        """
        Met à jour la position de la tuile.

        Args:
            deplacement (int): Déplacement horizontal/verticale de la tuile.
        """
        self.rect.x += deplacement
        
        if self.move:
            if self.rect.y in {400, 150}:
                self.direction *= -1
            self.rect.y += self.direction

class Obstacle(Tile):
    def __init__(self, pos, size, image_path, is_moving=False):
        """
        Initialise un objet Obstacle.

        Args:
            pos (tuple): Position (x, y) de l'obstacle.
            size (int): Taille de l'obstacle.
            image_path (str): Chemin vers l'image de l'obstacle.
            is_moving (bool): Indique si l'obstacle est mobile. Par défaut False.
        """
        super().__init__(pos, size)
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (size, size))
        self.move = is_moving

class Ground(Tile):
    def __init__(self, pos, size):
        """
        Initialise un objet Ground.

        Args:
            pos (tuple): Position (x, y) du sol.
            size (int): Taille du sol.
        """
        super().__init__(pos, size)
        self.image = pygame.Surface((size, size), pygame.SRCALPHA)

class Coin(Tile):
    """
    Classe représentant une pièce animée.

    Attributes:
        val (int): Valeur numérique de la pièce.
    """
    def __init__(self, pos, size, val, image_path):
        """
        Initialise un objet Coin.

        Args:
            pos (tuple): Position (x, y) de la pièce.
            size (int): Taille de la pièce.
            val (int): Valeur numérique de la pièce.
            image_path (str): Chemin vers l'image de la pièce.
        """
        super().__init__(pos, size)
        self.val = val
        center_x, center_y = self.rect.center
        if val == 0:
            self.image = pygame.image.load(image_path).convert_alpha()
            self.image = pygame.transform.scale(self.image, (40, 40))
        elif val == 1:
            self.image = pygame.image.load(image_path).convert_alpha()
            self.image = pygame.transform.scale(self.image, (40, 40))
        elif val == 2:  # Bouclier
            self.image = pygame.image.load(image_path).convert_alpha()
            self.image = pygame.transform.scale(self.image, (75, 75))
        elif val == 3:  # Aimant
            self.image = pygame.image.load(image_path).convert_alpha()
            self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect(center=(center_x, center_y))

class BUS(Obstacle):
    def __init__(self, pos, image_path, size=(500, 150)):
        """
        Initialise un objet BUS.

        Args:
            pos (tuple): Position (x, y) du bus.
            image_path (str): Chemin vers l'image du bus.
            size (tuple): Taille du bus (largeur, hauteur). Par défaut (500, 150).
        """
        tile_size = 50
        super().__init__(pos, tile_size, image_path)
        self.image = pygame.Surface(size)
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, size)
        self.rect = self.image.get_rect(topleft=pos)
        self.x = pos[0]
        self.y = pos[1]
