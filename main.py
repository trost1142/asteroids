from time import sleep
from constants import *
import pygame
import player
import asteroid
import asteroidfield
import shot

def main():
  print("Starting asteroids!")
  print("Screen width:", SCREEN_WIDTH)
  print("Screen height:", SCREEN_HEIGHT)
  pygame.init()
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  clock = pygame.time.Clock()
  dt = 0
  updatable = pygame.sprite.Group()
  drawable = pygame.sprite.Group()
  asteroids = pygame.sprite.Group()
  shots = pygame.sprite.Group()
  shot.Shot.containers = (shots, updatable, drawable)
  asteroid.Asteroid.containers = (asteroids, updatable, drawable)
  asteroidfield.AsteroidField.containers = (updatable)
  player.Player.containers = (updatable, drawable)
  player1 = player.Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
  asteroidField1 = asteroidfield.AsteroidField()


  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
          return
    screen.fill(000)
    for updatable_player in updatable:
      updatable_player.update(dt)
    for asteroid_obj in asteroids:
      if asteroid_obj.does_collide(player1):
        print("Game Over!")
        exit()
    for asteroid_obj in asteroids:
      for bullet in shots:
        if asteroid_obj.does_collide(bullet):
          asteroid_obj.split()
          bullet.kill()
    for drawable_player in drawable:
      drawable_player.draw(screen)
    pygame.display.flip()
    new_time = clock.tick(60)
    dt = new_time / 1000

if __name__ == "__main__":
  main()
