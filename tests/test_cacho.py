import random
from src.juego.cacho import Cacho
from src.juego.dado import Dado

def test_init_cacho():
    cacho = Cacho()
    dados = cacho.GetDados()

    assert len(dados) == 5

    for dado in dados:
        assert isinstance(dado, Dado)

def test_agregar_quitar_dado_cacho():
    cacho = Cacho()
    assert len(cacho.GetDados()) == 5

    cacho.agregar_dado()
    assert len(cacho.GetDados()) == 6

    cacho.agregar_dado()
    assert len(cacho.GetDados()) == 7

    # Quitar dados hasta que quede al menos p
    while len(cacho.GetDados()) > 0:
        cacho.quitar_dado()

    assert len(cacho.GetDados()) == 0
