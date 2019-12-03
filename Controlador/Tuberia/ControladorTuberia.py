import math


class ControladorTuberia:
    @staticmethod
    def get_long_pv(long_pd, x):
        return long_pd * (math.cos(math.radians(x)))

    @staticmethod
    def profundidad_vertical(interiores, direccional):
        long_tp_provi = 0
        count = 0
        for x in interiores:
            inicio_tp = x.get_inicio_pd()
            fin_tp = x.get_fin_pd()
            for y in direccional:
                inicio_e_pd = y.get_inicio_pd()
                fin_e_pd = y.get_fin_pd()
                angulo_e = y.get_angulo()
                if not (inicio_tp >= fin_e_pd):
                    if inicio_tp >= inicio_e_pd and fin_tp <= fin_e_pd:
                        long_tp_provi += ControladorTuberia.get_long_pv(fin_tp - inicio_tp, angulo_e)
                        x.set_fin_pv(long_tp_provi)
                        if count is 0:
                            x.set_inicio_pv(0)
                            x.set_lv()
                        else:
                            x.set_inicio_pv(interiores[count - 1].get_fin_pv())
                            x.set_lv()
                        count += 1
                        break
                    elif inicio_tp >= inicio_e_pd and fin_tp >= fin_e_pd:
                        long_tp_provi += ControladorTuberia.get_long_pv(fin_e_pd - inicio_tp, angulo_e)
                        inicio_tp = fin_e_pd

    @staticmethod
    def set_velocdad_interior(interiores, bomba):
        for x in interiores:
            x.set_vel_interior(bomba.get_gasto() * 24.51 / math.pow(x.get_dint(), 2))
