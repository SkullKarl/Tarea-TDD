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

def test_apuesta_caso_ases():
    validador = ValidadorApuesta()

    # --------- A AS|ES ---------
    #
    
    # MITAD REDONDEADA PARA ARRIBA [IMPRAR]
    apuesta_anterior = (7, "Tren")
    apuesta_nueva = (4, "As")
    assert True == validador.esValido(apuesta_anterior, apuesta_nueva)

    apuesta_anterior = (7, "Tren")
    apuesta_nueva = (3, "As")
    assert False == validador.esValido(apuesta_anterior, apuesta_nueva)

    # MITAD MAS UNO [PAR]
    apuesta_anterior = (8, "Cuadra")
    apuesta_nueva = (5, "As")
    assert True == validador.esValido(apuesta_anterior, apuesta_nueva)

    apuesta_anterior = (8, "Cuadra")
    apuesta_nueva = (4, "As")
    assert False == validador.esValido(apuesta_anterior, apuesta_nueva)

    # --------- DE ASES ---------
    #
    apuesta_anterior = (2, "As")
    apuesta_nueva = (5, "Quinta")
    assert True == validador.esValido(apuesta_anterior, apuesta_nueva)

    apuesta_anterior = (2, "As")
    apuesta_nueva = (4, "Quinta")
    assert False == validador.esValido(apuesta_anterior, apuesta_nueva)

    # --------- DE ASES HACIA ASES ---------
    apuesta_anterior = (2, "As")
    apuesta_nueva = (5, "As")
    assert False == validador.esValido(apuesta_anterior, apuesta_nueva)

    apuesta_anterior = (8, "As")
    apuesta_nueva = (5, "As")
    assert False == validador.esValido(apuesta_anterior, apuesta_nueva)
