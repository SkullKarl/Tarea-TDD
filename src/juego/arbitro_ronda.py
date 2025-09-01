from src.juego.dado import Dado
from src.juego.contador_pintas import ContadorPintas

class ArbitroRonda:
    def __init__(self, jugadores, cacho_jugadores):
        self.jugadores = jugadores
        self.cacho_jugadores = cacho_jugadores
        self.contador = ContadorPintas(cacho_jugadores)
        self.ronda_especial = False # Si es true los ases no serán comodines

    # ======================= Funciones auxiliares =======================
    def _mostrar_cachos(self):
        for cacho in self.cacho_jugadores:
            cacho.mostrar()

    def _ocultar_cachos(self):
        for cacho in self.cacho_jugadores:
            cacho.ocultar()

    # ========================== Función dudar ===========================
    def dudar(self, pinta_cantada, cantidad_cantada, jugador_apostador, jugador_dudor):
        self._mostrar_cachos()
        
        total_pintas = self.contador.contar_pintas(
            pinta_cantada,
            contar_ases_como_comodines=not self.ronda_especial
        )

        # Determinar ganador y perdedor
        if total_pintas >= cantidad_cantada:
            # El dudador se equivocó
            jugador_perdedor = jugador_dudor
            jugador_ganador = jugador_apostador
        else:
            # El que apostó mintió
            jugador_perdedor = jugador_apostador
            jugador_ganador = jugador_dudor

        self._ocultar_cachos()

        return jugador_ganador, jugador_perdedor, total_pintas
    
    # ========================== Función calzar ==========================
    def calzar(self, pinta_cantada, cantidad_cantada, jugador_calzador):
        # Si no se puede calzar en este turno, no altera nada
        # (evaluar proximamente si a gestor_partida le sirve una exception aquí)
        if self.puede_calzar(jugador_calzador, self.cacho_jugadores) == False:
            jugador_ganador = None
            jugador_perdedor = None
            total_pintas = 0

            return jugador_ganador, jugador_perdedor, total_pintas

        self._mostrar_cachos()

        total_pintas = self.contador.contar_pintas(
            pinta_cantada,
            contar_ases_como_comodines=not self.ronda_especial
        )

        # Si calza exactamente, gana el calzador
        if total_pintas == cantidad_cantada:
            jugador_ganador = jugador_calzador
            jugador_perdedor = None
        else:
            jugador_ganador = None
            jugador_perdedor = jugador_calzador

        self._ocultar_cachos()
        return jugador_ganador, jugador_perdedor, total_pintas
    
    # ================ Función de validación para calzar =================
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
    