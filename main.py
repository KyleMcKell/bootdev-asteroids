import pygame

from constants import *
from player import Player

def main():
  pygame.init()
  print("Starting asteroids!")

  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  clock = pygame.time.Clock()
  dt = 0

  x = SCREEN_WIDTH / 2
  y = SCREEN_HEIGHT / 2
  player = Player(x, y)

  while True:
    tick = clock.tick(60)
    dt = tick / 1000

    for event in pygame.event.get():
       if event.type == pygame.QUIT:
          return

    screen.fill("black")
    player.draw(screen)
    pygame.display.flip()

if __name__ == "__main__":
    main()