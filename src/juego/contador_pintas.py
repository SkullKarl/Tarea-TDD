class ContadorPintas:
    def __init__(self, cacho_jugadores):
        self.cacho_jugadores = cacho_jugadores

    def contar_pintas(self, pinta_cantada, ases_comodines=True):
        total = 0
        for cacho in self.cacho_jugadores:
            if cacho is None:
                continue
            for dado in cacho.GetDados() or []:
                if pinta_cantada == 1:
                    # Solo cuentan los unos
                    if dado == 1:
                        total += 1
                elif not ases_comodines:
                    # Ronda obligada: los ases no son comodines
                    if dado == pinta_cantada:
                        total += 1
                else:
                    # Caso estándar: la pinta o un as cuentan
                    if dado == pinta_cantada or dado == 1:
                        total += 1
        return total
