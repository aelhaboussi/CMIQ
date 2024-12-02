import pygame
from os import walk

def import_images(path):
    """
    Importe et charge toutes les images d'un répertoire spécifié.

    Args:
    path (str): Chemin du répertoire contenant les images.

    Returns:
    list: Liste des surfaces chargées à partir des images.

    Exemple:
    Si vous avez un répertoire contenant des images à charger et que vous appelez la fonction
    `import_images('chemin/vers/le/repertoire')`, elle retournera une liste contenant toutes
    les surfaces des images dans le répertoire spécifié.
    """
    surface_list = []
    for __, _, img_files in walk(path):
        for image in img_files:
            full_path = path + "/" + image
            image_surf = pygame.image.load(full_path).convert_alpha()
            surface_list.append(image_surf)
    return surface_list

