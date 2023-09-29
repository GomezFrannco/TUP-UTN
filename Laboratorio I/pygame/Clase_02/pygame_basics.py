import pygame, sys
from pygame.locals import *

ROJO = (255,0,0)

# al módulo hay que inicializarlo y pararlo
pygame.init() # inicializador

WINDOW = pygame.display.set_mode((1000,500)) # medida de ventana (w, h)
pygame.display.set_caption("Game Window") # titulo
icon = pygame.image.load("heph-logo.png")
pygame.display.set_icon(icon)
WINDOW.fill(ROJO)

while True:
  event_list = pygame.event.get()
  for event in event_list:
    if event.type == pygame.QUIT:
      sys.exit()
  pygame.display.update() # Actualiza constantemente la ventana

pygame.quit()