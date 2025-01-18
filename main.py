import pygame

from constants import *

def main():
  pygame.init()
  print("Starting asteroids!")
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  clock = pygame.time.Clock()
  dt = 0
  while True:
    for event in pygame.event.get():
       if event.type == pygame.QUIT:
          return
    screen.fill("black")
    tick = clock.tick(60)
    dt = tick / 1000
    pygame.display.flip()

if __name__ == "__main__":
    main()