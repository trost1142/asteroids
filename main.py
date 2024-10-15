from constants import *
import pygame
import player

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
  player.Player.containers = (updatable, drawable)
  player1 = player.Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)


  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
          return
    screen.fill(000)
    for updatable_player in updatable:
      updatable_player.update(dt)
    for drawable_player in drawable:
      drawable_player.draw(screen)
    pygame.display.flip()
    new_time = clock.tick(60)
    dt = new_time / 1000

if __name__ == "__main__":
  main()
