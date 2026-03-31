from funciones import *

# Programa principal
inventario = []
opcion = 0
while opcion != 9:
    menu()
    opcion = int(input("\nIngresa el numero de la accion que deseas realizar: ").strip())
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

            
        nueva_cantidad = input("Ingresa la nueva cantidad del producto o deja en blanco para mantener: ").strip()


        actualizar_producto(inventario, nombre, nuevo_precio, nueva_cantidad)

    elif opcion == 5:
        nombre = input("Ingresa el nombre del producto que quieres eliminar: ").strip()
        eliminar_producto(inventario, nombre)

    elif opcion == 6:
        calcular_estadisticas(inventario)

    elif opcion == 9:
        print("Saliendo...")
    else:
        print("Opción inválida.")


