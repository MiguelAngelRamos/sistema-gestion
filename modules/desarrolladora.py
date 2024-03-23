from prettytable import PrettyTable
class Desarrolladora:
    def __init__(self, RUT, nombre, direccion, pais, es_persona_juridica):
        self.RUT = RUT
        self.nombre = nombre
        self.direccion = direccion
        self.pais = pais
        self.es_persona_juridica = es_persona_juridica

# Este diccionario va a tener llaves y dentro de llaves instancias de la clase
dic_desarrolladoras = {}
# Creando instancias de la clase Desarrolladora
desarrolladora1 = Desarrolladora("D001", "SuperGames", "Calle 123, Ciudad Juego", "España", True)
desarrolladora2 = Desarrolladora("D002", "PixelArt Studios", "Avenida 456, PixelCity", "Japón", True)
desarrolladora3 = Desarrolladora("D003", "Indie Devs", "Camino 789, IndieLand", "Canadá", False)

# Añadiendo las desarrolladoras al diccionario
dic_desarrolladoras[desarrolladora1.RUT] = desarrolladora1
dic_desarrolladoras[desarrolladora2.RUT] = desarrolladora2
dic_desarrolladoras[desarrolladora3.RUT] = desarrolladora3


def registrar_desarrolladora():
    imprimir_desarrolladoras()
    print("\nRegistrar Nueva Desarrolladora")
    RUT = input("RUT: ")
    nombre = input("Nombre: ")
    direccion = input("Dirección: ")
    pais = input("País: ")
    es_persona_juridica = input("Es persona jurídica (s/n): ").lower() == 's'
    desarrolladora = Desarrolladora(RUT, nombre, direccion, pais, es_persona_juridica)
    dic_desarrolladoras[RUT] = desarrolladora
    print("Desarrolladora registrada exitosamente.")

def imprimir_desarrolladoras():
    tabla = PrettyTable()
    tabla.field_names = ["RUT", "Nombre", "Direccion", "Pais", "Per. Juridica "]
    for obj_desarrolladora in dic_desarrolladoras.values():
        tabla.add_row([obj_desarrolladora.RUT, obj_desarrolladora.nombre, obj_desarrolladora.direccion, obj_desarrolladora.pais, obj_desarrolladora.es_persona_juridica])
        print(tabla)