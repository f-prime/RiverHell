from typing import *

import pygame
import time

from src.GameObject import GameObject

class Game(object):
    """
    This object is intended to get passed around
    to access global game state variables such as
    height, width, screen, dt, etc.
    """

    def __init__(
        self,
        screen: pygame.Surface,
        width: int = 800,
        height: int = 600,
    ):
        self.screen: pygame.Surface = screen
        self.height: int = height
        self.width: int = width
        self.dt: float = 0
        self.last_frame: float = time.time()
        self.game_objects: List[GameObject] = []

    def register_object(game_object: GameObject) -> None:
        self.game_objects.append(game_object)

    def destroy_object(game_object: GameObject) -> None:
        if game_object in self.game_objects:
            self.game_objects.remove(game_object)

    def clear(self) -> None:
        """
        Clears the game screen with white.
        """

        self.screen.fill((255, 255, 255))

    def tick(self) -> float:
        self.dt = time.time() - self.last_frame
        self.last_time = time.time()

        return self.dt

    def update(self) -> None:
        for game_object in self.game_objects:
            game_object.update()
