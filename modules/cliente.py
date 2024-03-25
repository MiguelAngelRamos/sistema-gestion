# modules/cliente.py
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


dic_clientes = {}
# Creando instancias de la clase Cliente
cliente1 = Cliente("C001", "Roberto Álvarez", 500.0, "RPG")
cliente2 = Cliente("C002", "Sofía Martín", 750.0, "Aventura")
cliente3 = Cliente("C003", "Miguel Torres", 200.0, "Estrategia")
cliente4 = Cliente("C004", "Laura Jiménez", 650.0, "Acción")
cliente5 = Cliente("C005", "Antonio García", 300.0, "Deportes")

# Añadiendo los clientes al diccionario
dic_clientes[cliente1.id_cliente] = cliente1
dic_clientes[cliente2.id_cliente] = cliente2
dic_clientes[cliente3.id_cliente] = cliente3
dic_clientes[cliente4.id_cliente] = cliente4
dic_clientes[cliente5.id_cliente] = cliente5



def registrar_cliente():
    print("\n Registrar un Nuevo Cliente")
    id_cliente = input("ID: ")
    nombre = input("Nombre: ")
    saldo = float(input("Saldo: "))
    preferencia_videojuego = input("Preferencia de video juego (opcional): ")

    try:
        cliente = Cliente(id_cliente, nombre, saldo, preferencia_videojuego)
        dic_clientes[id_cliente] = cliente
        print("Cliente registrado exitosamente")
        imprimir_clientes()
    except ValueError as error:
        print(f"Error al registrar el cliente: {error}")


def imprimir_clientes():
    tabla = PrettyTable()
    tabla.field_names = ["Id", "Nombre", "Saldo", "Preferencia Juego"]
    for obj_cliente in dic_clientes.values():
        tabla.add_row([obj_cliente.id_cliente, obj_cliente.nombre, obj_cliente.saldo, obj_cliente.preferencia_videojuego])
    print(tabla)


def recargar_saldo_cliente():
    print("\nRecargar Saldo de Cliente")
    id_cliente = input("ID del Cliente: ")
    monto = float(input("Monto a recargar: "))

    cliente = dic_clientes.get(id_cliente)
    if cliente:
        resultado_recarga = cliente.recargar_saldo(monto)
        print(resultado_recarga)
    else:
        print("Cliente no encontrado.")