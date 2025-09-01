from juego.dado import Pintas

class ValidadorApuesta:
    def esValido(self, apuesta_anterior, apuesta_nueva):
        cantidad_ant, tipo_ant = apuesta_anterior
        cantidad_nue, tipo_nue = apuesta_nueva

        valor_tipo_ant = Pintas[tipo_ant].value
        valor_tipo_nue = Pintas[tipo_nue].value

        # No puede ser menor en cantidad o tipo
        if cantidad_nue < cantidad_ant:
            return False
        if cantidad_nue == cantidad_ant and valor_tipo_nue <= valor_tipo_ant:
            return False
        if cantidad_nue > cantidad_ant and valor_tipo_nue < valor_tipo_ant:
            return False

        # Si pasa las validaciones anteriores, la apuesta es válida
        return True
