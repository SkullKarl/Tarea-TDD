from .dado import Dado

class Cacho:
    def __init__(self):
        self.__visible = True
        self.__dado = [Dado() for _ in range(5)]
        pass

    def GetDados(self):
        return self.__dado

    def agitar(self):
        for dado in self.__dado:
            dado.lanzar()

    def ocultar(self):
        self.__visible = False
    
    def mostrar(self):
        self.__visible = True
    
    def agregar_dado(self):
        self.__dado.append(Dado())

    def quitar_dado(self):
        if(len(self.__dado) > 0):
            self.__dado.pop()