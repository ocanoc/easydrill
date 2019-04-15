import math
from Modelo.Objetos.Hidraulica.SeccionesAnulares import *


class ControladorSecciones:
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
                                                                x, y, direccional))
                    if (y.get_inicio_pd() >= x.get_inicio_pd()) and (y.get_fin_pd() > x.get_fin_pd()):
                        listasecciones.append(SeccionesAnulares(x.get_fin_pd() - longdisp, x.get_fin_pd(), longdisp,
                                                                x, y, direccional))
                        longrestante = y.get_long() - longdisp
                        longdisp = 0
                        break
                    else:
                        longdisp -= longrestante
                        listasecciones.append(SeccionesAnulares(y.get_fin_pd() - longrestante, y.get_fin_pd(),
                                                                longrestante, x, y, direccional))
                        y.setentr()
        return listasecciones

