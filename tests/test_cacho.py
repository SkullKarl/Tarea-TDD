from src.juego.cacho import Cacho
from src.juego.dado import Dado

def test_init_cacho():
    cacho = Cacho()
    dados = cacho.GetDados()

    assert len(dados) == 5

    for dado in dados:
        assert isinstance(dado, Dado)