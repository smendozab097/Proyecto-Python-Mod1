def menu():
    """Muestra el menú principal con las opciones disponibles de gestión de inventario."""
    print("""
          *** MENU ***
        1. Agregar producto
        2. Mostrar inventario
        3. Buscar producto
        4. Actualizar producto
        5. Eliminar producto
        6. Calcular estadísticas
        7. Guardar CSV
        8. Cargar CSV
        9. Salir""")

def validar_entrada(mensaje, tipo, condicion=None, error_msg="Entrada inválida."):
    """Valida una entrada del usuario con tipo y condición personalizada.
    
    Args:
        mensaje (str): Mensaje a mostrar al usuario.
        tipo: Tipo de dato esperado (int, float, str, etc.).
        condicion (callable, optional): Función que valida la entrada. Defaults to None.
        error_msg (str): Mensaje de error personalizado. Defaults to "Entrada inválida.".
    
    Returns:
        El valor convertido al tipo especificado y validado.
    """
    while True:

        valor = input(mensaje).strip()
        if not valor:
            print(f"El campo no puede estar vacío.")
            continue

        try:
            convertido = tipo(valor)
            if condicion and not condicion(convertido):
                raise ValueError(error_msg)
            return convertido
        except ValueError as e:
            print(f"Error: {e}. Inténtalo de nuevo.")


def agregar_producto(inventario):
    """Agrega un nuevo producto al inventario.
    
    Solicita nombre, precio y cantidad, validando que no exista un producto con el mismo nombre.
    
    Args:
        inventario (list): Lista de productos del inventario.
    """
    while True:
        nombre = validar_entrada("Ingrese el nombre del producto: ", str, lambda x: not x.isdigit(), "El nombre puede contener numeros, pero no ser solo números.").lower()
        # Verificar si algún producto ya tiene ese nombre
        if any(p['nombre'] == nombre for p in inventario):
            print(f"Error: El producto '{nombre}' ya existe. Intente con otro nombre.")
        else:
            break # Si no existe, sale del bucle para pedir precio y cantidad
    precio = validar_entrada("Ingrese el precio del producto: ", float, lambda x: x > 0, "El precio debe ser un número positivo.")
    cantidad = validar_entrada("Ingrese la cantidad de unidades: ", int, lambda x: x > 0, "La cantidad debe ser un número positivo.")

    id = len(inventario) + 1
    producto = {
                "id": id, 
                "nombre": nombre, 
                "precio": precio, 
                "cantidad": cantidad}
    
    inventario.append(producto)
    print("-----------------------------------\n")
    print(f"Producto [{id}] agregado - nombre: {nombre} | precio: {precio} | cantidad: {cantidad}")
    print("\n-----------------------------------\n")


def mostrar_inventario(inventario):
    """Muestra todos los productos del inventario con su información.
    
    Args:
        inventario (list): Lista de productos a mostrar.
    """
    if not inventario:
        print("El inventario está vacío.")
        return
    print("\n-----------------------------------")
    print("""
          Inventario:
          """)
    for prod in inventario:
        print(f"- [{prod['id']}] {prod['nombre']}: Precio {prod['precio']:.2f}, Cantidad {prod['cantidad']}")
    print("\n-----------------------------------\n")

def buscar_producto(inventario, nombre):
    """Busca un producto en el inventario por nombre.
    
    Args:
        inventario (list): Lista de productos del inventario.
        nombre (str): Nombre del producto a buscar.
    """
    print("\n-----------------------------------\n")
    for p in inventario:
        if p['nombre'] == nombre:
            print(p)
            return
    print("Producto no encontrado.")


def actualizar_producto(inventario, nombre, nuevo_precio=None, nueva_cantidad=None):
    """Actualiza el precio y/o cantidad de un producto existente.
    
    Args:
        inventario (list): Lista de productos del inventario.
        nombre (str): Nombre del producto a actualizar.
        nuevo_precio (float, optional): Nuevo precio del producto. Defaults to None.
        nueva_cantidad (int, optional): Nueva cantidad del producto. Defaults to None.
    """
    for p in inventario:
        if p['nombre'] == nombre:
            if nuevo_precio is not None:
                if nuevo_precio <= 0:
                    print("Error: El precio debe ser positivo.")
                    return
                p['precio'] = nuevo_precio  # Ya es float
            if nueva_cantidad is not None:
                if nueva_cantidad <= 0:
                    print("Error: La cantidad debe ser positiva.")
                    return
                p['cantidad'] = nueva_cantidad  # Ya es int
            print("\n-----------------------------------\n")
            print(f"Producto '{nombre}' actualizado.")
            print(f"Nuevo Precio: {p['precio'] if nuevo_precio else 'Sin cambios'} | Nueva Cantidad: {p['cantidad'] if nueva_cantidad else 'Sin cambios'}.")
            print("\n-----------------------------------\n")
            return
    print("Producto no encontrado.")

def eliminar_producto(inventario, nombre):
    """Elimina un producto del inventario por nombre.
    
    Args:
        inventario (list): Lista de productos del inventario.
        nombre (str): Nombre del producto a eliminar.
    """
    inventario[:] = [p for p in inventario if p['nombre'] != nombre]
    print(f"Producto '{nombre}' eliminado.")
    print("\n-----------------------------------\n")


def calcular_estadisticas(inventario):
    """Calcula y muestra estadísticas del inventario.
    
    Calcula total de productos, valor total, producto más caro y con mayor stock.
    
    Args:
        inventario (list): Lista de productos del inventario.
    """
    if not inventario:
        print("No hay productos para calcular estadísticas.")
        return
    total_productos = sum(p['cantidad'] for p in inventario)
    valor_total = sum(p['precio'] * p['cantidad'] for p in inventario)
    p_caro = max(inventario, key=lambda p: p['precio'])
    p_stock = max(inventario, key=lambda p: p['cantidad'])
    estadisticas = {"total de productos": total_productos,
                    "valor total": valor_total,
                    "producto mas caro": p_caro,
                    "producto con mayor stock": p_stock}
    print("\n-----------------------------------\n")
    print(estadisticas)
    print("\n=== ESTADÍSTICAS DEL INVENTARIO ===")
    print(f"Unidades totales: {total_productos}")
    print(f"Valor total:      ${valor_total:,.2f}")
    print(f"Producto más caro: {p_caro['nombre']} (${p_caro['precio']:,.2f})")
    print(f"Mayor stock:      {p_stock['nombre']} ({p_stock['cantidad']} unidades)")
    print("===================================\n")
    print("\n-----------------------------------\n")