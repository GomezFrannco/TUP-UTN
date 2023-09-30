add_data_message = "1. CARGAR DATOS\n0. SALIR\n---------->  "

# name_list = []
# amount_list = []
# quantity_list = []
# instrument_type_list = []

# datos de prueba
name_list = ["Empresa A", "Empresa B", "Empresa C", "Empresa D"]
amount_list = [50000, 75000, 60000, 90000]
quantity_list = [100, 150, 120, 180]
instrument_type_list = ["CEDEAR", "BONOS", "CEDEAR", "MEP"]

# mensajes destinados al input
name_input_message = "Ingrese el nombre: "
amount_input_message = "Ingrese el monto de la operación (no menor a $10000): "
quantity_input_message = "Ingrese la cantidad de instrumentos: "
instrument_type_input_message = "Tipo de instrumento (CEDEAR, BONOS, MEP): "

while True:
  add_data = input(add_data_message)
  
  match add_data:
    case "1":
      add_data_message = "1. CARGAR MÁS DATOS\n2. MOSTRAR INFORME\n0. SALIR\n---------->  "
      
      # validaciones de inputs por medio de un while
      while True:
        name = input(name_input_message)
        if len(name) > 0:
          break
      while True:
        amount = input(amount_input_message)
        # validacion de números
        if amount.isdigit():
          amount = int(amount)
          if amount >= 10000:
            break
      while True:
        quantity = input(quantity_input_message)
        # validacion de números
        if quantity.isdigit():
          quantity = int(quantity)
          if quantity > 0:
            break
      while True:
        instrument_type = input(instrument_type_input_message)
        instrument_type = instrument_type.upper()
        # validación de instrumentos
        if instrument_type == "CEDEAR" or instrument_type == "BONOS" or instrument_type == "MEP":
          break
      # agregar datos a listas para procesarlos  
      name_list.append(name)
      amount_list.append(amount)
      quantity_list.append(quantity)
      instrument_type_list.append(instrument_type)
      # mensaje de lo que se ingresó
      output_message = f"""
        nombre: {name}\n
        monto: {amount}\n
        instumentos:{quantity}\n
        tipo: {instrument_type}
      """

      print(output_message)

    case "2":
      cedear_count = 0
      bonos_count = 0
      mep_count = 0

      most_operated_instrument = None
      # dado que en este caso solo hay 3 instrumentos 
      # voy a obviar la posibilidad de comparar y contar
      # elementos, y # asi, solo comparar igualdades
      for instrument in instrument_type_list:
        if instrument == "CEDEAR":
          cedear_count += 1
        if instrument == "BONOS":
          bonos_count += 1
        if instrument == "MEP":
          mep_count += 1
      
      # utilizo estructuras if else para encontrar el mayor
      if cedear_count > bonos_count and cedear_count > mep_count:
        most_operated_instrument = "CEDEAR"
      elif bonos_count > mep_count and bonos_count > cedear_count:
        most_operated_instrument = "BONOS"
      elif mep_count > cedear_count and mep_count > bonos_count:
        most_operated_instrument = "MEP"
      else:
        most_operated_instrument = "NINGUN BONO FUE EL MÁS OPERADO QUE OTRO"
      print(f"Tipo de instrumento que más se operó: {most_operated_instrument}\n")
      # -------------------------------------------------------------------------- #
      investor_count = 0
      for i in range(len(name_list)):
        if quantity_list[i] > 150 and quantity_list[i] < 200 and amount_list[i] > 50000:
          investor_count += 1
      print(f"Cantidad de usuarios que compraron entre 150 y 200 BONOS y que invirtieron más de $50000: {investor_count}\n")
      # -------------------------------------------------------------------------- #
      smaller_investment = float('inf')
      flag = False

      for i in range(len(amount_list)):
        if instrument_type_list[i] == "BONOS" or instrument_type_list[i] == "MEP":
          if amount_list[i] < smaller_investment or flag == True:
            smaller_investment = amount_list[i]
            flag = True
            
      print("Nombre y cantidad de instrumentos del usuario que compró BONOS o MEP, que menos dinero invirtió:\n")
      for i in range(len(amount_list)):
        if instrument_type_list[i] == "BONOS" or instrument_type_list[i] == "MEP":
          if amount_list[i] == smaller_investment:
            print(f"Nombre: {name_list[i]}\nCantidad de instrumentos: {quantity_list[i]}")
      # -------------------------------------------------------------------------- #
      average_investment = 0
      total_investments = 0
      amount_of_investments = len(amount_list)

      for amount in amount_list:
        total_investments += amount

      if amount_of_investments > 0:
        average_investment = total_investments / amount_of_investments

      print("\nNombre de los usuarios que invirtieron en CEDEAR, cuya inversión supere el monto promedio:\n")
      for i in range(len(name_list)):
        if instrument_type_list[i] == "CEDEAR":
          if amount_list[i] > average_investment:
            print(name_list[i])

    case "0":
      print("HASTA LUEGO :D")
      break

    case _:
      print("\nINGRESE UNA OPCIÓN VÁLIDA\n")