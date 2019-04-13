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
        l = self.longMD
        inicio = self.inicioPD
        for x in dd:
            disponible = x.getFinPD() - inicio
            if disponible >= l:
                self.finPD += l
                self.finPV += get_long_pv(l, x)
                return 0
            elif disponible > 0 and l > disponible:
                l -= disponible
                self.finPD += disponible
                self.finPV += get_long_pv(disponible, x)
                inicio += disponible
            else:
                self.finPD += l
                self.finPV += get_long_pv(l, x)
                return 0

    def __init__(self, d_e, d, l, d_direccional, previa):
        self.dExt = d_e
        self.dInt = d
        self.longMD = l
        self.capacidad = 0.5067*(self.dInt**2)
        if previa is not None:
            self.inicioPD = previa.getFinPD()
            self.inicioPV = previa.getFinPV()
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

    def getInicioPD(self):
        return self.inicioPD

    def getInicioPV(self):
        return self.inicioPV

    def getLV(self):
        return self.longMV

    def getFinPD(self):
        return self.finPD

    def getFinPV(self):
        return self.finPV

    def getDext(self):
        return self.dExt

    def getDint(self):
        return self.dInt

    def getLong(self):
        return self.longMD


def get_long_pv(long_pd, x):
    return long_pd * (math.cos(math.radians(x.getAngulo())))