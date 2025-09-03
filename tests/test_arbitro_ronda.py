import pytest
from src.juego.arbitro_ronda import ArbitroRonda
from src.juego.validador_apuesta import ValidadorApuesta

@pytest.fixture
def arbitro(mocker):
    # Hacemos los mocks para los cachos
    cacho1 = mocker.Mock()
    cacho2 = mocker.Mock()
    cacho3 = mocker.Mock()
    cacho_jugadores = [cacho1, cacho2, cacho3]

    # Mockeamos ContadorPintas
    mock_contador_class = mocker.patch("src.juego.arbitro_ronda.ContadorPintas")
    mock_contador = mock_contador_class.return_value

    # Creamos el árbitro y devolvemos también el mock del contador, para alterarlos en cada test
    arbitro = ArbitroRonda(jugadores=["J1", "J2", "J3"], cacho_jugadores=cacho_jugadores)
    arbitro._mock_contador = mock_contador
    return arbitro

# =========================================== Tests dudar ===========================================
def test_dudar_pierde_jugador_dudor(arbitro):
    """
    Si la cantidad real de la pinta apostada es mayor o igual a la apuesta,
    pierde el jugador que duda
    """
    arbitro._mock_contador.contar_pintas.return_value = 7 # Hay 7 trenes reales, contando comodines
    # Datos de la apuesta actual: J1 apostó 6 trenes
    pinta_cantada = 3
    cantidad_cantada = 6
    jugador_apostador = "J1"
    jugador_dudor = "J2" # jugador que dudó de esa apuesta

    jugador_ganador, jugador_perdedor, total_pintas = arbitro.dudar(
        pinta_cantada=pinta_cantada,
        cantidad_cantada=cantidad_cantada,
        jugador_apostador=jugador_apostador,
        jugador_dudor=jugador_dudor
    )

    # luego, asumimos que la función dudar de arbitro_ronda retornará un diccionario con
    # quién gana, quien pierde y la cantidad real
    assert jugador_ganador == jugador_apostador
    assert jugador_perdedor == jugador_dudor
    assert total_pintas == 7


def test_dudar_pierde_jugador_apostador(arbitro):
    """
    Si la cantidad real de la pinta apostada es menor a la apuesta,
    pierde el jugador que apostó
    """
    arbitro._mock_contador.contar_pintas.return_value = 5 # Hay 5 trenes reales, contando comodines
    # Datos de la apuesta actual: J1 apostó 6 trenes
    pinta_cantada = 3
    cantidad_cantada = 6
    jugador_apostador = "J1"
    jugador_dudor = "J2" # jugador que dudó de esa apuesta

    jugador_ganador, jugador_perdedor, total_pintas = arbitro.dudar(
        pinta_cantada=pinta_cantada,
        cantidad_cantada=cantidad_cantada,
        jugador_apostador=jugador_apostador,
        jugador_dudor=jugador_dudor
    )

    assert jugador_ganador == jugador_dudor
    assert jugador_perdedor == jugador_apostador
    assert total_pintas == 5

# =========================================== Tests calzar ===========================================

def test_calzar_exito(arbitro):
    arbitro._mock_contador.contar_pintas.return_value = 6
    # Datos de la apuesta actual: jugador previo apostó 6 trenes
    pinta_cantada = 3
    cantidad_cantada = 6
    jugador_calzador = "J2" # J2 intenta calzar

    cacho1 = arbitro.cacho_jugadores[0]
    cacho2 = arbitro.cacho_jugadores[1]
    cacho3 = arbitro.cacho_jugadores[2]

    cacho1.GetDados.return_value = [1, 2, 1, 2]
    cacho2.GetDados.return_value = [3, 4]
    cacho3.GetDados.return_value = [5, 6]

    jugador_ganador, jugador_perdedor, total_pintas = arbitro.calzar(
        pinta_cantada=pinta_cantada,
        cantidad_cantada=cantidad_cantada,
        jugador_calzador=jugador_calzador
    )
    
    assert jugador_ganador == jugador_calzador
    assert jugador_perdedor == None
    assert total_pintas == 6


