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
                else: 
                    hero[key] = int(value)
                    modifications += 1

    if modifications > 0:
        return True
    else:
        return False

# 1.1 ✅
def obtener_nombre(hero: dict) -> bool or str:
    """
    @brief Valida si un diccionario no esta vacio y si existe la key 'nombre'.

    @param hero: Un heroe en forma de diccionario.
    @type hero: Diccionario.

    @return False si no existe la key o si el diccionario esta vacío y un string con el nombre del heroe.
    """
    if len(hero) == 0 or "nombre" not in hero:
        return False
    else:
        hero_name = f"Nombre: {hero['nombre']}"
        return hero_name

# 1.2 ✅
def obtener_dato(hero: dict, key: str) -> bool or str:
    """
    @brief Muestra el valor de una clave en un diccionario.

    @param hero: Un heroe en forma de diccionario.
    @type hero: Diccionario.
    @param key: La clave de la cual se desea obtener el valor.
    @type key: String.

    @return El valor de la key solicitada y False si no existe la key o si el diccionario esta vacío.
    """
    key = key.lower()

    if len(hero) == 0 or key not in hero:
        return False
    else:
        return hero[key]

# 2.0 ✅
def obtener_dato_y_nombre(hero: dict, key: str) -> bool or str:
    """
    @brief muestra el nombre junto del heroe con un valor solicitado mediante una key

    @param hero: Un heroe en forma de diccionario.
    @type hero: Diccionario.
    @param key: La clave de la cual se desea obtener el valor.
    @type key: String.

    @return False si el diccionario esta vacio o si no existe la key y un string con el nombre y el dato solicitado
    """
    key = key.lower()

    if len(hero) == 0 or key not in hero:
        return False
    else:
        hero_name = obtener_nombre(hero)
        hero_data = obtener_dato(hero, key)

        if hero_name == False or hero_data == False:
            return False
        else:
            hero_info = f"{hero_name} | {key}: {hero_data}"
            return hero_info

