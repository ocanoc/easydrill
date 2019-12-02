from Controlador.Hidraulica.Metodos.ParametrosdePerforacion import *
from Modelo.Objetos.Hidraulica.SeccionesAnulares import *


class ControladorSecciones:
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
            longdisp = x.get_long_disp()
            print("diponible tr", longdisp)
            for y in interior:
                print(longrestante)
                if longdisp > 0 and y.getentr() is False:
                    if (y.get_inicio_pd() >= x.get_inicio_pd()) and (y.get_fin_pd() <= x.get_fin_pd()):
                        print("caso1")
                        print("meti :", y.get_long())
                        longdisp -= y.get_long()
                        x.set_disp(longdisp)
                        y.setentr()
                        listasecciones.append(SeccionesAnulares(y.get_inicio_pd(), y.get_fin_pd(), y.get_long(), x, y))
                    elif (y.get_inicio_pd() >= x.get_inicio_pd()) and (y.get_fin_pd() >= x.get_fin_pd()):
                        print("caso2")
                        longrestante = y.get_long()
                        print("meti :", longdisp)
                        print("resta", longrestante - longdisp)
                        listasecciones.append(SeccionesAnulares(y.get_inicio_pd(), x.get_fin_pd(), longdisp, x, y))
                        x.set_disp(0)
                        longrestante = longrestante - longdisp
                        break
                    else:
                        print("caso3")
                        print("meti :", longrestante)
                        listasecciones.append(SeccionesAnulares(y.get_fin_pd() - longrestante,
                                                                x.get_inicio_pd() + longrestante, longrestante, x, y, ))
                        longrestante -= longdisp
                        x.set_disp(longdisp)
        return listasecciones

    @staticmethod
    def set_parametros(secciones, bomba, fluido):
        for x in secciones:
            x.set_vel_anular(ParametrosPerforacion.vel_anular(bomba, x.get_dmayor(), x.get_dmenor()))
            x.set_indice_acarreo(ParametrosPerforacion.cap_acarreo(fluido, x.get_vel_anular()))

    @staticmethod
    def set_dec(secciones, fluido):
        dp_anular = 0
        for x in secciones:
            dp_anular += x.get_dp()
            x.set_dec(fluido.get_dl() + (dp_anular * 10 / x.get_fin_pv()))
