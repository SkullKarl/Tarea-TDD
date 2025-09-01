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

def test_JugarRonda():
    j = ['1', '2', '3']
    J = [Cacho(), Cacho(), Cacho()]
    A = ArbitroRonda(j, J)
    GP = GestorPartida(A, J)
    X = GP.JugarRonda()
    assert J != X

def test_obligar():
    j = ['1', '2', '3']
    J = [Cacho(), Cacho(), Cacho()]
    A = ArbitroRonda(j, J)
    GP = GestorPartida(A, J)
    jugador_con_un_dado = J[1]
    X = GP.obligar(jugador_con_un_dado)
    assert X == True