
#Menu de opciones
option="0"
while option!="4":
    print("""
          *** MENU ***
        1. Agregar producto
        2. Mostrar inventario
        3. Calcular estadísticas
        4. Salir""")
    option = input("Ingresa el numero de la accion que deseas realizar: ")

    if option == "1":

        #Solicitud de datos al usuario y validación de entradas

        #solicitud y validación del nombre del producto (no puede estar vacío ni ser numerico)
        nombre = input("Ingrese el nombre del producto: ")
        
        # while not nombre.isalpha(): #validacion de que no esté vacío y que no sean numeros (.isalpha)
        #     nombre = input("El nombre del producto no puede estar vacío ni ser un numero, ingresa un nombre de producto válido: ")

        #solicitud y validación del precio del producto (no puede estar vacío ni ser negativo o cero)
        precio = input("Ingrese el precio del producto: ") #El precio se pide como string para validar que no esté vacío y luego convertirlo a decimal
        while not precio or float(precio) <= 0:
            precio = input("Ingresa un valor válido (no vacío y mayor a cero): ")
        precio = float(precio)  # Convierte el precio a un número decimal

        #solicitud y validación de la cantidad de unidades (no puede estar vacía ni ser negativa o cero)
        cantidad = input("Ingrese la cantidad de unidades: ") #La cantidad se pide como string para validar que no esté vacía y luego convertirla a entero
        while not cantidad or int(cantidad) <= 0:
            cantidad = input("La cantidad no puede ser negativa o cero, ingresa un valor válido: ")
        cantidad = int(cantidad)  # Convierte la cantidad a un número entero


        #Cálculo del costo total y mensaje
        costo_total = precio * cantidad
        print(f"Producto '{nombre}' | Precio unitario: {precio:.2f} | Cantidad: {cantidad} | Costo total: {costo_total:.2f}")


