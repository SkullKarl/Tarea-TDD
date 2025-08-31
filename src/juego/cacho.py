from .dado import Dado

class Cacho:
    def __init__(self):
        self.__visible = True
        self.__dado = [Dado() for _ in range(5)]
        pass

    def GetDados(self):
        if (self.__visible == False):
            return None
        return self.__dado

    def agitar(self):
        for dado in self.__dado:
            dado.lanzar()

    def ocultar(self):
        self.__visible = False
    
    def mostrar(self):
        self.__visible = True