from juego.dado import Pintas

class ValidadorApuesta:
    def __init__(self):
        pass

    def esValido(self, apuesta_anterior, apuesta_nueva):
        cantidad_anterior, tipo_anterior = apuesta_anterior
        cantidad_nueva, tipo_nueva = apuesta_nueva

        tipo_anterior_int = Pintas[tipo_anterior].value
        tipo_nueva_int = Pintas[tipo_nueva].value

        if (cantidad_anterior > cantidad_nueva):
            return False

        if (tipo_anterior_int > tipo_nueva_int):
            return False
        
        if (cantidad_anterior == cantidad_nueva and tipo_anterior == tipo_nueva):
            return False

        if(tipo_anterior_int < tipo_nueva_int and cantidad_anterior == cantidad_nueva):
            return True
        
        if(tipo_anterior_int == tipo_nueva_int and cantidad_anterior < cantidad_nueva):
            return True
        
        return False
        