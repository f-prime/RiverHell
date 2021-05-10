import pygame

from src.GameObject import GameObject


class River(GameObject):
    """
    The main purpose of this object is to add a small vector to the
    player object in the y dirgit@github.com:f-prime/RiverHell.gitection. 
    """

    id = "RIVER"

    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 25, 25)
        self.river_speed = 30

    def update(self, game):
        player = game.get_player()

        if player and self.rect.colliderect(player.rect):
            player.move(pygame.Vector2(0, self.river_speed * game.dt))

        pygame.draw.rect(game.screen, (80, 80, 255), self.rect)
