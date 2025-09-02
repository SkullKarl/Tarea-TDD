from src.juego.cacho import Cacho
from src.juego.arbitro_ronda import ArbitroRonda
from src.juego.gestor_partida import GestorPartida, Obligar

def test_IniciarPartida():
    j = ['1', '2', '3']
    J = [Cacho(), Cacho(), Cacho()]
    A = ArbitroRonda(j, J)
    GP = GestorPartida(A, j, J)
    X = GP.IniciarPartida()
    assert isinstance(X, str)
    assert X in ['1', '2', '3']

"""def test_JugarRonda():
    j = ['1', '2', '3']
    J = [Cacho(), Cacho(), Cacho()]
    A = ArbitroRonda(j, J)
    GP = GestorPartida(A, j, J)
    X = GP.JugarRonda()
    assert J != X

def test_obligar():
    j = ['1', '2', '3']
    J = [Cacho(), Cacho(), Cacho()]
    J[1]
    A = ArbitroRonda(j, J)
    GP = GestorPartida(A, j, J)
    X = GP.obligar(J[1], Obligar.Abierta)
    assert X == True

def test_FinalizarPartida():
    j = ['1', '2', '3']
    J = [Cacho(), Cacho(), Cacho()]
    A = ArbitroRonda(j, J)
    GP = GestorPartida(A, j, J)
    Ganador = GP.FinalizarPartida()
    assert isinstance(Ganador, str)
    assert Ganador in ['1', '2', '3']"""