# 3.1 ✅
def obtener_maximo(data_list: list, key: str) -> bool or int or float:
    """
    @brief determina el valor máximo de una clave dentro de un diccionario en una lista de diccionarios

    @param data_list: Una lista con diccionarios.
    @type data_list: Lista.
    @param key: Clave de la cual necesitamos el valor máximo.
    @type key: string.

    @return el número máximo como entero o decimal y False si la lista esta vacia o si el valor no es un numero.
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

# 3.2 ✅
def obtener_minimo(data_list: list, key: str) -> bool or int or float:
    """
    @brief determina el valor mínimo de una clave dentro de un diccionario en una lista de diccionarios.

    @param data_list: Una lista con diccionarios.
    @type data_list: Lista.
    @param key: Clave de la cual necesitamos el valor máximo.
    @type key: string.

    @return el número máximo como entero o decimal y False si la lista esta vacia o si el valor no es un numero.
    """
    key = key.lower()
    # se establece un número alto para poder comparar numeros menores al actual
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

# 3.3 ✅
def obtener_dato_cantidad(data_list: list, cantidad: int or float, key: str) -> list or bool:
    """
    @brief devuelve una lista con los heroes que cumplan con la cantidad solicitada para determinada key.

    @param data_list: Una lista de diccionarios.
    @type data_list: Lista.
    @param cantidad: La cantidad buscada.
    @type cantidad: Integer o float.
    @param key: Clave de la cual necesitamos el valor máximo.
    @type key: String.

    @return una lista con los valores encontrados o False
    """
    key = key.lower()
    hero_list = []
    
    if len(data_list) == 0:
        return False
    else:
        for hero in data_list:
            if hero[key] == cantidad:
                hero_list.append(hero)
        return hero_list

# 3.4 ✅
def stark_imprimir_heroes(data_list: list) -> None or bool:
    """
    @brief recorre una lista de diccionarios e imprime todos sus pares clave valor.

    @param data_list: Una lista de diccionarios.
    @type data_list: Lista.

    @return False o imprime por consola los datos de los diccionarios.
    """

    if len(data_list) == 0:
        return False
    else:
        for hero in data_list:
            print("\n")
            for key, value in hero.items():
                print(f"{key}: {value}")

# 4.1 ✅
def sumar_dato_heroe(data_list: list, key: str) -> bool or int or float:
    """
    @brief suma todos los valores de los diccionarios dentro de una lista.

    @param data_list: Una lista de diccionarios.
    @type data_list: Lista.
    @param key: La clave de la cual se desea sumar todos los valores.
    @type key: String.

    @return False o la cantidad sumada.
    """

    key = key.lower()
    total_value = 0
    
    if len(data_list) == 0:
        return False    
    else:
        for hero in data_list:
            if isinstance(hero, dict) and len(hero) > 0:
                total_value += hero[key]
        return total_value
            
# 4.2 ✅
def dividir(dividendo: int or float|, divisor: int or float) -> int or float or bool:
    """
    @brief divide dos numeros y devuelve el resultado.

    @param dividendo: Número al cual se va a dividir.
    @type dividendo: Integer o float.
    @param divisor: Número que divide al del parametro anterior.
    @type divisor: Integer o float.

    @return False o el resultado de la división
    """

    if divisor == 0:
        return False
    else:
        return round(dividendo / divisor, 2)

# 4.3 ✅
def calcular_promedio(data_list: list, key: str) bool or int or float:
    """
    @brief calcula el promedio de los valores encontrados en determinada key.

    @param data_list: Lista de diccionarios.
    @type data_list: Lista.
    @param key: Clave del valor del cual necesitamos el promedio.
    @type key: String.

    @return False o el promedio entre los valores de la key.
    """

    key = key.lower()
    total_value = sumar_dato_heroe(data_list, key)
    values_count = 0

    if len(data_list) == 0:
        return False
    
    for hero in data_list:
        if key in hero:
            values_count += 1

    return dividir(total_value, values_count)

# 4.4 ✅
def mostrar_promedio_dato(data_list: list, key: str) -> str or bool:
    """
    @brief muestra el promedio calculado de determinada key.

    @param data_list: Lista de diccionarios.
    @type data_list: Lista.
    @param key: Clave del valor del cual necesitamos el promedio.
    @type key: String.

    @return un string con el promedio calculado o False.
    """

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
def imprimir_menu() -> None:
    """
    @brief muestra por consola una serie de opciones que forman un menú.

    @return None
    """

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
    print("11. LISTA DE HÉROES POR INTELIGENCIA")
    print("12. SALIR")
    print("|==================================================|")

# 5.2 ✅
def validar_entero(number: str) -> bool:
    """
    @brief valida que un string contenga números y sea un número

    @param number: El string que debería ser un número.
    @type number: String.

    @return True si es un número o False.
    """

    return number.isdigit()

# 5.3 ✅
def stark_menu_principal() -> int or bool:
    """
    @brief despliega el menu por consola y solicita un input al usuario

    @return un entero previamente validado o False
    """
    
    imprimir_menu()

    user_input = input("[ELIJA UNA OPCIÓN]--------->  ")

    if validar_entero(user_input):
        return int(user_input)
    else:
        return False
    
# adicional ✅
def obtener_heroes_por_genero(data_list: list, gender: str) -> list or bool:
    """
    @brief genera una lista de heroes de determinado género.

    @param data_list: Lista de diccionarios.
    @type data_list: Lista.
    @param gender: Genero solicitado.
    @type gender: String.

    @return False o una lista de diccionarios.
    """

    hero_list = []

    if len(data_list) == 0 or not isinstance(gender, str) or len(gender) == 0:
        return False
    else:
        gender = gender.upper()

        for hero in data_list:
            if obtener_dato(hero, "gEneRO") == gender:
                hero_list.append(hero)

        return hero_list

# adicional ✅
def contar_repetidos(data_list: list) -> bool or dict:
    """
    @brief cuenta la cantidad de elementos repetidos que hay dentro de una lista.

    @param data_list: Una lista con elementos.
    @type data_list: Lista.

    @return False o un diccionario.
    """

    n = len(data_list)
    values_dict = {}
    
    if n == 0:
        return False

    for i in range(0, n):
        count = 0
        
        for j in range(0, n):
            # valido si el indice actual es mayor al comparado y si los elementos son iguales
            if i > j and data_list[i] == data_list[j]:
                break
            # valida si los elementos son iguales
            if data_list[i] == data_list[j]:
                count += 1
            else:
                pass
        # valida que al menos haya un elemento contado
        if count != 0:
            # crea una clave llamada como el elemento actual y le asigna el contador
            values_dict[data_list[i]] = count

    return values_dict

# 6.0 ✅
def stark_marvel_app(data_list: list) -> None:
    """
    @brief Se encarga de ejecutar el menú y la lógica detras de la selección de opciones.

    @param
    @type
    @param
    @type

    @return
    """

    normalized_data = False

    while True:
        user_input = stark_menu_principal()

        if normalized_data != True and user_input != 1 and user_input != 12:
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
                key = "color_ojos"
                eye_color_list = []

                for hero in data_list:
                    eye_color_list.append(obtener_dato(hero, key))
                
                color_count = contar_repetidos(eye_color_list)

                stark_imprimir_heroes([color_count])
                #for k, v in color_count.items():
                 #   print(f"color {k}: {v} héroes")

            case 9:
                key = "Color_peLO"
                hair_color_list = []

                for hero in data_list:
                    hair_color_list.append(obtener_dato(hero, key))
                
                color_count = contar_repetidos(hair_color_list)
                
                stark_imprimir_heroes([color_count])

                #for k, v in color_count.items():
                 #   print(f"color {k}: {v} héroes")

            case 10:
                key = "color_PELO"
                hero_dict = {}

                for i in range(len(data_list)):
                    # valor actual en la iteración
                    current_color = obtener_dato(data_list[i], key)
                    # se crea una lista temporal
                    current_list = []
                    # inicia un bucle para comparar el color actual con todos los demas
                    for j in range(len(data_list)):         
                        # valor a comparar con el de la iteración actual del bucle anterior     
                        compare = obtener_dato(data_list[j], key)
                        # valida que no compare con un elemento anterior del mismo valor
                        if i > j and current_color == compare:
                            break
                           
                        if current_color == compare:
                            # crea una key de nombre igual al valor del primer bucle
                            hero_dict[current_color] = None
                            # agrega la coincidencia dentro de la lista temporal
                            current_list.append(obtener_nombre(data_list[j]))
                    
                    if len(current_list) != 0:
                        # se cambia el valor None por el de la lista temporal
                        hero_dict[current_color] = current_list

                stark_imprimir_heroes([hero_dict])

            case 11:
                key = "inteligencia"
                hero_dict = {}

                for i in range(len(data_list)):
                    # valor actual en la iteración
                    current_color = obtener_dato(data_list[i], key)
                    # se crea una lista temporal
                    current_list = []
                    # inicio un bucle para comparar el color actual con todos los demas
                    for j in range(len(data_list)):         
                        # valor a comparar con el de la iteración actual del bucle anterior              
                        compare = obtener_dato(data_list[j], key)
                        # valida que no compare con un elemento anterior del mismo valor 
                        if i > j and current_color == compare:
                            break
                           
                        if current_color == compare:
                            # crea una key de nombre igual al valor del primer bucle
                            hero_dict[current_color] = None
                            # agrega la coincidencia dentro de la lista temporal
                            current_list.append(obtener_nombre(data_list[j]))

                    if len(current_list) != 0:
                        # se cambia el valor None por el de la lista temporal
                        hero_dict[current_color] = current_list

                stark_imprimir_heroes([hero_dict])
            
            case 12:
                print("Hasta luego :D")
                break
                
            case _:
                print(f"Opción no válida: {user_input}\n Seleccione una opción válida")

stark_marvel_app(lista_personajes)
