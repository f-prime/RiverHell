import pygame

from src.GameObject import GameObject


class Player(GameObject):
    id = "PLAYER"

    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 25, 25)
        self.position_vector = pygame.Vector2(x, y)
        self.speed = 250

    def move(self, vector):
        self.position_vector += vector

    def update(self, game):
        """
        Why do we multiply the velocity by game.dt?
        Because of d = vt. Distance is velocity * time. Our time in this case
        is the time since the last frame. So we are calculating how far the object
        on the screen should move from one frame to the next if it is traveling at
        250 (self.speed) pixels per second. 
        """

        distance = self.speed * game.dt

        pygame.draw.rect(game.screen, (0, 255, 0), self.rect)

        pressed_key = game.get_pressed_key()

        if pressed_key[pygame.K_RIGHT]:
            self.move(pygame.Vector2(distance, 0))
        elif pressed_key[pygame.K_LEFT]:
            self.move(pygame.Vector2(-distance, 0))

        if pressed_key[pygame.K_DOWN]:
            self.move(pygame.Vector2(0, distance))
        elif pressed_key[pygame.K_UP]:
            self.move(pygame.Vector2(0, -distance))

        self.rect.x = self.position_vector.x
        self.rect.y = self.position_vector.y

        self.velocity_vector = pygame.Vector2(0, 0)
