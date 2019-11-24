import math


class ParametrosPerforacion:

    @staticmethod
    def vel_anular(bomba, d_ext, d_int):

        return (24.51 * bomba.get_gasto()) / ((d_ext ** 2) - (d_int ** 2))
    @staticmethod
    def indice_limpieza(fluido, vel):
        if fluido.get_n() is 0 or fluido.get_k() is 0:
            n = 3.32 * math.log10(((2 * fluido.get_visco_plastica()) + fluido.get_p_cedencia()) / (
                        fluido.get_visco_plastica() + fluido.get_p_cedencia()))
            fluido.set_n(n)
            indice_consistencia = (fluido.get_visco_plastica() + fluido.get_p_cedencia()) / math.pow(511, n)
            fluido.set_k(indice_consistencia)
        print(fluido.get_k())
        return (fluido.get_dl() * fluido.get_k() * vel) / 48000

    @staticmethod
    def capacicad_accrreo(pozo):
        for x in pozo.get_anulares():
            x.set_indice_acarreo(pozo.get_fluido().get_dl() * x.get_velociad_anular() * pozo.get_fluido().get_k() /
                                 48000)

    @staticmethod
    def dec(pozo):
        return (pozo.get_dp_anular() * 0.703 / pozo.get_profundidad()) + pozo.get_fluido().get_dl()
