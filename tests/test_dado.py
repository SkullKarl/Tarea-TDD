import os
import sys
from src.juego.dado import Dado, Pintas

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

def test_lanzar():
    dado = Dado()
    dado.lanzar()
    assert dado.cara in [1, 2, 3, 4, 5, 6]
    assert dado.pinta in ["As", "Tonto", "Tren", "Cuadra", "Quina", "Sexto"]