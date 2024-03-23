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
        return f"Nuevo precio del video juego : {self.precio}"

    def mostrar_info_desarrolladora(self):
        return f"Desarrolladora: {self.desarrolladora}, País: {self.desarrolladora.pais}"

dic_videojuegos = {}


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
