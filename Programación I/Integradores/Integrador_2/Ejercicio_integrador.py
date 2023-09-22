from data_stark import lista_personajes

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
        hero_info = f"{key}: {hero[key]}"
        return hero_info

# print(obtener_dato(lista_personajes[0], "Nombre"))

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
            hero_info = f"{hero_name} | {hero_data}"
            return hero_info

# print(obtener_dato_y_nombre(lista_personajes[18], "IDENTIDAD"))

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

def obtener_dato_cantidad(data_list: list, cantidad: int or float, key: str):
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

def stark_imprimir_heroes(data_list: list):
    key = key.lower()
    if len(data_list) == 0:
        return False
    else:
        for hero in data_list:
            print("\n")
            for key, value in hero.items():
                print(f"{key}: {value}")

#stark_imprimir_heroes(lista_personajes)

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

def dividir(dividendo: int, divisor: int):
    if divisor == 0:
        return False
    else:
        return int(dividendo / divisor)

#print(dividir(90, 0))

def calcular_promedio(data_list: list, key: str):
    key = key.lower()
    total_value = 0
    values_count = 0 
    if len(data_list) == 0:
        return False 
    for hero in data_list:
        if key in hero:
            values_count += 1
            total_value += hero[key] 

    return round(float(total_value / values_count), 2)

#print(calcular_promedio(lista_personajes, "fuerza"))