class Libro:
    def __init__(self, titulo, autor, genero):
        self.__titulo = titulo
        self.__autor = autor
        self.__genero = genero

    @property
    def get_titulo(self):
        return self.__titulo

    def set_titulo(self, titulo):
        self.__titulo = titulo
    @property
    def get_autor(self):
        return self.__autor

    def set_autor(self, autor):
        self.__autor = autor

    @property
    def get_genero(self):
        return self.__genero

    def set_genero(self, genero):
        self.__genero = genero