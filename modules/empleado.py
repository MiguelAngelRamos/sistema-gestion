class Empleado:
    def __init__(self, id_empleado, nombre, comision=0):
        self.id_empleado = id_empleado
        self.nombre = nombre
        self.comision = comision

    def vender(self, videojuego, cliente):
        if cliente.saldo < videojuego.precio:
            return "Venta no realiza: saldo insuficiente"
        if videojuego.stock <= 0:
            return "Venta no realiza: stock insuficiente"
        videojuego.stock -= 1
        # 1000 * 0.05 = 50
        self.comision += videojuego.precio * 0.05
        cliente.saldo -= videojuego.precio
        return f"Venta realizada. Comisión del empleado actualizada : {self.comision}. Saldo del Cliente: {cliente.saldo}."







