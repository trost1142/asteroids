from constants import *
import pygame
import circleshape
import random

class Asteroid(circleshape.CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.radius = radius
        self.velocity = pygame.Vector2(0, 0)
    
    def draw(self, screen_obj):
        pygame.draw.circle(screen_obj, "white", (int(self.position.x), int(self.position.y)), int(self.radius), 2)
    
    def update(self, dt):
        self.position += self.velocity*dt

    def split(self):
        self.kill()
        if (self.radius <= ASTEROID_MIN_RADIUS):
            return
        
        random_angle = random.uniform(20, 50)
        positive_vector = self.velocity.rotate(random_angle)
        negative_vector = self.velocity.rotate(-random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        first_new_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        second_new_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        first_new_asteroid.velocity = positive_vector * 1.2
        second_new_asteroid.velocity = negative_vector * 1.2


