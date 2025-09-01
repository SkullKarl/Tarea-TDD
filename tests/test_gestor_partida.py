from src.juego.cacho import Cacho
from src.juego.arbitro_ronda import ArbitroRonda
from src.juego.gestor_partida import GestorPartida

def test_IniciarPartida():
    j = ['1', '2', '3']
    J = [Cacho(), Cacho(), Cacho()]
    A = ArbitroRonda(j, J)
    GP = GestorPartida(A, J)
    X = GP.IniciarPartida()
    assert isinstance(X, int)
    assert X in range(1, len(j))