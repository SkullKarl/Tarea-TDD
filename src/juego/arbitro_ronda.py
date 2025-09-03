from src.juego.dado import Dado
from src.juego.contador_pintas import ContadorPintas
from src.juego.cacho import Cacho

class ArbitroRonda:
    def __init__(self, jugadores : list[str], cacho_jugadores : list[Cacho]):
        self.jugadores = jugadores
        self.cacho_jugadores = cacho_jugadores
        self.contador = ContadorPintas(cacho_jugadores)
        self.ronda_especial = False # Si es true los ases no serán comodines

    # ============================= Funciones auxiliares =============================
    def _mostrar_cachos(self):
        for cacho in self.cacho_jugadores:
            cacho.mostrar()

    def _ocultar_cachos(self):
        for cacho in self.cacho_jugadores:
            cacho.ocultar()

    def _contar_pintas(self, pinta_cantada : int) -> int:
        return self.contador.contar_pintas(
            pinta_cantada,
            ases_comodines=not self.ronda_especial
        )

    # ================================ Función dudar =================================
    def dudar(self, pinta_cantada : int,
                cantidad_cantada : int,
                jugador_apostador : str,
                jugador_dudor : str) -> tuple[str | None, str | None, int]:
        
        self._mostrar_cachos()
        total_pintas = self._contar_pintas(pinta_cantada)

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
    
    # ================================ Función calzar ================================
    def calzar(self, pinta_cantada : int,
                cantidad_cantada : int,
                jugador_calzador : str) -> tuple[str | None, str | None, int]:
        
        # Si no se puede calzar en este turno, no altera nada
        if self.puede_calzar(jugador_calzador) == False:
            jugador_ganador = None
            jugador_perdedor = None
            total_pintas = 0

            return jugador_ganador, jugador_perdedor, total_pintas

        self._mostrar_cachos()

        total_pintas = self._contar_pintas(pinta_cantada)

        # Si calza exactamente, gana el calzador
        if total_pintas == cantidad_cantada:
            jugador_ganador = jugador_calzador
            jugador_perdedor = None
        else:
            jugador_ganador = None
            jugador_perdedor = jugador_calzador

        self._ocultar_cachos()

        return jugador_ganador, jugador_perdedor, total_pintas
    
    # ====================== Función de validación para calzar =======================
    def puede_calzar(self, jugador_calzador : str) -> bool:
        total_dados = sum(len(cacho.GetDados()) for cacho in self.cacho_jugadores)
        dados_iniciales = len(self.cacho_jugadores) * 5

        # Caso 1: mitad o mayor que dados iniciales
        if total_dados >= dados_iniciales / 2:
            return True

        # Caso 2: jugador calzó con un solo dado
        idx = self.jugadores.index(jugador_calzador)
        if len(self.cacho_jugadores[idx].GetDados()) == 1:
            return True

        # Caso 3: no cumplimos condiciones para calzar
        return False
    