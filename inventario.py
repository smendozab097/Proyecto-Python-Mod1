from funciones import *


option="0"
while option!="7":

    menu()

    option = int(input("Ingresa el numero de la accion que deseas realizar: ").strip()) #Elimina los espacios en blanco al inicio y al final de la entrada del usuario

    if option == 1:
        agregar_producto()

    elif option == 2:
        mostrar_productos()

    elif option == 3:
        buscar_producto()

    elif option == 4:
        actualizar_producto()

    elif option == 7:
        print("Programa finalizado")
        break

