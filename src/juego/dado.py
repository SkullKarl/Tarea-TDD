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
        denominaciones = {
            1: "As",
            2: "Tonto",
            3: "Tren",
            4: "Cuadra",
            5: "Quina",
            6: "Sexto"
        }
        return denominaciones.get(self.cara, "Desconocido")
