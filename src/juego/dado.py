import random

class Dado:

    def __init__(self):
        self.lanzar()
        self.pintar()

    def lanzar(self):
        self.cara = random.randint(1, 6)

    def pintar(self):
        match self.cara:
            case 1:
                self.pinta = "As"
            case 2:
                self.pinta = "Tonto"
            case 3:
                self.pinta = "Tren"
            case 4:
                self.pinta = "Cuadra"
            case 5:
                self.pinta = "Quina"
            case 6:
                self.pinta = "Sexto"