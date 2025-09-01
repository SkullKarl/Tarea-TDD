import numpy
from .dado import Dado, Pintas
from .contador_pintas import ContadorPintas
from .validador_apuesta import ValidadorApuesta

class GestorPartida:

    def __init__(self, arbitro, jugadores):
        self.arbitro = arbitro
        self.jugadores = jugadores
        self.Contador = ContadorPintas(jugadores)
        self.Validador = ValidadorApuesta()

    def IniciarPartida(self):
        D = Dado()
        DadosIniciales = numpy.zeros(len(self.jugadores))

        while True:
            for i in range (len(self.jugadores)):
                D.lanzar()
                x = D.GetDenominacion()
                DadosIniciales[i] = Pintas[x].value

            numero_mayor = numpy.max(DadosIniciales)
            if numpy.sum(DadosIniciales == numero_mayor) == 1:
                break

        max_i = 0
        max_val = DadosIniciales[0]

        for i in range(len(DadosIniciales)):
            if DadosIniciales[i] > max_val:
                max_val = DadosIniciales[i]
                max_i = i

        return max_i + 1

    """def JugarRonda(self):

        if obligar(self.jugadores[i]):
            x
        else:

        self.jugadores =

        return self.jugadores

    #Un dado en juego (obligar)
    def obligar(self, jugador_con_un_dado):

        if len(jugador_con_un_dado.GetDados) == 1:
            return True

        return False

    def FinalizarPartida(self):

        if X == 1:
            ganador =
            return ganador"""