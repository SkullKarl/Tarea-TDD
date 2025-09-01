import math
from juego.dado import Pintas

class ValidadorApuesta:
    def esPrimerApuestaDelTurnoValida(self, apuesta,cant_dados):
        cant_aposta, tipo_apuesta = apuesta

        int_tipo_apuesta = Pintas[tipo_apuesta].value

        if int_tipo_apuesta != 1:
            return True

        if int_tipo_apuesta == 1 and cant_dados == 1: 
            return True

        return False

    
    def esValido(self, apuesta_anterior, apuesta_nueva):
        cantidad_ant, tipo_ant = apuesta_anterior
        cantidad_nue, tipo_nue = apuesta_nueva

        valor_tipo_ant = Pintas[tipo_ant].value
        valor_tipo_nue = Pintas[tipo_nue].value

        if valor_tipo_nue == 1 and valor_tipo_ant == 1:
            return False
        if valor_tipo_ant == 1:
            return self.esValido_DE_As(cantidad_ant,cantidad_nue)
        if valor_tipo_nue == 1:
            return self.esValido_A_As(cantidad_ant,cantidad_nue)

        # No puede ser menor en cantidad o tipo
        if cantidad_nue < cantidad_ant:
            return False
        if cantidad_nue == cantidad_ant and valor_tipo_nue <= valor_tipo_ant:
            return False
        if cantidad_nue > cantidad_ant and valor_tipo_nue < valor_tipo_ant:
            return False

        # Si pasa las validaciones anteriores, la apuesta es válida
        return True

    def esValido_A_As(self,cantidad_ant,cantidad_nue):
        if(cantidad_ant % 2 == 0):
            # PAR: Mitad mas uno
            return cantidad_nue == (cantidad_ant // 2) + 1
        else:
            # IMPAR: Mitad redondeada para arriba
            return cantidad_nue == math.ceil(cantidad_ant/2)

    def esValido_DE_As(self,cantidad_ant,cantidad_nue):
        return (cantidad_nue == (cantidad_ant * 2) + 1)
