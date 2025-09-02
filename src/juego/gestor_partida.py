import numpy
from enum import Enum
from.cacho import Cacho
from .dado import Dado, Pintas
from .arbitro_ronda import ArbitroRonda
from .contador_pintas import ContadorPintas
from .validador_apuesta import ValidadorApuesta

class Obligar(Enum):
    No = 0
    Abierta = 1
    Cerrada = 2

class GestorPartida:

    def __init__(self, arbitro, nombres, jugadores):
        self.arbitro = arbitro
        self.nombres = nombres
        self.jugadores = jugadores
        self.Contador = ContadorPintas(jugadores)
        self.Validador = ValidadorApuesta()
        self.rondaex = Obligar.No

    def IniciarPartida(self):
        D = Dado()
        DadosIniciales = numpy.zeros(len(self.jugadores))

        #Lanzar los dados para determinar que jugador iniciara la partida
        while True:
            for i in range (len(self.jugadores)):
                D.lanzar()
                x = D.GetDenominacion()
                DadosIniciales[i] = Pintas[x].value

            #Verifica que el numero mayor no se repita, si se repite el while continua
            numero_mayor = numpy.max(DadosIniciales)
            if numpy.sum(DadosIniciales == numero_mayor) == 1:
                break

        #Devuelve la posicion del arreglo que saco el numero mayor
        max_i = 0
        max_val = DadosIniciales[0]

        for i in range(len(DadosIniciales)):
            if DadosIniciales[i] > max_val:
                max_val = DadosIniciales[i]
                max_i = i

        return self.nombres[max_i]

    """def JugarRonda(self):

        if obligar(self.jugadores[i]):
            x
        else:

        self.jugadores =

        return self.jugadores"""

    #Un dado en juego (obligar)
    def obligar(self, jugador_con_un_dado, AC: Obligar):

        if sum(1 for elem in jugador_con_un_dado.GetDados if isinstance(elem, Dado)) == 1:
            self.rondaex = AC
            return True

        return False

    def FinalizarPartida(self):

        #Revisa el arreglo de jugadores, si solo queda 1 lo devuelve, si no devuelve 'Aun no hay ganador'
        if sum(1 for elem in self.jugadores if isinstance(elem, Cacho)) == 1:
            for i, elem in enumerate(self.jugadores):
                if isinstance(elem, Cacho):
                    return self.nombres[i]

        return 'Aun no hay ganador'