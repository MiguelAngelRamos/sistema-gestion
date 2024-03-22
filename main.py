from modules.cliente import registrar_cliente

def menu_principal():
    while True:
        print("\n Menu principal de la Tienda de VideoJuegos")
        print("1. Registrar Desarrolladora")
        print("2. Registrar VideoJuego")
        print("3. Registrar Empleado")
        print("4. Registrar Cliente")
        print("5. Registrar Venta")
        print("6. Actualizar Precio de un VideoJuego")
        print("7. Recargar Saldo del Cliente")
        print("8. Salir")

        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            pass
        elif opcion == "2":
            pass
        elif opcion == "3":
            pass
        elif opcion == "4":
            registrar_cliente()
        elif opcion == "5":
            pass
        if opcion == "6":
            pass
        if opcion == "7":
            pass
        if opcion == "8":
            print("Saliendo del Programa....")
            break
        else:
            print("Opción no válida, intente de nuevo")



if __name__ == '__main__':
    menu_principal()