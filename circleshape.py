import pygame

class CircleShape(pygame.sprite.Sprite):
  def __init__(self, x, y, radius):
    if hasattr(self, "containers"):
      super().__init__(self.containers)
    else:
      super().__init__()

    self.position = pygame.Vector2(x, y)  
    self.velocity = pygame.Vector2(0, 0)  
    self.radius = radius
  
  def draw(self, screen):
    pass

  def update(self, dt):
    pass

  def is_colliding(self, target):
    r1 = self.radius
    r2 = target.radius
    additive_radius = r1 + r2
    distance = self.position.distance_to(target.position)

    if additive_radius > distance:
      return True

    return False