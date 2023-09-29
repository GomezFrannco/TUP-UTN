import pygame, sys
from pygame.locals import *

pygame.init()

WHITE = (255,255,255)

WINDOW = pygame.display.set_mode((1000,500))
pygame.display.set_caption("Ejercicio diccionario")

TITLE_FONT = pygame.font.SysFont("Arial", 50)
PARAGRAPH_FONT = pygame.font.SysFont("Arial", 25)
title = TITLE_FONT.render("Ejercicio Diccionario", False, WHITE, None)

putin_image = pygame.transform.scale(pygame.image.load("putin.jpg"), (100, 100))
mbappe_image = pygame.transform.scale(pygame.image.load("mbappe.jpg"), (100, 100))
snoop_image = pygame.transform.scale(pygame.image.load("snoop.jpg"), (100, 100))

first_pet = {
  "name": "Putin",
  "age": "70",
  "image": putin_image
}
second_pet = {
  "name": "Mbappe",
  "age": "24",
  "image": mbappe_image
}
third_pet = {
  "name": "Snoop",
  "age": "51",
  "image": snoop_image
}

pet_list = [first_pet, second_pet, third_pet]

x = 50
y = 120

while True:
  event_list = pygame.event.get()
  for event in event_list:
    if event.type == pygame.QUIT:
      sys.exit()

  WINDOW.blit(title,(50,50))

  for pet in pet_list:
    name = PARAGRAPH_FONT.render(pet["name"], False, WHITE, None)
    age = PARAGRAPH_FONT.render(pet["age"], False, WHITE, None)
    WINDOW.blit(name,(x , y + 30))
    WINDOW.blit(age,(x + 100, y + 30))
    WINDOW.blit(pet["image"],(x + 200, y))
    y += 120

    if y > 500 - 120:
      y = 120

  pygame.display.update()

pygame.quit()