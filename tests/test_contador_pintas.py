import pytest
from src.juego.contador_pintas import ContadorPintas

@pytest.fixture
def crear_cacho(mocker):
    def _crear(valores):
        cacho = mocker.Mock()
        cacho.dados = valores
        cacho.GetDados.return_value = valores
        return cacho
    return _crear


def test_contador_pintas_ases_comodines(crear_cacho):
    cacho1 = crear_cacho([2, 2, 1, 4, 5])
    cacho2 = crear_cacho([3, 3, 6, 6, 6])
    cacho3 = crear_cacho([1, 2, 2, 5, 1])

    contador = ContadorPintas([cacho1, cacho2, cacho3])

    # Contamos los 2 considerando ases como comodines -> total = 7
    assert contador.contar_pintas(2, ases_comodines=True) == 7


def test_contador_pintas_ases(crear_cacho):
    cacho1 = crear_cacho([2, 2, 1, 4, 5])
    cacho2 = crear_cacho([3, 3, 6, 6, 6])
    cacho3 = crear_cacho([1, 2, 2, 5, 1])

    contador = ContadorPintas([cacho1, cacho2, cacho3])

    # Contamos ases sin comodines -> total = 3
    assert contador.contar_pintas(1, ases_comodines=True) == 3


def test_contador_pintas_obligado(crear_cacho):
    cacho1 = crear_cacho([2])
    cacho2 = crear_cacho([3, 3, 6, 6, 6])
    cacho3 = crear_cacho([1, 2, 2, 5, 1])

    contador = ContadorPintas([cacho1, cacho2, cacho3])

    # Contamos los 6 en ronda obligada (ases no comodines) -> total = 3
    assert contador.contar_pintas(6, ases_comodines=False) == 3


def test_contador_pintas_obligado_ases(crear_cacho):
    cacho1 = crear_cacho([1])
    cacho2 = crear_cacho([3, 3, 6, 6, 6])
    cacho3 = crear_cacho([1, 2, 2, 5, 1])

    contador = ContadorPintas([cacho1, cacho2, cacho3])

    # Contamos los ases en ronda obligada -> total = 3
    assert contador.contar_pintas(1, ases_comodines=False) == 3
