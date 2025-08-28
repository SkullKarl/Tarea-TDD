import random

class Dado:

    def __init__(self):
        self.cara = 1

    def lanzar(self):
        self.cara = random.randint(1, 6)