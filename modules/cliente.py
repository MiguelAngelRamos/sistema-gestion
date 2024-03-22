class Cliente:
    def __init__(self, id_cliente, nombre, saldo, preferencia_videojuego=None):
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.saldo = saldo
        self.preferencia_videojuego = preferencia_videojuego

    def recargar_saldo(self, monto):
        self.saldo += monto
        return f"Saldo actualizado, Nuevo saldo: {self.saldo}"
