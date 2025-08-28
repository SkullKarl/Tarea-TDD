from src.juego.cacho import Cacho
from src.juego.dado import Dado

def test_init_cacho():
    cacho = Cacho()
    for dado in cacho.dados:
        assert isinstance(dado, Dado)
    assert len(cacho.dados) == 5