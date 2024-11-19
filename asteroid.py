import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(
            surface=screen,
            color="white",
            center=self.position,
            radius=self.radius,
            width=2
        )
    
    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        degree = random.randint(20, 50)
        asteroid_one_velocity, asteroid_two_velocity = self.velocity.rotate(degree), self.velocity.rotate(-degree)
        radius = self.radius - ASTEROID_MIN_RADIUS

        asteroid_one = Asteroid(self.position.x, self.position.y, radius)
        asteroid_one.velocity = asteroid_one_velocity * 1.2
        asteroid_two = Asteroid(self.position.x, self.position.y, radius)
        asteroid_two.velocity = asteroid_two_velocity * 1.2