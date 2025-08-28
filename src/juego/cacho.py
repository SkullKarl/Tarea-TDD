import random
from .dado import Dado

class Cacho:
    def __init__(self):
        self.dados = [Dado() for _ in range(5)]
        return

    def agitar(self):
        for dado in self.dados:
            dado.lanzar()
        return