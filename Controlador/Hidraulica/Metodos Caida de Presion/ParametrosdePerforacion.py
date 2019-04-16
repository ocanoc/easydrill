class PamarametosPerforacion:

    @staticmethod
    def inidice_limpieza(pozo):
        return (pozo.get_barrena().get_caidad_presion() * pozo.get_bomba().get_gasto()) /\
               (1346.18 * (pozo.get_barrena().get_dext()))

    @staticmethod
    def capacicad_accrreo(pozo):
        for x in pozo.get_anulares():
            x.set_indice_acarreo(pozo.get_fluido().get_dl() * x.get_velociad_anular() * pozo.get_fluido().get_k() /
                                 48000)

    @staticmethod
    def dec(pozo):
        return (pozo.get_dp_anular() * 0.703 / pozo.get_profundidad()) + pozo.get_fluido().get_dl()