def test_calzar_fracaso(arbitro):
    arbitro._mock_contador.contar_pintas.return_value = 4
    # Datos de la apuesta actual: jugador previo apostó 5 trenes
    pinta_cantada = 3
    cantidad_cantada = 5
    jugador_calzador = "J2" # J2 intenta calzar

    cacho1 = arbitro.cacho_jugadores[0]
    cacho2 = arbitro.cacho_jugadores[1]
    cacho3 = arbitro.cacho_jugadores[2]

    cacho1.GetDados.return_value = [1, 2, 1, 2]
    cacho2.GetDados.return_value = [3, 4]
    cacho3.GetDados.return_value = [5, 6]

    jugador_ganador, jugador_perdedor, total_pintas = arbitro.calzar(
        pinta_cantada=pinta_cantada,
        cantidad_cantada=cantidad_cantada,
        jugador_calzador=jugador_calzador
    )

    assert jugador_ganador == None
    assert jugador_perdedor == jugador_calzador
    assert total_pintas == 4

def test_calzar_llama_puede_calzar(arbitro, mocker):
    spy = mocker.spy(arbitro, "puede_calzar")
    # Datos de la apuesta actual: el jugador previo apostó 2 trenes
    pinta_cantada = 3
    cantidad_cantada = 2
    jugador_calzador = "J2" # J2 intenta calzar

    cacho1 = arbitro.cacho_jugadores[0]
    cacho2 = arbitro.cacho_jugadores[1]
    cacho3 = arbitro.cacho_jugadores[2]

    cacho1.GetDados.return_value = [1, 2, 1, 2]
    cacho2.GetDados.return_value = [3, 4]
    cacho3.GetDados.return_value = [5, 6]

    # Verificamos que puede_calzar sea llamada una vez
    arbitro.calzar(
        pinta_cantada=pinta_cantada,
        cantidad_cantada=cantidad_cantada,
        jugador_calzador=jugador_calzador
    )
    assert spy.call_count == 1


def test_calzar_apuesta_invalida(arbitro):
    cacho1 = arbitro.cacho_jugadores[0]
    cacho2 = arbitro.cacho_jugadores[1]
    cacho3 = arbitro.cacho_jugadores[2]

    cacho1.GetDados.return_value = [1, 2]
    cacho2.GetDados.return_value = [3, 4]
    cacho3.GetDados.return_value = [5, 6]

    # Llama a calzar con una apuesta cualquiera, no importa el valor porque no se puede calzar
    resultado = arbitro.calzar(
        pinta_cantada=3,
        cantidad_cantada=5,
        jugador_calzador="J1"
    )

    # Debe retornar (None, None, 0) porque no se puede calzar
    assert resultado == (None, None, 0)

# =========================================== Tests de puede_calzar ===========================================

def test_puede_calzar_cumple_condicion_mitad(arbitro):
    """
    Se puede calzar solo si la cantidad total de dados en juego es
    menor o igual a la mitad de los dados iniciales o cuando el jugador
    que calza le queda solo un dado
    """
    cacho1 = arbitro.cacho_jugadores[0]
    cacho2 = arbitro.cacho_jugadores[1]
    cacho3 = arbitro.cacho_jugadores[2]

    cacho1.GetDados.return_value = [1, 2, 1, 2]
    cacho2.GetDados.return_value = [3, 4]
    cacho3.GetDados.return_value = [5, 6]

    # 3 jugadores * 5 dados = 15 dados iniciales
    # Mitad de dados iniciales = 7.5 ~ 7
    # Dados en juego: 8 (cumple condición para calzar)
    assert arbitro.puede_calzar(jugador_calzador="J1") == True

