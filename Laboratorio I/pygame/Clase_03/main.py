import pygame, sys
from pygame.locals import *
import math

# pi number as a constant
PI_NUMBER = math.pi

# initializing pygame
pygame.init()

# window settings
window_width = 800
window_height = 600
WINDOW = pygame.display.set_mode((window_width, window_height)) # values in pixels (x, y)
pygame.display.set_caption("Funciones Pygame") # window title

# fonts to use
FONT = pygame.font.SysFont("Arial", 25)

# colors
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
YELLOW =  (255, 255, 0)

# data from different geometric figures
figure_list = [
  {
    "type": "circulo",
    "color": GREEN,
    "x_pos": 350,
    "y_pos": 250,
    "radius": 25
  },
  {
    "type": "cuadrado",
    "color": WHITE,
    "x_pos": 350,
    "y_pos": 250,
    "base": 100,
    "height": 100
  },
  {
    "type": "rectangulo",
    "color": RED,
    "x_pos": 300,
    "y_pos": 200,
    "base": 200,
    "height": 100
  },
  {
    "type": "triangulo",
    "color": YELLOW,
    "x_pos": 0,
    "y_pos": 0,
    "point_a": (400, 300),
    "point_b": (400, 250),
    "point_c": (450, 300),
  }
]

# circle functions
def calculate_circle_area(circle_data: dict):
  radius = circle_data["radius"]
  radius_squared = radius ** 2
  area = PI_NUMBER * radius_squared
  return area

def calculate_circle_perimeter(circle_data: dict):
  radius = circle_data["radius"]
  perimeter = 2 * PI_NUMBER * radius
  return perimeter

def draw_circle(surface: pygame.surface.Surface, data: dict):
  position = (data["x_pos"], data["y_pos"])
  radius = data["radius"]
  color = data["color"]
  pygame.draw.circle(surface, color, position, radius) # (pos x, pos y), radius

# quadrilateral functions
def calculate_quadrilateral_perimeter(quad_data: dict):
  base = quad_data["base"]
  height = quad_data["height"]
  perimeter = (2 * base) + (2 * height)
  return perimeter

def calculate_quadrilateral_area(quad_data: dict):
  base = quad_data["base"]
  height = quad_data["height"]  
  area = base * height
  return area

def draw_quadrilateral(surface: pygame.surface.Surface, quad_data: dict):
  x, y = quad_data["x_pos"], quad_data["y_pos"]
  base = quad_data["base"]
  height = quad_data["height"]
  color = quad_data["color"]
  pygame.draw.rect(surface, color, (x, y, base, height)) # (pos x, pos y, width, height)

# triangle functions
def calculate_module(a, b):
  distance = a - b
  if distance < 0:
    distance = distance * -1
  
  return distance

def calculate_triangle_area(triangle_data: dict):
  x1, y1 = triangle_data["point_a"]
  x2, y2 = triangle_data["point_b"]
  x3, y3 = triangle_data["point_c"]

  base = calculate_module(x2, x3)

  height = calculate_module(y1, y2)

  area = (base * height) / 2

  return area

def calculate_triangle_perimeter(triangle_data: dict):
  x1, y1 = triangle_data["point_a"]
  x2, y2 = triangle_data["point_b"]
  x3, y3 = triangle_data["point_c"]

  side_a = calculate_module(y1, y2) # height
  side_b = calculate_module(x2, x3) # base
  side_c = ((side_a ** 2) + (side_a ** 2)) ** 0.5 # hypotenuse

  perimeter = side_a + side_b + side_c

  return perimeter

def draw_triangle(surface, data):
  triangle_points = [data["point_a"], data["point_b"], data["point_c"]]
  pygame.draw.polygon(surface, data["color"], triangle_points)

# functions to print figures and their information
def find_a_figure(figure_list: list, figure_name: str):
  figure_dict =  None
  
  if len(figure_list) > 0: 
    for figure in figure_list:
      if figure["type"] == figure_name:
        figure_dict = figure
  else:
    figure_dict = False

  return figure_dict

def draw_a_figure(figure: dict):
  match figure["type"]:
    case "circulo":
      draw_circle(WINDOW, figure)
    case "cuadrado":
      draw_quadrilateral(WINDOW, figure)
    case "rectangulo":
      draw_quadrilateral(WINDOW, figure)
    case "triangulo":
      draw_triangle(WINDOW, figure)

# main function to manage the window and events
def main():
  clock = pygame.time.Clock()
  is_running = True

  while is_running:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        is_running = False

    # window background color
    WINDOW.fill(BLACK)

    # choose a geometric figure to print (a circle in this case)
    figure = "cuadrado"
    figure_data = find_a_figure(figure_list, figure)
    
    # drawing the geometric figure in the window
    draw_a_figure(figure_data) 

    # calculate geometric figure area and perimeter
    if figure == "circulo":
      area = calculate_circle_area(figure_data)
      perimeter = calculate_circle_perimeter(figure_data)
    elif figure == "cuadrado" or figure == "rectangulo":
      area = calculate_quadrilateral_area(figure_data)
      perimeter = calculate_quadrilateral_perimeter(figure_data)
    elif figure == "triangulo":
      area = calculate_triangle_area(figure_data)
      perimeter = calculate_triangle_perimeter(figure_data)

    # showing figure data
    perimeter_text = f"Perímetro: {perimeter:.2f}"
    rendering_perimeter = FONT.render(perimeter_text, False, WHITE, None)
    area_text = f"Area: {area:.2f}"
    rendering_area = FONT.render(area_text, False, WHITE, None)
    WINDOW.blit(rendering_perimeter, (300,400))
    WINDOW.blit(rendering_area, (300,450))

    pygame.display.flip()
    clock.tick(60)

  pygame.quit()
  sys.exit()

main()