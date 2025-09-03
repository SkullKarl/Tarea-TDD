import numpy
from enum import Enum
from .cacho import Cacho
from .dado import Dado, Pintas
from .arbitro_ronda import ArbitroRonda
from .contador_pintas import ContadorPintas
from .validador_apuesta import ValidadorApuesta

class ObligarOpciones(Enum):
    No = 0
    Abierta = 1
    Cerrada = 2

class GestorPartida:

    def __init__(self, nombres, jugadores):
        self.nombres = nombres
        self.jugadores = jugadores
        self.Arbitro = ArbitroRonda(nombres, jugadores)
        self.Contador = ContadorPintas(jugadores)
        self.Validador = ValidadorApuesta()
        self.DadosAFavor = numpy.zeros(len(self.jugadores))
        self.rondaex = ObligarOpciones.No
        self.NoObligar = numpy.ones(len(self.jugadores))

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

        for i in range (len(DadosIniciales)):
            if DadosIniciales[i] > max_val:
                max_val = DadosIniciales[i]
                max_i = i

        return self.nombres[max_i]

    def JugarRonda(self, pinta_cantada, cantidad_cantada, jugador_apostador, dudo=False, jugador_dudor='No', calzar=False):

        for i in range (len(self.jugadores)):
            if isinstance(self.jugadores[i], Cacho):
                self.jugadores[i].agitar()

        if self.rondaex != ObligarOpciones.No:
            self.Arbitro.ronda_especial = True

            if self.rondaex == ObligarOpciones.Abierta:
                for i in range (len(self.jugadores)):
                    if isinstance(self.jugadores[i], Cacho):
                        self.jugadores[i].mostrar()
            elif self.rondaex == ObligarOpciones.Cerrada:
                for i in range (len(self.jugadores)):
                    if isinstance(self.jugadores[i], Cacho):
                        self.jugadores[i].ocultar()

        p_c = pinta_cantada
        c_c = cantidad_cantada
        j_a = jugador_apostador
        j_d = jugador_dudor

        if dudo:
            ganador, perdedor, pintas = self.Arbitro.dudar(p_c, c_c, j_a, j_d)
            indexperdedor = self.nombres.index(perdedor)
            self.jugadores[indexperdedor].quitar_dado()

        if calzar:
            if self.Arbitro.puede_calzar(j_d):
                ganador, perdedor, pintas = self.Arbitro.calzar(p_c, c_c, j_d)
                indexganador = self.nombres.index(ganador)

                if len(self.jugadores[indexganador].GetDados()) == 5:
                    self.DadosAFavor[indexganador] = self.DadosAFavor[indexganador] + 1
                else:
                    self.jugadores[indexganador].agregar_dado()

                indexperdedor = self.nombres.index(perdedor)
                self.jugadores[indexperdedor].quitar_dado()

        for i in range (len(self.jugadores)):
            if self.jugadores[i] is None:
                continue

            if not any(isinstance(dado, Dado) for dado in self.jugadores[i].GetDados()):
                self.jugadores[i] = None

        if self.rondaex != ObligarOpciones.No:
            self.rondaex = ObligarOpciones.No
            self.Arbitro.ronda_especial = False

        return self.jugadores

    #Un dado en juego (obligar)
    def obligar(self, i_jugador_con_un_dado, jugador_con_un_dado, AC: ObligarOpciones):

        #Un jugador solo puede obligar una vez por partida
        if self.NoObligar[i_jugador_con_un_dado] == 0:
            return False

        if AC == ObligarOpciones.No:
            return False

        if sum(1 for elem in jugador_con_un_dado.GetDados() if isinstance(elem, Dado)) == 1:
            self.rondaex = AC
            self.NoObligar[i_jugador_con_un_dado] = 0
            return True

        return False

    def FinalizarPartida(self):

        #Revisa el arreglo de jugadores, si solo queda 1 lo devuelve, si no devuelve 'Aun no hay ganador'
        if sum(1 for elem in self.jugadores if isinstance(elem, Cacho)) == 1:
            for i, elem in enumerate(self.jugadores):
                if isinstance(elem, Cacho):
                    return self.nombres[i]

        return 'Aun no hay ganador'