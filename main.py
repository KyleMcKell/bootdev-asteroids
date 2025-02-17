import pygame
import sys

from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
  pygame.init()
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  clock = pygame.time.Clock()
  dt = 0

  updatable = pygame.sprite.Group()
  drawable = pygame.sprite.Group()
  asteroids = pygame.sprite.Group()
  shots = pygame.sprite.Group()

  Player.containers = (updatable, drawable)
  Asteroid.containers = (updatable, drawable, asteroids)
  AsteroidField.containers = (updatable)
  Shot.containers = (shots, updatable, drawable)

  player_starting_x = SCREEN_WIDTH / 2
  player_starting_y = SCREEN_HEIGHT / 2
  player = Player(player_starting_x, player_starting_y)

  asteroid_field = AsteroidField()

  while True:
    for event in pygame.event.get():
       if event.type == pygame.QUIT:
          return

    screen.fill("black")

    for sprite in updatable:
      sprite.update(dt)

    for asteroid in asteroids:
      for shot in shots:
        if asteroid.is_colliding(shot):
          asteroid.split()
          shot.kill()

      if asteroid.is_colliding(player):
        sys.exit("Game over!")
      
      
    for sprite in drawable:
      sprite.draw(screen)

    tick = clock.tick(60)
    dt = tick / 1000

    pygame.display.flip()

if __name__ == "__main__":
    main()