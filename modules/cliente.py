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
    cliente = Cliente(id_cliente, nombre, saldo, preferencia_videojuego)
    dic_cliente[id] = cliente
    print("Cliente registrado exitosamente")
