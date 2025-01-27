import pygame
from constants import *

class CircleShape(pygame.sprite.Sprite):
    def __init__(self, radius, x, y):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass

    def check_collision(self, other_shape):
        distance = self.position.distance_to(other_shape.position)
        if distance <= self.radius + other_shape.radius:
            return True
        return False

class Shot(CircleShape):
    def __init__(self, x, y, velocity):
        super().__init__(SHOT_RADIUS, x, y)
        self.velocity = velocity

    def update(self, dt):
      self.position += self.velocity * dt

    def draw(self, screen):
        pygame.draw.circle(screen, "white", (self.position.x, self.position.y), SHOT_RADIUS)