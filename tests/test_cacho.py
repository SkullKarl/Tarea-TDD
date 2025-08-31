import random
from src.juego.cacho import Cacho
from src.juego.dado import Dado

def test_init_cacho():
    cacho = Cacho()
    dados = cacho.GetDados()

    assert len(dados) == 5

    for dado in dados:
        assert isinstance(dado, Dado)

def test_agitar_cacho():
    cacho = Cacho()
    dados_antes = cacho.GetDados()
    caras_antes = [dado.cara for dado in dados_antes]

    random.seed(42)  # Fijar la semilla para asegurar cambio de valores 
    cacho.agitar()

    dados_despues = cacho.GetDados()
    caras_despues = [dado.cara for dado in dados_despues]

    assert caras_antes != caras_despues

def test_mostrar_ocultar_cacho():
    cacho = Cacho()
    cacho.ocultar()
    dados = cacho.GetDados()
    assert dado is None
    cacho.mostrar()
    dados = cacho.GetDados()

    for dado in dados:
        assert isinstance(dado, Dado)
