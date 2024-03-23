from modules.cliente import registrar_cliente, recargar_saldo_cliente
from modules.desarrolladora import registrar_desarrolladora
from modules.videojuego import registrar_videojuego, actualizar_precio_videojuego
from modules.empleado import registrar_empleado, realizar_venta
def menu_principal():
    while True:
        print("\n Menu principal de la Tienda de VideoJuegos")
        print("1. Registrar Desarrolladora")
        print("2. Registrar VideoJuego")
        print("3. Registrar Empleado")
        print("4. Registrar Cliente")
        print("5. Realizar Venta")
        print("6. Actualizar Precio de un VideoJuego")
        print("7. Recargar Saldo del Cliente")
        print("8. Salir")

        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            registrar_desarrolladora()
        elif opcion == "2":
            registrar_videojuego()
        elif opcion == "3":
            registrar_empleado()
        elif opcion == "4":
            registrar_cliente()
        elif opcion == "5":
            realizar_venta()
        if opcion == "6":
            actualizar_precio_videojuego()
        if opcion == "7":
            recargar_saldo_cliente()
        if opcion == "8":
            print("Saliendo del Programa....")
            break
        else:
            print("Opción no válida, intente de nuevo")



if __name__ == '__main__':
    menu_principal()