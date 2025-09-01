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
    apuesta_actual = {"pinta" : 3, "cantidad" : 6, "jugador": "J1"}  # J1 apostó 6 trenes
    jugador_apostador = apuesta_actual["jugador"]
    jugador_dudor = "J2" # jugador que dudó de esa apuesta

    resultado = arbitro.dudar(
        apuesta_actual=apuesta_actual,
        jugador_dudor=jugador_dudor
    )

    # luego, asumimos que la función dudar de arbitro_ronda retornará un diccionario con
    # quién gana, quien pierde y la cantidad real
    assert resultado["jugador_ganador"] == jugador_apostador
    assert resultado["jugador_perdedor"] == jugador_dudor
    assert resultado["total_pintas"] == 7


def test_dudar_pierde_jugador_apostador(arbitro):
    """
    Si la cantidad real de la pinta apostada es menor a la apuesta,
    pierde el jugador que apostó
    """
    arbitro._mock_contador.contar_pintas.return_value = 5 # Hay 5 trenes reales, contando comodines
    apuesta_actual = {"pinta" : 3, "cantidad" : 6, "jugador": "J1"}  # J1 apostó 6 trenes
    jugador_apostador = apuesta_actual["jugador"]
    jugador_dudor = "J2" # jugador que dudó de esa apuesta

    resultado = arbitro.dudar(
        apuesta_actual=apuesta_actual,
        jugador_dudor=jugador_dudor
    )

    assert resultado["jugador_ganador"] == jugador_dudor
    assert resultado["jugador_perdedor"] == jugador_apostador
    assert resultado["total_pintas"] == 5

# =========================================== Tests calzar ===========================================

# Test calzar mínimo, sin contar el mock de validar ni reglas especiales
def test_calzar_exito(arbitro):
    arbitro._mock_contador.contar_pintas.return_value = 6
    apuesta_actual = {"pinta": 3, "cantidad": 6, "jugador": "J1"}  # J1 apostó 6 trenes
    jugador_calzador = "J2" # J2 intenta calzar

    resultado = arbitro.calzar(
        apuesta_actual=apuesta_actual,
        jugador_calzador=jugador_calzador
    )

    assert resultado["jugador_ganador"] == jugador_calzador
    assert resultado["jugador_perdedor"] == None
    assert resultado["total_pintas"] == 6


def test_calzar_fracaso(arbitro):
    arbitro._mock_contador.contar_pintas.return_value = 4
    apuesta_actual = {"pinta": 3, "cantidad": 5, "jugador": "J1"}  # J1 apostó 5 trenes
    jugador_calzador = "J2" # J2 intenta calzar

    resultado = arbitro.calzar(
        apuesta_actual=apuesta_actual,
        jugador_calzador=jugador_calzador
    )

    assert resultado["jugador_ganador"] == None
    assert resultado["jugador_perdedor"] == jugador_calzador
    assert resultado["total_pintas"] == 4