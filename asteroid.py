import pygame
import circleshape

class Asteroid(circleshape.CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.radius = radius
        self.velocity = pygame.Vector2(0, 0)
    
    def draw(self, screen_obj):
        pygame.draw.circle(screen_obj, "white", (int(self.position.x), int(self.position.y)), int(self.radius), 2)
    
    def update(self, dt):
        self.position += self.velocity*dt