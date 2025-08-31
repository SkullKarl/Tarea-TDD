from src.juego.validador_apuesta import ValidadorApuesta

def test_apuesta_valida():
    validador = ValidadorApuesta()

    apuesta_anterior = (3, "Tren")
    apuesta_nueva = (2, "Tren")
    assert False == validador.esValido(apuesta_anterior, apuesta_nueva)

    apuesta_anterior = (3, "Tren")
    apuesta_nueva = (3, "Tren")
    assert False == validador.esValido(apuesta_anterior, apuesta_nueva)

    apuesta_anterior = (3, "Tren")
    apuesta_nueva = (4, "Tren")
    assert True == validador.esValido(apuesta_anterior, apuesta_nueva)

    apuesta_anterior = (3, "Tren")
    apuesta_nueva = (3, "Cuadra")
    assert True == validador.esValido(apuesta_anterior, apuesta_nueva)
    
    apuesta_anterior = (3, "Tren")
    apuesta_nueva = (4, "Tonto")
    assert False == validador.esValido(apuesta_anterior, apuesta_nueva)

    apuesta_anterior = (3, "Tren")
    apuesta_nueva = (3, "Tonto")
    assert False == validador.esValido(apuesta_anterior, apuesta_nueva)
