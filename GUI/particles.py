import pygame
from import_images import import_images
jump_folder_path = "./graphics/runner_animation/dust_particles/jump"
land_folder_path = "./graphics/runner_animation/dust_particles/land"
run_folder_path = "./graphics/runner_animation/dust_particles/run"
explosion_folder_path="./graphics/runner_animation/dust_particles/explosion"


class ParticleEffect(pygame.sprite.Sprite):
    def __init__(self, pos, type):
        """
        Initialise un effet de particule à une position donnée selon le type spécifié.

        Args:
        - pos (tuple): Position initiale de l'effet de particule.
        - type (str): Type de l'effet de particule ('jump', 'land' ou 'explosion').

        Attributes:
        - frame_index (int): Index de l'image de l'effet de particule dans la séquence d'animation.
        - animation_speed (float): Vitesse d'animation de l'effet de particule.
        - frames (list): Liste des images de l'effet de particule.
        - image (Surface): Image actuelle de l'effet de particule.
        - rect (Rect): Rectangle englobant de l'effet de particule.
        """
        super().__init__()
        self.frame_index = 0
        self.animation_speed = 0.5
        if type == "jump":
            animation_images = import_images(jump_folder_path)
            scale = 1.5
            scaled_images = [
                pygame.transform.scale(
                    image, (image.get_width() * scale, image.get_height() * scale)
                )
                for image in animation_images
            ]
            self.frames = scaled_images
        if type == "run":
            animation_images = import_images(run_folder_path)
            scale = 1.5
            scaled_images = [
                pygame.transform.scale(
                    image, (image.get_width() * scale, image.get_height() * scale)
                )
                for image in animation_images
            ]
            self.frames = scaled_images
        if type == "explosion":
            animation_images = import_images(explosion_folder_path)
            scale = 1.0
            scaled_images = [
                pygame.transform.scale(
                    image, (image.get_width() * scale, image.get_height() * scale)
                )
                for image in animation_images
            ]
            self.frames = scaled_images

        if type == "land":
            animation_images = import_images(land_folder_path)
            scale = 0.5
            scaled_images = [
                pygame.transform.scale(
                    image, (image.get_width() * scale, image.get_height() * scale)
                )
                for image in animation_images
            ]
            self.frames = scaled_images
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect(center=pos)

    def animate(self):
        """
        Anime l'effet de particule en changeant l'image affichée.
        """
        self.frame_index += self.animation_speed
        if self.frame_index >= len(self.frames):
            self.kill()
        else:
            self.image = self.frames[int(self.frame_index)]

    def update(self, x_shift):
        """
        Met à jour la position de l'effet de particule et anime l'effet.

        Args:
        - x_shift (int): Décalage horizontal de l'effet de particule.
        """
        self.animate()
        self.rect.x += x_shift