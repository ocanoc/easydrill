import math


class General:
    dExt = 0
    dInt = 0
    longMD = 0
    longMV = 0
    inicioPD = 0
    inicioPV = 0
    finPD = 0
    finPV = 0
    capacidad = 0
    VolInterior = 0

    def profundidad(self, dd):
        long = self.longMD
        inicio = self.inicioPD
        for x in dd:
            disponible = x.get_fin_pd() - inicio
            if disponible >= long:
                self.finPD += long
                self.finPV += get_long_pv(long, x)
                return 0
            elif disponible > long > disponible:
                long -= disponible
                self.finPD += disponible
                self.finPV += get_long_pv(disponible, x)
                inicio += disponible
            else:
                self.finPD += long
                self.finPV += get_long_pv(long, x)
                return 0

    def __init__(self, d_e, d, l, d_direccional, previa):
        self.dExt = d_e
        self.dInt = d
        self.longMD = l
        self.capacidad = 0.5067*(self.dInt**2)
        if previa is not None:
            self.inicioPD = previa.get_fin_pd()
            self.inicioPV = previa.get_fin_pv()
        else:
            self.inicioPD = 0
            self.inicioPV = 0
        self.finPD = self.inicioPD
        self.finPV = self.inicioPV
        self.profundidad(d_direccional)
        self.longMV = self.finPV - self.inicioPV
        self.VolInterior = self.capacidad*self.longMD

    def __str__(self):
        return """\
Diametro exterior       \t{}
Diametro interior      \t{}
Inicio PD               \t{}
Longitud PD             \t{}
Fin PD                  \t{}
Inicio PV               \t{}
Longitud PV             \t{}
Fin PV                  \t{}""".format(self.dExt, self.dInt, self.inicioPD, self.longMD, self.finPD, self.inicioPV,
                                       self.longMV, self.finPV)

    def get_inicio_pd(self):
        return self.inicioPD

    def get_inicio_pv(self):
        return self.inicioPV

    def get_lv(self):
        return self.longMV

    def get_fin_pd(self):
        return self.finPD

    def get_fin_pv(self):
        return self.finPV

    def get_dext(self):
        return self.dExt

    def get_dint(self):
        return self.dInt

    def get_long(self):
        return self.longMD

def get_long_pv(long_pd, x):
    return long_pd * (math.cos(math.radians(x.get_angulo())))