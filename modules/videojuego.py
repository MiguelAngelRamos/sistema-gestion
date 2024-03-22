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
        return f"Desarrolladora: {self.desarrolladora}"

