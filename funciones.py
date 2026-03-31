inventario=[]

def menu():
    print("""
          *** MENU ***
        1. Agregar producto
        2. Mostrar inventario
        3. Buscar producto
        4. Actualizar producto
        5. Eliminar producto
        6. Calcular estadísticas
        7. Salir""")
    
def agregar_producto():
    # Solicitud de datos al usuario y validación de entradas con try-except
    while True:
        try:
            nombre = input("Ingrese el nombre del producto: ").strip() # Validar que nombre no esté vacío
            if not nombre or nombre.isdigit()==True:
                raise ValueError("El nombre no puede estar vacío ni ser solo numeros.")
            break
            
        except:
            print(f"Error: El nombre no puede estar vacío ni ser solo numeros. Inténtalo de nuevo.")
        
        for producto in inventario:
            if producto['nombre'] == nombre:
                print(f"Error: {nombre} ya existe.")
                

    
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
        except:
            print(f"Error: El precio debe ser un numero mayor a cero. Inténtalo de nuevo.")

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
        except:
            print(f"Error: La cantidad debe ser mayor a cero. Inténtalo de nuevo.")

    id=len(inventario) + 1
    producto = {"id": id, 
             "nombre": nombre, 
             "precio": precio,
             "cantidad": cantidad
             }
    
    inventario.append(producto)
    print(f"Producto [{id}] agregado - nombre: {nombre} | precio: {precio} | cantidad: {cantidad}")

def mostrar_productos():
    print("""
    --- Inventario de inventario ---
ID producto |   precio  |   cantidad    |""")
    for p in inventario:
        print(f"[{p['id']}] {p['nombre']} | {p['precio']} | {p['cantidad']}")
    print("-----------------------\n")

def buscar_producto(id, nombre):
    for p in inventario:
        if p['id'] == id:
            # p['titulo'] = nuevo_titulo
            # p['completada'] = nuevo_estado
            print(f"Producto {id} actualizada.")
            return
    print("Tarea no encontrada.")


def actualizar_producto(id, nombre, nuevo_precio, nueva_cant):
    id = int(input("ingresa el numero del producto que quieres actualizar: "))
    nuevo_precio = int(input("ingresa el nuevo titulo de la tarea o deja en blanco para mantener: ").strip())
    if nuevo_precio =="":
        nuevo_precio=precio
    nueva_cantidad = int(input("Esta completa la tarea? S/N"))
    if nueva_cantidad == "":
        nueva_cantidad=cantidad
    else: nueva_cantidad=estado
    for p in inventario:
        if p['id'] == id:
            p['nombre'] == nombre
            p['precio'] = nuevo_precio
            p['cantidad'] = nueva_cant
            print(f"Tarea {id} actualizada.")
            print(f"Producto [{id}] {nombre} | Nuevo Precio: {nuevo_precio} | Nueva Cantidad: {nueva_cant}.")
            return
    print("Tarea no encontrada.")