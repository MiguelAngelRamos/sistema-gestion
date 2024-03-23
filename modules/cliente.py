from prettytable import PrettyTable


class Cliente:
    def __init__(self, id_cliente, nombre, saldo, preferencia_videojuego=None):
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.saldo = saldo
        self.preferencia_videojuego = preferencia_videojuego

    def recargar_saldo(self, monto):
        self.saldo += monto
        return f"Saldo actualizado, Nuevo saldo: {self.saldo}"


dic_cliente = {}


def registrar_cliente():
    print("\n Registrar un Nuevo Cliente")
    id_cliente = input("ID: ")
    nombre = input("Nombre: ")
    saldo = float(input("Saldo: "))
    preferencia_videojuego = input("Preferencia de video juego (opcional): ")

    try:
        cliente = Cliente(id_cliente, nombre, saldo, preferencia_videojuego)
        dic_cliente[id_cliente] = cliente
        print("Cliente registrado exitosamente")
        imprimir_clientes()
    except ValueError as error:
        print(f"Error al registrar el cliente: {error}")


def imprimir_clientes():
    tabla = PrettyTable()
    tabla.field_names = ["ID", "Nombre", "Saldo", "Preferencia Juego"]
    for obj_cliente in dic_cliente.values():
        tabla.add_row([obj_cliente.id_cliente, obj_cliente.nombre, obj_cliente.saldo, obj_cliente.preferencia_videojuego])
        print(tabla)

