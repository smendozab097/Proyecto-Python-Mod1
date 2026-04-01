from servicios import *
from archivos import *

# Programa principal
inventario = []
ruta_archivo = "inventario.csv"
opcion = 0
while opcion != 9:
    menu()
    try:
        opcion = int(input("\nIngresa la accion que deseas realizar (1-9): ").strip())
        if opcion < 1 or opcion > 9:
            print("Error: Debes ingresar un número entre 1 y 9.")
            opcion = 0
            continue
    except ValueError:
        print("Error: Entrada inválida. Por favor, ingresa un número.")
        opcion = 0
        continue
    if opcion == 1:
        agregar_producto(inventario)

    elif opcion == 2:
        mostrar_inventario(inventario)

    elif opcion == 3:
        nombre_busqueda = input("Ingresa el nombre del producto que quieres buscar: ").strip()
        buscar_producto(inventario, nombre_busqueda)

    elif opcion == 4:
        nombre = input("Ingresa el nombre del producto que quieres actualizar: ").strip()

        nuevo_precio = input("Ingresa el nuevo precio del producto o deja en blanco para mantener: ").strip()
        nuevo_precio = float(nuevo_precio) if nuevo_precio else None
            
        nueva_cantidad = input("Ingresa la nueva cantidad del producto o deja en blanco para mantener: ").strip()
        nueva_cantidad = int(nueva_cantidad) if nueva_cantidad else None

        actualizar_producto(inventario, nombre, nuevo_precio, nueva_cantidad)

    elif opcion == 5:
        nombre = input("Ingresa el nombre del producto que quieres eliminar: ").strip()
        eliminar_producto(inventario, nombre)

    elif opcion == 6:
        calcular_estadisticas(inventario)

    elif opcion == 7:
        guardar_csv(inventario, ruta_archivo)

    elif opcion == 8:
        datos,invalidas = cargar_csv(ruta_archivo) 

        if datos is not None:
            print(f"\nSe encontraron {len(datos)} productos validos y {invalidas} filas con errores")
            while True:
                decision = input("¿Qué deseas hacer? (S)obreescribir / (A)gregar / (C)ancelar: ").strip().upper()
                if decision == "S":
                    # Sobreescribir completamente el inventario
                    inventario.clear()
                    for i, p in enumerate(datos, 1):
                        p['id'] = i
                        inventario.append(p)
                    print(f"✅ Inventario sobrescrito exitosamente. {len(inventario)} productos importados.")
                    print("\n-----------------------------------\n")
                    break
                elif decision == "A":
                    # Agregar los productos cargados sin perder los existentes
                    max_id = max([p['id'] for p in inventario], default=0)
                    for i, p in enumerate(datos, max_id + 1):
                        p['id'] = i
                        inventario.append(p)
                    print(f"✅ {len(datos)} productos agregados al inventario existente.")
                    print("\n-----------------------------------\n")
                    break
                elif decision == "C":
                    # Cancelar la carga y mantener el inventario actual
                    print("Carga cancelada. El inventario actual se mantiene intacto.")
                    print("\n-----------------------------------\n")
                    break
                else:
                    print("Entrada inválida. Por favor, ingresa 'S', 'A' o 'C'.")

    elif opcion == 9:
        print("Saliendo...")
    else:
        print("Opción inválida.")


