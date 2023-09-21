from data import lista_bzrp

# video/s con mas vistas
max_views = 0

for v in lista_bzrp:
  vistas = v["views"]
  if vistas > max_views:
    max_views = vistas

for v in lista_bzrp:
  vistas = v["views"]
  titulos = v["title"]
  if vistas == max_views:
    print(f"Titulo:{titulos} - Video:{vistas}")

# promedio de la duracion de los videos
acumulador = 0

for v in lista_bzrp:
  duracion = v["length"]
  acumulador += duracion

promedio = acumulador / len(lista_bzrp)

print(f"Duracion promedio: {promedio:0.2f}s")

# videos que superan el promedio

for v in lista_bzrp:
  duracion = v["length"]
  titulos = v["title"]
  if duracion > promedio:
    print(f"Titulo:{titulos} - Duracion:{duracion}s")