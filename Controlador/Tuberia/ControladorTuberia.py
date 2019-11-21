import math


class ControladorTuberia:
    @staticmethod
    def get_long_pv(long_pd, x):
        return long_pd * (math.cos(math.radians(x)))

    @staticmethod
    def profundidad_vertical(interiores, direccional):
        long_tp_provi = 0
        for x in interiores:
            inicio_tp = x.get_inicio_pd()
            fin_tp = x.get_fin_pd()
            long_tp = x.get_long()
            for y in direccional:
                inicio_e_pd = y.get_inicio_pd()
                fin_e_pd = y.get_fin_pd()
                inicio_e_pv = y.get_inicio_pv()
                fin_e_pv = y.get_fin_pv()
                angulo_e = y.get_angulo()
                print("""\
Inicio tp md               \t{} Fin tp md                  \t{}

Inicio estacion md         \t{} fin estacion md             \t{}""".format(inicio_tp, fin_tp, inicio_e_pd, fin_e_pd))
                if inicio_tp >= inicio_e_pd and fin_tp <= fin_e_pd:
                    long_tp_pv = ControladorTuberia.get_long_pv(long_tp, angulo_e)
                    print(long_tp_pv)
                    break
                elif inicio_tp >= inicio_e_pd and fin_tp >= fin_e_pd:
                    long_tp_provi += ControladorTuberia.get_long_pv(fin_e_pd - inicio_tp, angulo_e)
                    inicio_tp = fin_e_pd
                    print(long_tp_provi)
