import math

# 1
def circle_area(radius: int or float) -> int or float or str:
  result = None

  if isinstance(radius, int or float) != True:
    result = "Ingrese un número"
  else:
    pi_number = math.pi
    square_radius = radius ** 2
    result = pi_number * square_radius

  return result

# print(circle_area(6))

# 2
def even_or_odd(number: int or float) -> str:
  number_is = None

  if isinstance(number, int or float) != True:
    number_is = "No es un número"
  else:
    if number % 2 == 0:
      number_is = f"El número {number} es par"
    else:
      number_is = f"El número {number} es impar"
  
  return number_is

# print(even_or_odd(287122))

# 3
def sum_all_elements(number_list: list) -> int or float:
  total = None

  if isinstance(number_list, list) and len(number_list) > 0:
    total = 0
    
    for number in number_list:
      if isinstance(number, int):
        total += number
      else:
        total = "La lista solo debe contener números"
        break
  else:
    total = "Ingrese una lista no vacía"
  
  return total

# print(sum_all_elements([1, 2, 3, 4]))

# 4
def max_number(a: int or float, b: int or float, c: int or float) -> int or float:
  found = None

  if isinstance(a, int or float) != True or isinstance(b, int or float) != True or isinstance(c, int or float) != True:
    found = "Todos deben ser números"
  else:
    if a > b and a > c:
      found = a
    elif b > a and b > c:
      found = b
    elif c > a and c > b:
      found = c
    else:
      found = "No hay un solo número que sea el mas grande"
  
  return found

# print(max_number(1,5, 15))

# 5
def invert_string(string: str) -> str:
  output = ""

  if isinstance(string, str):
    for l in range(len(string)):
      output = string[l] + output
  else:
    output = "Por Favor, ingrese un string"
  
  return output
  
# print(invert_string("PYTHON"))

# 7
def power_of_a_number(base: int or float, exponent: int or float) -> int or str:
  power_result = None

  if isinstance(base, int or float) and isinstance(exponent, int or float):
    power_result = base ** exponent
  else:
    power_result = "Ingrese números válidos"
  
  return power_result

# print(power_of_a_number(9,2))

# 8
def find_even_numbers(number_list: list) -> list or str:
  even_list = None

  if isinstance(number_list, list) and len(number_list) > 0:
    even_list = []

    for number in number_list:
      # valida que cada elemento sea de tipo entero
      if isinstance(number, int):
        if number % 2 == 0:
          even_list.append(number)
      else:
        even_list = "La lista solo debe contener números"
        break
  else:
    even_list = "Ingrese una lista no vacía"
  
  return even_list

# print(find_even_numbers([18,1,231,657,86]))

# 9
def product_of_all(number_list: list) -> int or float or str:
  result = None

  if isinstance(number_list, list) or len(number_list) > 0:
    # asigno el primer elemento de la lista al resultado
    result = number_list[0]
    # comienzo el bucle desde la posición 1
    for i in range(1, len(number_list)):
      # valida que cada número sea de tipo entero
      if isinstance(number_list[i], int):
        result = number_list[i] * result
      else:
        result = "La lista solo debe contener números"
        break
  else:
    result = "Ingrese una lista no vacía"
  
  return result

# print(product_of_all([5,9,3,4,7,8,5]))

# 10
def is_palindrome(word: str) -> bool or str:
  result = None

  if isinstance(word, str) and len(word) > 0:
    for i in range(len(word)):
       # Comparación simetrica de posiciones
      if word[i] == word[len(word)-1-i]: # -> "HELLO" -> "H" == "O", "E" == "L", etc...
        result = True
      else: 
        result = False
  else:
    result = "Ingrese una palabra"

  return result

# print(is_palindrome("neuquen"))