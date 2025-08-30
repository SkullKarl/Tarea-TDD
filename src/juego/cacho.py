import random
from .dado import Dado

class Cacho:
    def __init__(self):
        self.__visible = True
        self.dados = [Dado() for _ in range(5)]
        return

    def agitar(self):
        for dado in self.dados:
            dado.lanzar()
        return
    
    def ocultar(self):
        self.__visible = False
        return
    
    def mostrar(self):
        self.__visible = True
        return
    
    def __str__(self):
        if self.__visible:
            return ' '.join([d.GetDenominacion() for d in self.dados])
        else:
            return "Ocultos"