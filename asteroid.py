import pygame
import random
from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += dt * self.velocity

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20, 50)
        velocity_one = self.velocity.rotate(angle)
        velocity_two = self.velocity.rotate(-angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        first = Asteroid(self.position.x, self.position.y, new_radius)
        speed_up = 1.2
        first.velocity = velocity_one * speed_up
        second = Asteroid(self.position.x, self.position.y, new_radius)
        second.velocity = velocity_two * speed_up
