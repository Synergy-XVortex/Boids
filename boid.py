import pygame
from tools import *
from random import uniform
import colorsys
from matrix import *
from math import pi, sin, cos


# La class boid avec les différents parmètres nécessaire
class Boid:

  def __init__(self, x, y):
    self.position = Vector(x, y)
    vec_x = uniform(-1, 1)
    vec_y = uniform(-1, 1)
    self.velocity = Vector(vec_x, vec_y)
    self.velocity.normalise()
    self.velocity = self.velocity * uniform(1.5, 4)
    self.acceleration = Vector()
    self.color = (255, 255, 255)
    self.temp = self.color
    self.secondaryColor = (70, 70, 70)
    self.max_speed = 5
    self.max_length = 1
    self.size = 2
    self.stroke = 5
    self.angle = 0
    self.hue = 0
    self.toggles = {"separation": True, "alignement": True, "cohesion": True}
    self.values = {"separation": 0.1, "alignement": 0.1, "cohesion": 0.1}
    self.radius = 40

# Définition des limites de la fenètre pour les boids

  def limits(self, width, height):
    if self.position.x > width:
      self.position.x = 0
    elif self.position.x < 0:
      self.position.x = width

    if self.position.y > height:
      self.position.y = 0
    elif self.position.y < 0:
      self.position.y = height

  def behaviour(self, flock):
    self.acceleration.reset()

    if self.toggles["separation"] == True:
      avoid = self.separation(flock)
      avoid = avoid * self.values["separation"]
      self.acceleration.add(avoid)

    if self.toggles["cohesion"] == True:
      coh = self.cohesion(flock)
      coh = coh * self.values["cohesion"]
      self.acceleration.add(coh)

    if self.toggles["alignement"] == True:
      align = self.alignement(flock)
      align = align * self.values["alignement"]
      self.acceleration.add(align)

# Fonction de séparation des boids

  def separation(self, flockMates):
    total = 0
    pilote = Vector()
    for mate in flockMates:
      dist = getDistance(self.position, mate.position)
      if mate is not self and dist < self.radius:
        temp = SubVectors(self.position, mate.position)
        temp = temp / (dist**2)
        pilote.add(temp)
        mate.color = hsv_to_rgb(self.hue, 1, 1)
        total += 1

    if total > 0:
      pilote = pilote / total
      pilote.normalise()
      pilote = pilote * self.max_speed
      pilote = pilote - self.velocity
      pilote.limit(self.max_length)
    return pilote

# Foncton d'alignement des boids

  def alignement(self, flockMates):
    total = 0
    pilote = Vector()
    for mate in flockMates:
      dist = getDistance(self.position, mate.position)
      if mate is not self and dist < self.radius:
        vel = mate.velocity.Normalise()
        pilote.add(vel)
        mate.color = hsv_to_rgb(self.hue, 1, 1)
        total += 1

    if total > 0:
      pilote = pilote / total
      pilote.normalise()
      pilote = pilote * self.max_speed
      pilote = pilote - self.velocity.Normalise()
      pilote.limit(self.max_length)
    return pilote

  # Fonction de cohesion des boids
  def cohesion(self, flockMates):
    total = 0
    pilote = Vector()
    for mate in flockMates:
      dist = getDistance(self.position, mate.position)
      if mate is not self and dist < self.radius:
        pilote.add(mate.position)
        mate.color = hsv_to_rgb(self.hue, 1, 1)
        total += 1

    if total > 0:
      pilote = pilote / total
      pilote = pilote - self.position
      pilote.normalise()
      pilote = pilote * self.max_speed
      pilote = pilote - self.velocity
      pilote.limit(self.max_length)
    return pilote

# Fonction d'actualisation des boids

  def update(self):
    self.position = self.position + self.velocity
    self.velocity = self.velocity + self.acceleration
    self.velocity.limit(self.max_speed)
    self.angle = self.velocity.heading() + pi / 2


# Dessine le boid, sa forme

  def Draw(self, screen, distance, scale):
    ps = []
    points = [None for _ in range(3)]
    points[0] = [[0], [-self.size], [0]]
    points[1] = [[self.size // 2], [self.size // 2], [0]]
    points[2] = [[-self.size // 2], [self.size // 2], [0]]

    for point in points:
      rotated = matrix_multiplication(rotationZ(self.angle), point)
      z = 1 / (distance - rotated[2][0])

      projection_matrix = [[z, 0, 0], [0, z, 0]]
      projected_2d = matrix_multiplication(projection_matrix, rotated)

      x = int(projected_2d[0][0] * scale) + self.position.x
      y = int(projected_2d[1][0] * scale) + self.position.y
      ps.append((x, y))

    pygame.draw.polygon(screen, self.secondaryColor, ps)
    pygame.draw.polygon(screen, self.color, ps, self.stroke)
