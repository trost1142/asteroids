from constants import *
import pygame
import circleshape


class Shot(circleshape.CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)
        self.rotation = 0
        self.velocity = pygame.Vector2(0, 0)
    
    def draw(self, screen_obj):
        pygame.draw.circle(screen_obj, "white", (int(self.position.x), int(self.position.y)), int(self.radius), 2)
    
    def update(self, dt):
        self.position += self.velocity*dt