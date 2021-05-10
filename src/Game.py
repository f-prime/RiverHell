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
        self, screen, width=800, height=600,
    ):
        self.screen = screen
        self.height = height
        self.width = width
        self.dt = 0
        self.last_frame = time.time()
        self.game_objects = []

    def register_object(self, game_object):
        self.game_objects.append(game_object)

    def destroy_object(self, game_object):
        if game_object in self.game_objects:
            self.game_objects.remove(game_object)

    def get_player(self):
        for obj in self.game_objects:
            if obj.id == "PLAYER":
                return obj
        return None

    def clear(self):
        """
        Clears the game screen with white.
        """

        self.screen.fill((255, 255, 255))

    def get_pressed_key(self):
        return pygame.key.get_pressed()

    def tick(self):
        self.dt = time.time() - self.last_frame
        self.last_frame = time.time()

        return self.dt

    def update(self):
        for game_object in self.game_objects:
            game_object.update(self)
