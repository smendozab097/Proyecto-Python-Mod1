#Menu de opciones
def mostrar_menu():
    print("""
          *** MENU ***
        1. Agregar producto
        2. Mostrar inventario
        3. Calcular estadísticas
        4. Salir""")

def validar_entrada(mensaje, tipo, condicion=None):
    while True:
        valor = input(mensaje).strip()
        if not valor:
            print(f"El campo no puede estar vacío.")
            continue
        try:
            convertido = tipo(valor)
            if condicion and not condicion(convertido):
                raise ValueError("El valor no cumple con la condición.")
            return convertido
        except ValueError as e:
            print(f"Error: {e}. Inténtalo de nuevo.")

def agregar_producto(inventario):
    nombre = validar_entrada("Ingrese el nombre del producto: ", str, lambda x: x)
    precio = validar_entrada("Ingrese el precio del producto: ", float, lambda x: x > 0)
    cantidad = validar_entrada("Ingrese la cantidad de unidades: ", int, lambda x: x > 0)
    producto = {"nombre": nombre, 
                "precio": precio, 
                "cantidad": cantidad}
    inventario.append(producto)
    costo_total = precio * cantidad
    print(f"Producto '{nombre}' agregado. Costo total: {costo_total:.2f}")

def mostrar_inventario(inventario):
    if not inventario:
        print("El inventario está vacío.")
        return
    print("Inventario:")
    for prod in inventario:
        print(f"- {prod['nombre']}: Precio {prod['precio']:.2f}, Cantidad {prod['cantidad']}")

def calcular_estadisticas(inventario):
    if not inventario:
        print("No hay productos para calcular estadísticas.")
        return
    total_productos = sum(p['cantidad'] for p in inventario)
    valor_total = sum(p['precio'] * p['cantidad'] for p in inventario)
    precio_promedio = valor_total / total_productos if total_productos > 0 else 0
    print(f"Estadísticas: Total productos: {total_productos}, Valor total: {valor_total:.2f}, Precio promedio: {precio_promedio:.2f}")
