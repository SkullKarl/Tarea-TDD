from src.juego.dado import Dado

def test_lanzar():
    dado = Dado()
    assert dado.lanzar() in [1, 2, 3, 4, 5, 6]