def test_puede_calzar_no_cumple_condicion_mitad(arbitro):
    cacho1 = arbitro.cacho_jugadores[0]
    cacho2 = arbitro.cacho_jugadores[1]
    cacho3 = arbitro.cacho_jugadores[2]

    cacho1.GetDados.return_value = [1, 2]
    cacho2.GetDados.return_value = [3, 4]
    cacho3.GetDados.return_value = [5, 6]

    # 3 jugadores * 5 dados = 15 dados iniciales
    # Mitad de dados iniciales = 7.5 ~ 7
    # Dados en juego: 6, no cumple condición para calzar
    assert arbitro.puede_calzar(jugador_calzador="J1") == False

def test_puede_calzar_cumple_condicion_un_dado(arbitro):
    cacho1 = arbitro.cacho_jugadores[0]
    cacho2 = arbitro.cacho_jugadores[1]
    cacho3 = arbitro.cacho_jugadores[2]

    cacho1.GetDados.return_value = [3]
    cacho2.GetDados.return_value = [3, 4]
    cacho3.GetDados.return_value = [5, 6]

    # J1 está calzando y tiene un dado, cumple condición para calzar
    assert arbitro.puede_calzar(jugador_calzador="J1") == True

def test_puede_calzar_no_cumple_ninguna_condicion(arbitro):
    cacho1 = arbitro.cacho_jugadores[0]
    cacho2 = arbitro.cacho_jugadores[1]
    cacho3 = arbitro.cacho_jugadores[2]

    cacho1.GetDados.return_value = [3, 4]
    cacho2.GetDados.return_value = [3, 4]
    cacho3.GetDados.return_value = [5, 6]

    # J1 está calzando pero no tiene un solo dado, ni hay suficientes dados, 
    # no cumple condición para calzar
    assert arbitro.puede_calzar(jugador_calzador="J1") == False


# =========================================== Tests de ronda especial ===========================================
'''
Estos tests abarcan el caso donde estamos en una ronda obligada. El gestor modificará
un atributo de la clase ArbitroRonda para reflejarlo
'''

def test_dudar_ronda_especial_ases_no_son_comodines_pierde_apostador(arbitro):
    arbitro.ronda_especial = True
    pinta_cantada = 3
    cantidad_cantada = 4
    jugador_apostador = "J1"
    jugador_dudor = "J2"

    # Mockeamos el contador para simular que, SIN contar ases, hay 3 pintas
    arbitro._mock_contador.contar_pintas.return_value = 3

    jugador_ganador, jugador_perdedor, total_pintas = arbitro.dudar(
        pinta_cantada=pinta_cantada,
        cantidad_cantada=cantidad_cantada,
        jugador_apostador=jugador_apostador,
        jugador_dudor=jugador_dudor
    )

    assert jugador_ganador == jugador_dudor  # Como hay menos pintas, pierde el apostador
    assert jugador_perdedor == jugador_apostador
    assert total_pintas == 3
    arbitro._mock_contador.contar_pintas.assert_called_once_with(
        pinta_cantada,
        ases_comodines=False
    )

def test_dudar_ronda_especial_ases_no_son_comodines_pierde_dudor(arbitro):
    arbitro.ronda_especial = True
    pinta_cantada = 3
    cantidad_cantada = 3
    jugador_apostador = "J1"
    jugador_dudor = "J2"

    # Mockeamos el contador para simular que, SIN contar ases, hay 3 pintas
    arbitro._mock_contador.contar_pintas.return_value = 3

    jugador_ganador, jugador_perdedor, total_pintas = arbitro.dudar(
        pinta_cantada=pinta_cantada,
        cantidad_cantada=cantidad_cantada,
        jugador_apostador=jugador_apostador,
        jugador_dudor=jugador_dudor
    )

    assert jugador_ganador == jugador_apostador  # Como hay menos pintas, pierde el dudor
    assert jugador_perdedor == jugador_dudor
    assert total_pintas == 3
    arbitro._mock_contador.contar_pintas.assert_called_once_with(
        pinta_cantada,
        ases_comodines=False
    )

    