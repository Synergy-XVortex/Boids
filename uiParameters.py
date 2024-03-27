from ui import *

panel = Panel()
panel.color = (0, 0, 0)
resetButton = Button("Reset")

Behaviours = TextUI("COMPORTEMENTS", (Width - 180, 120), (255, 255, 255))
UItoggle = TextUI("les paramètres", (Width - 180, 125), (255, 255, 255))
UItoggle1 = TextUI("Appuyez sur 'U' pour voir", (Width - 180, 100),
                   (255, 255, 255))

Separation = TextUI("Séparation: ", (Width - 245, 180), (255, 255, 255))
Alignement = TextUI("Alignement: ", (Width - 245, 220), (255, 255, 255))
Cohesion = TextUI("Cohesion: ", (Width - 245, 260), (255, 255, 255))

SeparationValue = TextUI("valeur de séparation: ", (Width - 245, 315),
                         (255, 255, 255))
AlignementValue = TextUI("valeur alignement: ", (Width - 245, 365),
                         (255, 255, 255))
CohesionValue = TextUI("cohesion Value: ", (Width - 245, 415), (255, 255, 255))
NumberOfBoids = TextUI("Nombres: ", (Width - 245, 465), (255, 255, 255))
ScaleText = TextUI("Boid-raduis (rayon): ", (Width - 200, 520),
                   (255, 255, 255))

toggleSeparation = ToggleButton((Width - 160, 170), 20, 20, True)
toggleAlignement = ToggleButton((Width - 160, 210), 20, 20, True)
toggleCohesion = ToggleButton((Width - 160, 250), 20, 20, True)
# preset valeur
separationInput = DigitInput(10, (Width - 160, 300), 80, 30)
alignementInput = DigitInput(10, (Width - 160, 350), 80, 30)
cohesionInput = DigitInput(10, (Width - 160, 400), 80, 30)
numberInput = DigitInput(25, (Width - 160, 450), 80, 30)  # Nombre de boids

sliderScale = Slider(Width - 280, 550, 40, 0, 100, 180, 10, 80)
