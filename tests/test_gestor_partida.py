from src.juego.cacho import Cacho
from src.juego.gestor_partida import GestorPartida, ObligarOpciones

def test_IniciarPartida():
    j = ['Gustavo', 'Sebastian', 'Sofia', 'Slayer']
    J = [Cacho(), Cacho(), Cacho(), Cacho()]
    GP = GestorPartida(j, J)
    X = GP.IniciarPartida()
    assert isinstance(X, str)
    assert X in ['Gustavo', 'Sebastian', 'Sofia', 'Slayer']

def test_JugarRonda():
    j = ['Gustavo', 'Sebastian', 'Sofia', 'Slayer']
    J = [Cacho(), Cacho(), Cacho(), Cacho()]
    GP = GestorPartida(j, J)
    GP.JugarRonda(2, 3, 'Slayer', dudo=True, jugador_dudor='Gustavo')
    GP.JugarRonda(3, 4, 'Gustavo', dudo=True, jugador_dudor='Sebastian')
    assert len(J[2].GetDados()) == len(GP.jugadores[2].GetDados())

def test_obligar():
    j = ['Gustavo', 'Sebastian', 'Sofia', 'Slayer']
    J = [Cacho(), Cacho(), Cacho(), Cacho()]
    for i in range (4):
        J[1].quitar_dado()
    GP = GestorPartida(j, J)
    X = GP.obligar(1, J[1], ObligarOpciones.Abierta)
    assert X == True
    assert GP.rondaex == ObligarOpciones.Abierta

def test_FinalizarPartida():
    j = ['Gustavo', 'Sebastian', 'Sofia', 'Slayer']
    J = [Cacho(), None, None, Cacho()]
    for i in range (5):
        J[0].quitar_dado()
    GP = GestorPartida(j, J)
    GP.JugarRonda(2, 3, 'Slayer')
    Ganador = GP.FinalizarPartida()
    assert isinstance(Ganador, str)
    assert Ganador == 'Slayer'