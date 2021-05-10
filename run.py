import sys
import pygame

from src.Game import Game
from src.Player import Player
from src.River import River

import time


def main(width: float, height: float) -> None:
    pygame.display.set_caption("River Hell")

    screen = pygame.display.set_mode((width, height))

    game = Game(screen, width, height)

    # Puts a big ass river in the middle of the screen

    for x in range(int(width * 0.15), int(width * 0.85), 25):
        for y in range(0, height, 25):
            game.register_object(River(x, y))

    player = Player(50, 50)

    game.register_object(player)

    while True:
        game.tick()
        game.clear()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        game.update()
        pygame.display.update()


if __name__ == "__main__":
    main(800, 600)
