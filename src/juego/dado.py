import random
from enum import Enum

class Pintas(Enum):
    As = 1
    Tonto = 2
    Tren = 3
    Cuadra = 4
    Quina = 5
    Sexto = 6

class Dado:
    def __init__(self, cara:int = None):
        if(cara == None):
            self.cara = 1
            return
        self.cara = cara

    def lanzar(self):
        self.cara = random.randint(1, 6)
    
    def GetDenominacion(self):
        return Pintas(self.cara).name 
