import pygame
import random
from circleshape import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius, velocity = None):
        super().__init__(radius, x, y)
        self.radius = radius
        self.velocity = velocity if velocity else pygame.math.Vector2(0, 0)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        random_angle = random.uniform(20,50)
        new_velocity1 = self.velocity.rotate(random_angle)
        new_asteroid1 = Asteroid(self.position.x, self.position.y, new_radius, new_velocity1 * 1.2)

        new_velocity2 = self.velocity.rotate(-random_angle)
        new_asteroid2 = Asteroid(self.position.x, self.position.y, new_radius, new_velocity2 * 1.2)
