from prettytable import PrettyTable
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

dic_empleado = {}

def registrar_empleado():
    print("\n Registrar un Nuevo empleado")
    id_empleado = input("ID: ")
    nombre = input("Nombre: ")
    comision = float(input("Ingrese Comisión (opcional, dejar en blanco si no hay: ) ") or 0 )



    try:
        empleado = Empleado(id, nombre, comision)
        dic_empleado[id_empleado] = empleado
        print("empleado registrado exitosamente")
        imprimir_empleado()
    except ValueError as error:
        print(f"Error al registrar el cliente: {error}")


def imprimir_empleado():
    tabla = PrettyTable()
    tabla.field_names = ["ID", "Nombre", "Comision"]
    for obj_empleado in dic_empleado.values():
        tabla.add_row([obj_empleado.id_empleado, obj_empleado.nombre, obj_empleado.comision])
        print(tabla)






