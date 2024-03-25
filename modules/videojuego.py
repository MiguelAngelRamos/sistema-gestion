#modules/videojuego.py
from prettytable import PrettyTable
from .desarrolladora import dic_desarrolladoras


class Videojuego:
    def __init__(self, codigo, titulo, precio, stock, desarrolladora, genero=None):
        self.codigo = codigo
        self.titulo = titulo
        self.precio = precio
        self.stock = stock
        self.desarrolladora = desarrolladora
        self.genero = genero

    def actualizar_precio(self, porcentaje):
        self.precio *= (1 + porcentaje/100)
        """
          self.precio *= (1 + porcentaje/100): Aquí, el precio actual del videojuego se multiplica por (1 + porcentaje/100). 
          Esto significa que el precio del videojuego se incrementará en el porcentaje proporcionado. Por ejemplo, 
          si el precio actual es 100 y el porcentaje proporcionado es 20, entonces el precio se incrementará en un 20%, 
          lo que resultará en un nuevo precio de 120.
          """
        return f"Nuevo precio del video juego : {self.precio}"


    def mostrar_info_desarrolladora(self):
        return f"Desarrolladora: {self.desarrolladora}, País: {self.desarrolladora.pais}"

dic_videojuegos = {}

# Creando instancias de la clase Videojuego
videojuego1 = Videojuego("V001", "Super Mario", 60, 100, dic_desarrolladoras.get("D001"), "Plataformas")
videojuego2 = Videojuego("V002", "Zelda: Breath of the Wild", 70, 50, dic_desarrolladoras.get("D002"), "Aventura")
videojuego3 = Videojuego("V003", "Minecraft", 30, 200, dic_desarrolladoras.get("D003"), "Sandbox")
videojuego4 = Videojuego("V004", "FIFA 22", 60, 150, dic_desarrolladoras.get("D001"), "Deportes")
videojuego5 = Videojuego("V005", "Call of Duty: Warzone", 0, 500, dic_desarrolladoras.get("D002"), "Shooter")

# Añadiendo los videojuegos al diccionario
dic_videojuegos[videojuego1.codigo] = videojuego1
dic_videojuegos[videojuego2.codigo] = videojuego2
dic_videojuegos[videojuego3.codigo] = videojuego3
dic_videojuegos[videojuego4.codigo] = videojuego4
dic_videojuegos[videojuego5.codigo] = videojuego5

def registrar_videojuego():
    print("\n Registrar video juegos")
    codigo = input("Código:")
    titulo = input("Titulo:")
    precio = input("Precio:")
    stock = input("Stock:")
    RUT_desarrolladora = input("RUT de la desarrolladora")
    genero = input("Genero (opcional)")
    desarrolladora = dic_desarrolladoras.get(RUT_desarrolladora)

    if desarrolladora:
        videojuego = Videojuego(codigo, titulo, precio, stock, desarrolladora, genero)
        dic_videojuegos[codigo] = videojuego
        print("Videojuego registrado exitosamente. ")
    else:
        print("Desarrolladora no encontrada. ")

def actualizar_precio_videojuego():
    print("\nActualizar Precio de Videojuego")
    codigo = input("Codigo del video juego")
    porcentaje = float(input("Porcentaje de aumento (ejemplo: para aumentar un 10%, escribe 10)"))
    videojuego = dic_videojuegos.get(codigo)

def imprimir_videojuegos():
    tabla = PrettyTable()
    tabla.field_names = ["Código", "Título", "Precio", "Stock", "Desarrolladora", "Género"]
    for obj_videojuego in dic_videojuegos.values():
        tabla.add_row([obj_videojuego.codigo, obj_videojuego.titulo, obj_videojuego.precio, obj_videojuego.stock, obj_videojuego.desarrolladora.nombre, obj_videojuego.genero])
    print(tabla)
