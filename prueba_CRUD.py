# --- CRUD SIN BASE DE DATOS (En memoria) ---

# 1. Almacenamiento (La "tabla")
tareas = []

# --- C: Crear (Create) ---
def crear_tarea(titulo, estado):

    tarea = {"id": len(tareas) + 1, 
             "titulo": titulo, 
             "completada": estado}
    
    tareas.append(tarea)
    print(f"Tarea creada: {titulo}, completada: {estado}")

# --- R: Leer (Read) ---
def leer_tareas():
    print("\n--- Lista de Tareas ---")
    for t in tareas:
        print(f"[{t['id']}] {t['titulo']} - Completada: {t['completada']}")
    print("-----------------------\n")

# --- U: Actualizar (Update) ---
def actualizar_tarea(id, nuevo_titulo, nuevo_estado):
    for t in tareas:
        if t['id'] == id:
            t['titulo'] = nuevo_titulo
            t['completada'] = nuevo_estado
            print(f"Tarea {id} actualizada.")
            return
    print("Tarea no encontrada.")

# --- D: Borrar (Delete) ---
def eliminar_tarea(id):
    global tareas
    tareas = [t for t in tareas if t['id'] != id]
    print(f"Tarea {id} eliminada.")

# --- Ejemplo de uso ---

#Menu de opciones
option="0"
while option!="4":
    print("""
        **** MENU ****
        1. Crear Tarea
        2. Mostrar Tarea
        3. Actualizar Tarea
        4. Eliminar Tarea
        5.Salir""")
    
    option = input("Ingresa el numero de la accion que deseas realizar: ").strip()

    if option == "1":

        # Solicitud de tarea y validación de entradas con try-except
        # Validar que nombre no esté vacío
        while True:
            try:
                titulo=input("Ingresa el titulo de la tarea: ")
                estado=input("Tarea completada? S/N: ").upper()
                if estado=="S":
                    estado=True
                else: estado=False
                crear_tarea(titulo, estado)

                if not titulo:
                    raise ValueError("El nombre no puede estar vacío.")
                break
            except:
                print(f"Error. Inténtalo de nuevo.")

    if option == "2":
        leer_tareas()

    if option == "3":
        id = int(input("ingresa el numero de la tarea que quieres actualizar: "))
        nuevotitulo = input("ingresa el nuevo titulo de la tarea o deja en blanco para mantener: ")
        if nuevotitulo =="":
            nuevotitulo=titulo
        nuevoestado = input("Esta completa la tarea? S/N").upper()
        if nuevoestado == "S":
            nuevoestado=True
        else: nuevoestado=estado
        actualizar_tarea(id, nuevotitulo, nuevoestado)

        


# crear_tarea("Aprender Python")
# crear_tarea("Hacer CRUD")
# leer_tareas()  # Muestra: Aprender Python, Hacer CRUD

# actualizar_tarea(1, "Aprender Python Avanzado")
# eliminar_tarea(2)

# leer_tareas()  # Muestra: Aprender Python Avanzado
