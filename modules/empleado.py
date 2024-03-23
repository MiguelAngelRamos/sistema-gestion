from prettytable import PrettyTable
from .videojuego import dic_videojuegos
from .cliente import dic_clientes
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

dic_empleados = {}
# Creando instancias de la clase Empleado
empleado1 = Empleado("E001", "Juan Pérez", 0.05)
empleado2 = Empleado("E002", "María López", 0.05)
empleado3 = Empleado("E003", "Carlos Gómez", 0.04)
empleado4 = Empleado("E004", "Ana Ruiz", 0.03)
empleado5 = Empleado("E005", "Luis Fernández", 0.02)

# Añadiendo los empleados al diccionario
dic_empleados[empleado1.id_empleado] = empleado1
dic_empleados[empleado2.id_empleado] = empleado2
dic_empleados[empleado3.id_empleado] = empleado3
dic_empleados[empleado4.id_empleado] = empleado4
dic_empleados[empleado5.id_empleado] = empleado5

def registrar_empleado():
    print("\n Registrar un Nuevo empleado")
    id_empleado = input("ID: ")
    nombre = input("Nombre: ")
    comision = float(input("Ingrese Comisión (opcional, dejar en blanco si no hay: ) ") or 0 )

    try:
        empleado = Empleado(id_empleado, nombre, comision)
        dic_empleados[id_empleado] = empleado
        print("empleado registrado exitosamente")
        imprimir_empleado()
    except ValueError as error:
        print(f"Error al registrar el cliente: {error}")


def imprimir_empleado():
    tabla = PrettyTable()
    tabla.field_names = ["ID", "Nombre", "Comision"]
    for obj_empleado in dic_empleados.values():
        tabla.add_row([obj_empleado.id_empleado, obj_empleado.nombre, obj_empleado.comision])
        print(tabla)


def realizar_venta():
    print("\nRealizar Venta")
    id_empleado = input("ID del Empleado: ")
    id_cliente = input("ID del Cliente: ")
    codigo_videojuego = input("Código del Videojuego: ")

    empleado = dic_empleados.get(id_empleado)
    cliente = dic_clientes.get(id_cliente)
    videojuego = dic_videojuegos.get(codigo_videojuego)

    if not empleado:
        print("Empleado no encontrado.")
        return
    if not cliente:
        print("Cliente no encontrado.")
        return
    if not videojuego:
        print("Videojuego no encontrado.")
        return

    resultado_venta = empleado.vender(videojuego, cliente)
    print(resultado_venta)






