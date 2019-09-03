from Modelo.Objetos.Hidraulica.SeccionesAnulares import *
import math


class ControladorSecciones:

    @staticmethod
    def profundidad(iniciopd, finpd, long, dd):
        longv = 0
        longitud = long
        for x in dd:
            disponible = x.get_fin_pd()
            if iniciopd > x.get_inicio_pd() and finpd < x.get_fin_pd():
                longv = ControladorSecciones.get_long_pv(long, x)
                return longv
            if iniciopd > x.get_inicio_pd() and finpd > x.get_fin_pd():
                longitud -= disponible
                longv += ControladorSecciones.get_long_pv(disponible, x)
                iniciopd += disponible
            else:
                longv += ControladorSecciones.get_long_pv(longitud, x)
                return 0
        return longv

    @staticmethod
    def get_long_pv(long_pd, x):
        return long_pd * (math.cos(math.radians(x.get_angulo())))

    @staticmethod
    def vel_anular(pozo):
        for x in pozo.get_anulares():
            x.set_velocidad((pozo.get_bombas().get_gasto() * 24.51) /
                            (x.get_diametroMayor ** 2 - x.get_diametroMenor ** 2))

    @staticmethod
    def creasecciones(exterior, interior, direccional):
        longrestante = 0
        listasecciones = []
        for x in exterior:
            longdisp = x.get_long()
            for y in interior:
                if longdisp > 0 and y.getentr() is False:
                    if (y.get_inicio_pd() >= x.get_inicio_pd()) and (y.get_fin_pd() <= x.get_fin_pd()):
                        longdisp -= y.get_long()
                        y.setentr()
                        listasecciones.append(SeccionesAnulares(y.get_inicio_pd(), y.get_fin_pd(), y.get_long(),
                                                                x, y,
                                                                ControladorSecciones.profundidad(y.get_inicio_pd(),
                                                                                                 y.get_fin_pd(),
                                                                                                 y.get_long(),
                                                                                                 direccional)))
                    if (y.get_inicio_pd() >= x.get_inicio_pd()) and (y.get_fin_pd() > x.get_fin_pd()):
                        listasecciones.append(SeccionesAnulares(x.get_fin_pd() - longdisp, x.get_fin_pd(), longdisp,
                                                                x, y, ControladorSecciones.profundidad(x.get_fin_pd() -
                                                                                                       longdisp,
                                                                                                       x.get_fin_pd(),
                                                                                                       longdisp,
                                                                                                       direccional)))
                        longrestante = y.get_long() - longdisp
                        longdisp = 0
                        break
                    else:
                        longdisp -= longrestante
                        listasecciones.append(SeccionesAnulares(y.get_fin_pd() - longrestante, y.get_fin_pd(),
                                                                longrestante, x, y,
                                                                ControladorSecciones.profundidad(y.get_fin_pd() -
                                                                                                 longrestante,
                                                                                                 y.get_fin_pd(),
                                                                                                 longrestante,
                                                                                                 direccional)))
                        y.setentr()
        return listasecciones
