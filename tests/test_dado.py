import os
import sys
from src.juego.dado import Dado, Pintas

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

def test_lanzar():
    dado = Dado()
    dado.lanzar()
    assert dado.cara in [1, 2, 3, 4, 5, 6]

def test_GetDenominacion():
    dado_1 = Dado(1)
    dado_2 = Dado(2)
    dado_3 = Dado(3)
    dado_4 = Dado(4)
    dado_5 = Dado(5)
    dado_6 = Dado(6)

    assert dado_1.GetDenominacion() == "As" 
    assert dado_2.GetDenominacion() == "Tonto" 
    assert dado_3.GetDenominacion() == "Tren" 
    assert dado_4.GetDenominacion() == "Cuadra" 
    assert dado_5.GetDenominacion() == "Quina"
    assert dado_6.GetDenominacion() == "Sexto"
