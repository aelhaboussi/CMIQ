from pygame.locals import *
from pygame import mixer


def music(path, volume):
    """
    Lit la musique spécifiée par le chemin fourni avec un volume défini.

    Args:
    path (str): Chemin du fichier audio à lire.
    volume (float): Niveau sonore de la lecture (compris entre 0.0 et 1.0).

    Returns:
    None
    """
    sound = mixer.Sound(path)
    sound.set_volume(volume)
    sound.play()
