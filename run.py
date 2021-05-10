import sys
import pygame

from src.Game import Game

def main(width: float, height: float) -> None:
    screen: pygame.Surface = pygame.display.set_mode((width, height))

    game: Game = Game(screen, width, height) 

    while True:
        game.tick()

        game.clear()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        pygame.display.update()

if __name__ == "__main__":
    main(800, 600)
