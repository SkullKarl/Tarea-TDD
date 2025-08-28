import random

class Dado:

    def __init__(self):
        self.lanzar()
        self.pintar()

    def lanzar(self):
        self.cara = random.randint(1, 6)

    def pintar(self):
        return

