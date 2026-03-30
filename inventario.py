from funciones import *

# Programa principal
inventario = []
opcion = "0"
while opcion != "4":
    mostrar_menu()
    opcion = input("Ingresa el numero de la accion que deseas realizar: ").strip()
    if opcion == "1":
        agregar_producto(inventario)
    elif opcion == "2":
        mostrar_inventario(inventario)
    elif opcion == "3":
        calcular_estadisticas(inventario)
    elif opcion == "4":
        print("Saliendo...")
    else:
        print("Opción inválida.")


