from src.juego.contador_pintas import ContadorPintas

'''
cacho = Cacho()
cacho.agitar()
valores = [dado.cara for dado in cacho.GetDados()]
print(valores)

cacho._Cacho__dado = cacho._Cacho__dado[:4]
cacho.agitar()
print([dado.cara for dado in cacho.GetDados()])
'''

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
            

    def calzar_validacion(self):
        pass
    