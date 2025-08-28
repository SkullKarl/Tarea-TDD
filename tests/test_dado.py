import os
import sys
from src.juego.dado import Dado
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))
def test_lanzar():
    dado = Dado()
    dado.lanzar()
    assert dado.cara in [1, 2, 3, 4, 5, 6]

"""def test_pinta():
    dado = Dado()
    dado.lanzar()
    dado.pintar()
    assert dado.pinta in ["As", "Tonto", "Tren", "Cuadra", "Quina", "Sexto"]"""