from src.juego.contador_pintas import ContadorPintas
'''
Asume que gestor de partida manejará:
    juego = {
        "jugadores": {
            "J1": (Cacho) cacho1,
            "J2": (Cacho) cacho2,
            "J3": (Cacho) cacho3
        },
        "apuesta_actual": {
            "cantidad": 6,
            "pinta": 3
        },
        "turno_especial": False
    }
'''
class ArbitroRonda:
    def __init__(self, jugadores, cacho_jugadores):
        self.jugadores = jugadores
        self.cacho_jugadores = cacho_jugadores  # Lista de Cacho por jugador
        self.contador = ContadorPintas(cacho_jugadores)

    # necesita saber: qué jugador dudó, cual es la apuesta
    # deben mostrar todos sus juegos
    # debe llamar a manejar_dados
    def dudar(self, apuesta_actual, jugador_dudor):
        pinta_cantada = apuesta_actual["pinta"]
        cantidad_cantada = apuesta_actual["cantidad"]
        jugador_apostador = apuesta_actual["jugador"]

        for cacho in self.cacho_jugadores:
            cacho.mostrar()
        
        # Contar las pintas reales
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

        # Ocultar los dados para la siguiente ronda
        for cacho in self.cacho_jugadores:
            cacho.ocultar()

        return {
            "jugador_ganador": jugador_ganador,
            "jugador_perdedor": jugador_perdedor,
            "total_pintas": total_pintas
        }