from data import lista_bzrp

while True:
  respuesta = int(input("\n1.Tema mas visto\n2.Duracion Promedio\n3. Cantidad de temas sobre el promedio\n4.Salir\nElija una opcion:"))
  match respuesta:
    case 1:
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

    case 2:
      acumulador = 0

      for v in lista_bzrp:
        duracion = v["length"]
        acumulador += duracion

      promedio = acumulador / len(lista_bzrp)

      print(f"Duracion promedio: {promedio:0.2f}s")
    case 3:
      acumulador = 0

      for v in lista_bzrp:
        duracion = v["length"]
        acumulador += duracion

      promedio = acumulador / len(lista_bzrp)
  
      for v in lista_bzrp:
        duracion = v["length"]
        titulos = v["title"]
        if duracion > promedio:
          print(f"Titulo:{titulos} - Duracion:{duracion}s")
    case 4:
      break
