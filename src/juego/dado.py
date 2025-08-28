import random

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