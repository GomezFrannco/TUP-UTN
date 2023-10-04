def bubble_sort(arr):
  """
  Ordena una lista utilizando el algoritmo Bubble Sort.

  :param arr: La lista que se desea ordenar.
  :return: La lista ordenada.
  """
  n = len(arr)
  for i in range(n):
    for j in range(0, n-i-1):
      if arr[j] > arr[j+1]:
        # Intercambiar elementos si están en el orden incorrecto
        arr[j], arr[j+1] = arr[j+1], arr[j]
# Ejemplo de uso
lista = [64, 34, 25, 12, 22, 11, 90]
# bubble_sort(lista)

# print("Lista ordenada:")
# print(lista)

sum = 0
for n in range(50):
  sum += 3*n
  print(sum)

# print(sum)