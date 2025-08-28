from src.juego.cacho import Cacho
from src.juego.dado import Dado
import random

def test_init_cacho():
    cacho = Cacho()
    for dado in cacho.dados:
        assert isinstance(dado, Dado)
    assert len(cacho.dados) == 5

def test_agitar_cacho():
    cacho = Cacho()
    random.seed(2) # Fijar la semilla para evitar mismos resultados
    dados = cacho.dados 
    cacho.agitar()
    valores_iniciales = [d.GetDenominacion() for d in dados]
    cacho.agitar()
    valores_revueltos = [d.GetDenominacion() for d in dados]

    assert valores_iniciales != valores_revueltos