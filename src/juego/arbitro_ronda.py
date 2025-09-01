from src.juego.dado import Dado
from src.juego.contador_pintas import ContadorPintas

class ArbitroRonda:
    def __init__(self, jugadores, cacho_jugadores):
        self.jugadores = jugadores
        self.cacho_jugadores = cacho_jugadores
        self.contador = ContadorPintas(cacho_jugadores)

    def dudar(self, apuesta_actual, jugador_dudor):
        pinta_cantada = apuesta_actual["pinta"]
        cantidad_cantada = apuesta_actual["cantidad"]
        jugador_apostador = apuesta_actual["jugador"]

        for cacho in self.cacho_jugadores:
            cacho.mostrar()
        
        total_pintas = self.contador.contar_pintas(pinta_cantada)

        # Determinar ganador y perdedor
        if total_pintas >= cantidad_cantada:
            # El dudador se equivocó
            jugador_perdedor = jugador_dudor
            jugador_ganador = jugador_apostador
        else:
            # El que apostó mintió
            jugador_perdedor = jugador_apostador
            jugador_ganador = jugador_dudor

        for cacho in self.cacho_jugadores:
            cacho.ocultar()

        return {
            "jugador_ganador": jugador_ganador,
            "jugador_perdedor": jugador_perdedor,
            "total_pintas": total_pintas
        }
    
    def calzar(self, apuesta_actual, jugador_calzador):
        if self.puede_calzar(jugador_calzador, self.cacho_jugadores) == False:
            return {
                "jugador_ganador": None,
                "jugador_perdedor": None,
                "total_pintas": 0
            }
        
        pinta_cantada = apuesta_actual["pinta"]
        cantidad_cantada = apuesta_actual["cantidad"]

        for cacho in self.cacho_jugadores:
            cacho.mostrar()

        total_pintas = self.contador.contar_pintas(pinta_cantada)

        # Si calza exactamente, gana el calzador
        if total_pintas == cantidad_cantada:
            jugador_ganador = jugador_calzador
            jugador_perdedor = None
        else:
            jugador_ganador = None
            jugador_perdedor = jugador_calzador

        for cacho in self.cacho_jugadores:
            cacho.ocultar()

        return {
            "jugador_ganador": jugador_ganador,
            "jugador_perdedor": jugador_perdedor,
            "total_pintas": total_pintas
        }
    
    def puede_calzar(self, jugador_calzador, cacho_jugadores):
        total_dados = sum(len(cacho.obtener_dados()) for cacho in cacho_jugadores)
        dados_iniciales = len(cacho_jugadores) * 5

        # Caso 1: mitad o mayor que dados iniciales
        if total_dados >= dados_iniciales / 2:
            return True

        # Caso 2: jugador calzó con un solo dado
        idx = self.jugadores.index(jugador_calzador)
        if len(cacho_jugadores[idx].obtener_dados()) == 1:
            return True

        # Caso 3: no cumplimos condiciones para calzar
        return False
    