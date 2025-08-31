from .dado import Dado

class Cacho:
    def __init__(self):
        self.__dado = [Dado() for _ in range(5)]
        pass

    def GetDados(self):
        return self.__dado