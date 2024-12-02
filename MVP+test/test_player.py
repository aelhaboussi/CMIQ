import pygame
import pytest
from player import Player
from settings import GRAVITY, jump_speed


@pytest.fixture
def player_instance():
    """
    Fixture pour créer une instance de Player pour les tests.
    """
    player = Player(0, 0)
    return player


def test_player_jump(player_instance):
    """
    Teste la fonction jump de la classe Player.
    Vérifie si la vitesse verticale du joueur est correctement mise à jour lors du saut.
    """
    player_instance.jump()
    assert player_instance.direction.y == jump_speed


def test_player_apply_gravity(player_instance):
    """
    Teste la fonction apply_gravity de la classe Player.
    Vérifie si la gravité est correctement appliquée au joueur.
    """
    player_instance.apply_gravity()
    assert player_instance.direction.y == GRAVITY


def test_player_entree_joueur(player_instance, mocker):
    """
    Teste la fonction entree_joueur de la classe Player.
    Vérifie si les directions sont correctement mises à jour selon les touches pressées.
    """
    mocker.patch(
        "pygame.key.get_pressed",
        return_value={
            pygame.K_LEFT: True,
            pygame.K_RIGHT: False,
            pygame.K_SPACE: False,
        },
    )
    player_instance.entree_joueur()
    assert player_instance.direction.x == -1