import os
import sys
import pytest
from unittest.mock import MagicMock
from src.juego.contador_pintas import ContadorPintas

def test_contador_pintas_ases_comodines():
    # Caso estándar
    # Simularemos esta partida de dudo con 3 jugadores:
    # cacho 1 = [2, 2, 1, 4, 5]
    # cacho 2 = [3, 3, 6, 6, 6]
    # cacho 3 = [1, 2, 2, 5, 1]

    cacho1 = MagicMock()
    cacho2 = MagicMock()
    cacho3 = MagicMock()

    cacho1.dados = [2, 2, 1, 4, 5]
    cacho2.dados = [3, 3, 6, 6, 6]
    cacho3.dados = [1, 2, 2, 5, 1]

    cacho1.obtener_dados.return_value = cacho1.dados
    cacho2.obtener_dados.return_value = cacho2.dados
    cacho3.obtener_dados.return_value = cacho3.dados

    contador_pintas = ContadorPintas([cacho1, cacho2, cacho3])

    # Contamos los 2 considerando 1 como comodín, total = 7
    resultado = contador_pintas.contar_pintas(2, ases_comodines=True)

    assert resultado == 7

def test_contador_pintas_ases():
    # Caso de apuesta por ases
    # Simularemos esta partida de dudo con 3 jugadores:
    # cacho 1 = [2, 2, 1, 4, 5]
    # cacho 2 = [3, 3, 6, 6, 6]
    # cacho 3 = [1, 2, 2, 5, 1]

    cacho1 = MagicMock()
    cacho2 = MagicMock()
    cacho3 = MagicMock()

    cacho1.dados = [2, 2, 1, 4, 5]
    cacho2.dados = [3, 3, 6, 6, 6]
    cacho3.dados = [1, 2, 2, 5, 1]

    cacho1.obtener_dados.return_value = cacho1.dados
    cacho2.obtener_dados.return_value = cacho2.dados
    cacho3.obtener_dados.return_value = cacho3.dados

    contador_pintas = ContadorPintas([cacho1, cacho2, cacho3])

    # Contamos los 1, total = 3
    resultado = contador_pintas.contar_pintas(1, ases_comodines=False)

    assert resultado == 3

def test_contador_pintas_obligado():
    # Caso ronda obligado, los 1 no valen como comodín
    # Simularemos esta partida de dudo con 3 jugadores con obligado:
    # cacho 1 = [2]
    # cacho 2 = [3, 3, 6, 6, 6]
    # cacho 3 = [1, 2, 2, 5, 1]

    cacho1 = MagicMock()
    cacho2 = MagicMock()
    cacho3 = MagicMock()

    cacho1.dados = [2]
    cacho2.dados = [3, 3, 6, 6, 6]
    cacho3.dados = [1, 2, 2, 5, 1]

    cacho1.obtener_dados.return_value = cacho1.dados
    cacho2.obtener_dados.return_value = cacho2.dados
    cacho3.obtener_dados.return_value = cacho3.dados

    contador_pintas = ContadorPintas([cacho1, cacho2, cacho3])

    # Contamos los 6, total = 3
    resultado = contador_pintas.contar_pintas(6, ases_comodines=False)

    assert resultado == 3

def test_contador_pintas_obligado_ases():
    # Caso de ronda obligado, apostando por ases
    # Simularemos esta partida de dudo con 3 jugadores:
    # cacho 1 = [1]
    # cacho 2 = [3, 3, 6, 6, 6]
    # cacho 3 = [1, 2, 2, 5, 1]

    cacho1 = MagicMock()
    cacho2 = MagicMock()
    cacho3 = MagicMock()

    cacho1.dados = [1]
    cacho2.dados = [3, 3, 6, 6, 6]
    cacho3.dados = [1, 2, 2, 5, 1]

    cacho1.obtener_dados.return_value = cacho1.dados
    cacho2.obtener_dados.return_value = cacho2.dados
    cacho3.obtener_dados.return_value = cacho3.dados

    contador_pintas = ContadorPintas([cacho1, cacho2, cacho3])

    # Contamos los 1, total = 3
    resultado = contador_pintas.contar_pintas(1, ases_comodines=False)

    assert resultado == 3