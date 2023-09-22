from data_stark import lista_personajes

# 1.0 ✅
def stark_normalizar_datos(hero_list: list) -> bool:
    """
    @brief Recorre una lista de diccionarios y convierte los strings con números a su tipo de dato correcto (entero o flotante).

    @param hero_list: Una lista de diccionarios.
    @type hero_list: Lista.
    
    @return valor booleano (True o False)
    """
    modifications = 0

    if len(hero_list) == 0:
        return False
    
    for hero in hero_list:
        # bucle anidado que recorre los valores de cada diccionario
        for key, value in hero.items():
            # ignora valores de tipo entero o flotante
            if isinstance(value, int) or isinstance(value, float):
                pass
            # valida valores que no sean vacíos y que en su primer posición contenga un dígito
            elif len(value) > 0 and value[0].isdigit():
                # en caso de que contenga un punto es un float
                if '.' in value:
                    hero[key] = float(value)
                    modifications += 1
                # de otro modo es un entero
                else: 
                    hero[key] = int(value)
                    modifications += 1

    if modifications > 0:
        return True
    else:
        return False

# print(stark_normalizar_datos(lista_personajes))

# 1.1 ✅
def obtener_nombre(hero: dict) -> bool or str:
    """
    @brief Según un diccionario que representa a un heroe, valida si no esta vacio y si existe la key 'nombre'.

    @param hero: Un heroe en forma de diccionario.
    @type hero: Diccionario.

    @return valor booleano (True o False) o un string con el nombre del heroe.
    """
    if len(hero) == 0 or "nombre" not in hero:
        return False
    else:
        hero_name = f"Nombre: {hero['nombre']}"
        return hero_name

# print(obtener_nombre(lista_personajes[1]))

# 1.2 ✅
def obtener_dato(hero: dict, key: str) -> bool or str:
    """
    @brief

    @param
    @type
    @param
    @type

    @return
    """
    key = key.lower()
    if len(hero) == 0 or key not in hero:
        return False
    else:
        return hero[key]

# print(obtener_dato(lista_personajes[0], "Nombre"))

# 2.0 ✅
def obtener_dato_y_nombre(hero: dict, key: str):
    """
    @brief

    @param
    @type
    @param
    @type

    @return
    """
    key = key.lower()
    if len(hero) == 0:
        return False
    else:
        hero_name = obtener_nombre(hero)
        hero_data = obtener_dato(hero, key)
        if hero_name == False or hero_data == False:
            return False
        else:
            hero_info = f"{hero_name} | {key}: {hero_data}"
            return hero_info

# print(obtener_dato_y_nombre(lista_personajes[18], "IDENTIDAD"))

# 3.1 ✅
def obtener_maximo(data_list: list, key: str) -> bool or int or float:
    """
    @brief

    @param
    @type
    @param
    @type

    @return
    """
    key = key.lower()
    max_value = 0
    if len(data_list) == 0:
        return False
    
    for hero in data_list:
        if isinstance(hero[key], int) or isinstance(hero[key], float):
            if hero[key] > max_value:
                max_value = hero[key]
        else:
            return False
    
    return max_value

# print(obtener_maximo(lista_personajes, "fuerza"))

# 3.2 ✅
def obtener_minimo(data_list: list, key: str) -> bool or int or float:
    """
    @brief

    @param
    @type
    @param
    @type

    @return
    """
    key = key.lower()
    min_value = float('inf')

    if len(data_list) == 0:
        return False

    for hero in data_list:
        if isinstance(hero[key], int) or isinstance(hero[key], float):
            if hero[key] < min_value:
                min_value = hero[key]
        else:
            return False

    return min_value

# print(obtener_minimo(lista_personajes,"fuerza"))

# 3.3 ✅
def obtener_dato_cantidad(data_list: list, cantidad: int or float, key: str) -> list:
    key = key.lower()
    hero_list = []
    if len(data_list) == 0:
        return False
    else:
        for hero in data_list:
            if hero[key] == cantidad:
                hero_list.append(hero)
        return hero_list

#value = obtener_maximo(lista_personajes, "fuerza")
#print(obtener_dato_cantidad(lista_personajes, value, "fuerza"))

# 3.4 ✅
def stark_imprimir_heroes(data_list: list):
    if len(data_list) == 0:
        return False
    else:
        for hero in data_list:
            print("\n")
            for key, value in hero.items():
                print(f"{key}: {value}")

#stark_imprimir_heroes(lista_personajes)

# 4.1 ✅
def sumar_dato_heroe(data_list: list, key: str):
    key = key.lower()
    total_value = 0
    if len(data_list) == 0:
        return False    
    else:
        for hero in data_list:
            if isinstance(hero, dict) and len(hero) > 0:
                total_value += hero[key]
        return total_value
            
#print(sumar_dato_heroe(lista_personajes, "fuerza"))

# 4.2 ✅
def dividir(dividendo: int, divisor: int):
    if divisor == 0:
        return False
    else:
        return round(dividendo / divisor, 2)

#print(dividir(90, 0))

