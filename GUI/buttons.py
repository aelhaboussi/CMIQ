import pygame
from settings import parametres

class button:
    
    def __init__(self, normal_image_path, hovered_image_path):
        """
        Initialise un objet BOUTTON.

        Args:
            normal_image_path (str): chemin vers l'image du boutton normale.
            hovered_image_path (str): Chemin vers l'image du boutton activé.
            
        Attributes:
            normal_image (pygame.Surface): Surface graphique du boutton normale.
            hovered_image (pygame.Surface): Surface graphique du boutton activé.
            rect (pygame.Rect): Rectangle pour la gestion des collisions.
            is_hovered (bool): Indique si la souris est sur le boutton.
        """
        self.normal_image = pygame.image.load(normal_image_path).convert_alpha()
        self.hovered_image = pygame.image.load(hovered_image_path).convert_alpha()
        self.is_hovered = False
        
    def rect(self,coords=(parametres.screen_width//2, parametres.screen_height//2)):
        """
        renvoie le rectangle associé à l'image du boutton.
        
        Args:
            coords (tuple): position (x,y) du rectangle.
        """
        return self.normal_image.get_rect(center = coords)
        
    def resize(self,width,height):
        """
        redimensionne les images du boutton.
        
        Args:
            width (float): taille horizontale.
            height (float): taille verticale.
        """
        self.normal_image = pygame.transform.scale(self.normal_image, (width, height))
        self.hovered_image = pygame.transform.scale(self.hovered_image, (width, height))
    
    def draw(self, screen, position = (0,0)):
        """
        affiche les images du boutton sur l'écran.
        
        Args:
            screen (pygame.Surface): surface d'affichage.
            position (tuple): position d'affichage de l'image, (0,0) par défaut.
        """
        if self.is_hovered:
            screen.blit(self.hovered_image, position)
        else:
            screen.blit(self.normal_image, position)