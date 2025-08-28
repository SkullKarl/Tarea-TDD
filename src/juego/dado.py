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

    def __init__(self):
        self.cara = 0
        self.pinta = 'P'
        self.lanzar()

    def lanzar(self):
        self.cara = random.randint(1, 6)
        self.pinta = Pintas(self.cara).name