# 4.3 ✅
def calcular_promedio(data_list: list, key: str):
    key = key.lower()
    total_value = sumar_dato_heroe(data_list, key)
    values_count = 0

    if len(data_list) == 0:
        return False
    
    for hero in data_list:
        if key in hero:
            values_count += 1

    return dividir(total_value, values_count)

#print(calcular_promedio(lista_personajes, "fuerza"))

# 4.4 ✅
def mostrar_promedio_dato(data_list: list, key: str):
    key = key.lower()

    if len(data_list) == 0:
        return False
    
    for hero in data_list:
        if isinstance(hero[key], int) or isinstance(hero[key], float):
            average = calcular_promedio(data_list, key)
            return f"{key} promedio: {average}"
        else:
            return False

# 5.1 ✅
def imprimir_menu():
    print("\n|======================[MENÚ]======================|")
    print("1.  NORMALIZAR DATOS")
    print("2.  NOMBRE DE HÉROES DE GÉNERO NB")
    print("3.  HÉROE MÁS ALTO DE GÉNERO F")
    print("4.  HÉROE MÁS ALTO DE GÉNERO M")
    print("5.  HÉROE MÁS DÉBIL DE GÉNERO M")
    print("6.  HÉROE MÁS DÉBIL DE GÉNERO NB")
    print("7.  FUERZA PROMEDIO DE HÉROES DE GÉNERO NB")
    print("8.  CANTIDAD DE HÉROES POR COLOR DE OJOS")
    print("9.  CANTIDAD DE HÉROES POR COLOR DE PELO")
    print("10. LISTA DE HÉROES POR COLOR DE OJOS")
    print("11. LISTA DE HÉROES POR COLOR DE INTELIGENCIA")
    print("12. SALIR")
    print("|==================================================|")

# imprimir_menu()

# 5.2 ✅
def validar_entero(number: str) -> bool:
    return number.isdigit()

# print(validar_entero("55545s"))

# 5.3 ✅
def stark_menu_principal():
    
    imprimir_menu()

    user_input = input("[ELIJA UNA OPCIÓN]--------->  ")

    if validar_entero(user_input):
        return int(user_input)
    else:
        return False
    
# print(stark_menu_principal())

# adicional ✅
def obtener_heroes_por_genero(data_list: list, gender: str):
    hero_list = []
    if len(data_list) == 0 or not isinstance(gender, str) or len(gender) == 0:
        return False
    else:
        gender = gender.upper()
        for hero in data_list:
            if obtener_dato(hero, "gEneRO") == gender:
                hero_list.append(hero)
        return hero_list

# print(obtener_heroes_por_genero(lista_personajes, "f"))

# 6.0 ❌
def stark_marvel_app(data_list: list):
    normalized_data = False

    while True:
        user_input = stark_menu_principal()

        if normalized_data != True and user_input != 1 and user_input != 9:
            print("Debe normalizar los datos primero (Opción 1)")
            continue

        match user_input:
            case 1:
                if stark_normalizar_datos(data_list):
                    print("Datos correctamente normalizados")
                    normalized_data = True
                else:
                    print("Error al normalizar los datos: Verifique que la lista no este vacía o que los datos no hayan normalizado previamente")

            case 2:
                nb_heros = obtener_heroes_por_genero(data_list, "nb")
                
                for hero in nb_heros:
                    print(obtener_nombre(hero))

            case 3:
                key = "altURA"
                f_heros = obtener_heroes_por_genero(data_list, "f")
                
                hero_height = obtener_maximo(f_heros, key)
                
                for hero in f_heros:
                    if obtener_dato(hero, key) == hero_height:
                        print(obtener_dato_y_nombre(hero, key))

            case 4:
                key = "aLtuRA"
                m_heros = obtener_heroes_por_genero(data_list, "m")
                
                hero_height = obtener_maximo(m_heros, key)
                
                for hero in m_heros:
                    if obtener_dato(hero, key) == hero_height:
                        print(obtener_dato_y_nombre(hero, key))

            case 5:
                key = "fuerza"
                m_heros = obtener_heroes_por_genero(data_list, "m")
                
                hero_strength = obtener_minimo(m_heros, key)
                
                for hero in m_heros:
                    if obtener_dato(hero, key) == hero_strength:
                        print(obtener_dato_y_nombre(hero, key))

            case 6:
                key = "fuerza"
                m_heros = obtener_heroes_por_genero(data_list, "nb")
                
                hero_strength = obtener_minimo(m_heros, key)
                
                for hero in m_heros:
                    if obtener_dato(hero, key) == hero_strength:
                        print(obtener_dato_y_nombre(hero, key))

            case 7:
                nb_heros = obtener_heroes_por_genero(data_list, "nb")

                print(mostrar_promedio_dato(nb_heros, "fuerza"))
                
            case 8:
                print(f"Opción {user_input}")
            case 9:
                print(f"Opción {user_input}")
            case 10:
                print(f"Opción {user_input}")
            case 11:
                print(f"Opción {user_input}")
            case 12:
                print("CHAU")
                break
            case _:
                print(f"Opción no válida: {user_input}")

stark_marvel_app(lista_personajes)