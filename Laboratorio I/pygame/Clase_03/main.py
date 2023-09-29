import pygame, sys
from pygame.locals import *

pygame.init() # Para inicializar pygame

COLORS = {
    "white": (255, 255, 255),
    "black": (0, 0, 0),
    "red": (255, 0, 0),
    "green": (0, 255, 0),
    "blue": (0, 0, 255)
}

WINDOW = pygame.display.set_mode((500, 400)) # values are pixels

# window title
pygame.display.set_caption("First game")

WINDOW.fill(COLORS["white"])

while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      sys.exit()
  pygame.display.update() # constantly updating the window

pygame.quit()