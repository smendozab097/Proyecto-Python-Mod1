
#Menu de opciones
option="0"
while option!="4":
    print("""
          *** MENU ***
        1. Agregar producto
        2. Mostrar inventario
        3. Calcular estadísticas
        4. Salir""")
    option = input("Ingresa el numero de la accion que deseas realizar: ").strip() #Elimina los espacios en blanco al inicio y al final de la entrada del usuario

    if option == "1":

        # Solicitud de datos al usuario y validación de entradas con try-except

        # Validar que nombre no esté vacío
        while True:
            try:
                nombre = input("Ingrese el nombre del producto: ").strip()
                if not nombre:
                    raise ValueError("El nombre no puede estar vacío.")
                break
            except ValueError as e:
                print(f"Error: {e}. Inténtalo de nuevo.")

        # Validar precio (convertir a float y mayor a cero)
        while True:
            valor = input("Ingrese el precio del producto: ").strip()
            if not valor:
                print("Error: El precio no puede estar vacío.")
                continue
            try:
                precio = float(valor)
                if precio <= 0:
                    raise ValueError("El precio debe ser mayor a cero.")
                break
            except ValueError as e:
                print(f"Error: {e}. Inténtalo de nuevo.")

        # Validar cantidad (convertir a int y mayor a cero)
        while True:
            valor = input("Ingrese la cantidad de unidades: ").strip()
            if not valor:
                print("Error: La cantidad no puede estar vacía.")
                continue
            try:
                cantidad = int(valor)
                if cantidad <= 0:
                    raise ValueError("La cantidad debe ser mayor a cero.")
                break
            except ValueError as e:
                print(f"Error: {e}. Inténtalo de nuevo.")

        # Cálculo del costo total y mensaje
        costo_total = precio * cantidad
        print(f"Producto '{nombre}' | Precio unitario: {precio:.2f} | Cantidad: {cantidad} | Costo total: {costo_total:.2f}")


