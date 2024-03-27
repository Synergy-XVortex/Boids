import pygame  # Print un truc vers la page de pygames
from boid import Boid
from tools import Vector
import math
import random
from constants import *
from uiParameters import *

# Initialisation de le fenètre pygame
pygame.init()
window = pygame.display.set_mode(size, pygame.FULLSCREEN)
clock = pygame.time.Clock()
fps = 60

taille = 40
Distance = 5
speed = 0.005

flock = []
# Nombre de boids
n = 25

# Taille des boids
for i in range(n):
  flock.append(
    Boid(random.randint(20, Width - 20), random.randint(20, Height - 20)))

textI = "10"
reset = False
SpaceButtonPressed = False
backSpace = False
keyPressed = False
showUI = True
clicked = False
run = True

while run:
  clock.tick(fps)
  window.fill((10, 10, 15))

  n = numberInput.value
  taille = sliderScale.value

  for event in pygame.event.get():

    if event.type == pygame.QUIT:
      run = False
    if event.type == pygame.MOUSEBUTTONUP:
      clicked = True
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_ESCAPE:
        run = False
      if event.key == pygame.K_r:
        reset = True
      if event.key == pygame.K_SPACE:
        SpaceButtonPressed = True

      textI = pygame.key.name(event.key)
      keyPressed = True

    if event.type == pygame.KEYUP:
      if event.key == pygame.K_BACKSPACE:
        backSpace = True
      if event.key == pygame.K_u:  # Paramètre de touche pour afficher ui
        showUI = not showUI

# Permet de reset la fenetre
  if reset == True or resetButton.state == True:
    flock = []
    for i in range(n):
      flock.append(
        Boid(random.randint(20, Width - 20), random.randint(20, Height - 20)))
    reset = False

# Fait apparaitre les boids
  for boid in flock:
    boid.toggles = {
      "separation": toggleSeparation.state,
      "alignement": toggleAlignement.state,
      "cohesion": toggleCohesion.state
    }
    boid.values = {
      "separation": separationInput.value / 100,
      "alignement": alignementInput.value / 100,
      "cohesion": cohesionInput.value / 100
    }
    boid.radius = taille
    boid.limits(Width, Height)
    boid.behaviour(flock)
    boid.update()
    boid.hue += speed
    boid.Draw(window, Distance, taille)

# Affiche l'interface utilisateur
  if showUI == True:
    panel.Render(window)
    resetButton.Render(window)
    Behaviours.Render(window)
    Separation.Render(window)
    Alignement.Render(window)
    Cohesion.Render(window)
    SeparationValue.Render(window)
    AlignementValue.Render(window)
    CohesionValue.Render(window)
    NumberOfBoids.Render(window)
    ScaleText.Render(window)
    toggleSeparation.Render(window, clicked)
    toggleAlignement.Render(window, clicked)
    toggleCohesion.Render(window, clicked)
    separationInput.Render(window, textI, backSpace, keyPressed)
    alignementInput.Render(window, textI, backSpace, keyPressed)
    cohesionInput.Render(window, textI, backSpace, keyPressed)
    numberInput.Render(window, textI, backSpace, keyPressed)
    sliderScale.Render(window)

# Ou affiche comment afficher l'interface utilisateur
  else:
    UItoggle.Render(window) or UItoggle1.Render(window)

  backSpace = False
  keyPressed = False
  pygame.display.flip()
  clicked = False
pygame.quit()
