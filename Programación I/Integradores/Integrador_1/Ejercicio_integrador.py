from data_stark import lista_personajes

while True:
  console_input = int(input("\n1.Datos de todos los superhéroes\n2.Identidad y peso del superhéroe con mas fuerza\n3.Nombre e identidad del superhéroe mas bajo\n4.Peso promedio de los superhéroes masculinos\n5.Nombre y peso de los superhéroes que superan la fuerza promedio de los superhéroes femeninos\n6.Salir\nElija una opcion:"))
  match console_input:
    case 1:
      for hero in lista_personajes:
        name = hero["nombre"]
        identity = hero["identidad"]
        company = hero["empresa"]
        height = hero["altura"]
        weight = hero["peso"]
        gender = hero["genero"]
        eye_color = hero["color_ojos"]
        hair_color = hero["color_pelo"]
        strength = hero["fuerza"]
        intelligence = hero["inteligencia"] 
        print(f"Datos del heroe:\n{name}\n{identity}\n{company}\n{height}\n{weight}\n{gender}\n{eye_color}\n{hair_color}\n{strength}\n{intelligence}\n-----------------")
    case 2: 
      max_strenght = 0

      for hero in lista_personajes:
        strength = int(hero["fuerza"])
        if max_strenght < strength:
          max_strenght = strength

      for hero in lista_personajes:
        identity = hero["identidad"]
        weight = float(hero["peso"])
        if int(hero["fuerza"]) == max_strenght:
          print(f"Datos del heroe:\n{identity}\n{weight:0.2f}\n-----------------")
    case 3:
      min_height = 0
      hero_name = ""
      hero_identity = ""
      
      for hero in lista_personajes: 
        current = float(hero["altura"])
        min_height = current
        for sub_hero in lista_personajes:
          height = float(sub_hero["altura"])
          name = sub_hero["nombre"]
          identity = sub_hero["identidad"]
          if height < min_height:
            min_height = height
            hero_name = name
            hero_identity = identity

      print(f"\nDatos del héroe:\n{hero_name}\n{hero_identity}")
    case 4:
      m_total_weight = 0
      m_hero_quantity = 0

      for hero in lista_personajes:
        weight = float(hero["peso"])
        gender = hero["genero"]
        if gender == "M":
          m_hero_quantity += 1
          m_total_weight += weight

      average_m_weight = m_total_weight / m_hero_quantity

      print(f"Peso promedio: {average_m_weight:0.2f}")
    case 5:
      f_hero_quantity = 0
      f_total_strength = 0

      for hero in lista_personajes:
        strength = int(hero["fuerza"])
        gender = hero["genero"]
        if gender == "F":
          f_hero_quantity += 1
          f_total_strength += strength

      average_f_strength = f_total_strength / f_hero_quantity

      for hero in lista_personajes:
        weight = float(hero["peso"])
        name = hero["nombre"]
        strength = int(hero["fuerza"])
        if strength > average_f_strength:
          print(f"Datos del heroe:\n{name}\n{weight:0.2f}\n-----------------")
    case 6:
      break
    case _:
      print("Por favor seleccione una opcion válida\n")