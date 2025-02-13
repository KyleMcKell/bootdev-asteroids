import pygame
import random

from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
  def __init__(self, x, y, radius):
    super().__init__(x, y, radius)

  def draw(self, screen):
    return pygame.draw.circle(screen, "white", self.position, self.radius, 2)

  def update(self, dt):
    self.position += self.velocity * dt
  
  def split(self):
    self.kill()
    if self.radius <= ASTEROID_MIN_RADIUS:
      return
    
    angle = random.uniform(20, 50) 
    new_velocity_pos = self.velocity.rotate(angle)
    new_velocity_neg = self.velocity.rotate(-angle)
    new_radius = self.radius - ASTEROID_MIN_RADIUS

    for velocity in [new_velocity_pos, new_velocity_neg]:
      asteroid = Asteroid(self.position.x, self.position.y, new_radius)
      asteroid.velocity = velocity * 1.2