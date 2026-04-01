#Menu de opciones
def menu():
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
    if not inventario:
        print("El inventario está vacío.")
        return
    print("\n-----------------------------------\n")
    print("""
          Inventario:
          """)
    for prod in inventario:
        print(f"- [{prod['id']}] {prod['nombre']}: Precio {prod['precio']:.2f}, Cantidad {prod['cantidad']}")
    print("\n-----------------------------------\n")

def buscar_producto(inventario, nombre):
    print("\n-----------------------------------\n")
    for p in inventario:
        if p['nombre'] == nombre:
            print(p)
            return
    print("Tarea no encontrada.")


def actualizar_producto(inventario, nombre, nuevo_precio=None, nueva_cantidad=None):

    for p in inventario:
        if p['nombre'] == nombre:
            if nuevo_precio:
                p['precio'] = int(nuevo_precio)
            if nueva_cantidad:
                p['cantidad'] = int(nueva_cantidad)
            print("\n-----------------------------------\n")
            print(f"Producto '{nombre}' actualizado.")
            print(f"Producto '{nombre}' | Nuevo Precio: {nuevo_precio} | Nueva Cantidad: {nueva_cantidad}.")
            print("\n-----------------------------------\n")
            return
    print("Producto no encontrado.")

def eliminar_producto(inventario, nombre):
    inventario = [p for p in inventario if p['nombre'] != nombre]
    print(f"Producto '{nombre}' eliminado.")
    print("\n-----------------------------------\n")


def calcular_estadisticas(inventario):
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