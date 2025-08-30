import random

class ContadorPintas:
    def __init__(self, cacho_jugadores):
        # cacho_jugadores: lista de listas (pronto con objetos Cacho) con los dados por jugador
        self.cacho_jugadores = cacho_jugadores

    def contar_pintas(self, pinta_cantada, ases_comodines=True):
        total = 0

        for cacho in self.cacho_jugadores:
            for dado in cacho.obtener_dados():
                # Caso 1, pinta_cantada es 1
                if pinta_cantada == 1:
                    if dado == 1:
                        total += 1
                # Caso 2, ronda obligada por lo que los ases no cuentan como comodines
                elif not ases_comodines:
                    if dado == pinta_cantada:
                        total += 1
                # Caso estándar
                else:
                    if dado == pinta_cantada or dado == 1:
                        total += 1
        return total


