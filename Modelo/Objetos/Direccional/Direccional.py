import math


class Direccional:
    InicioPD = 0
    InicioPV = 0
    FinPD = 0
    FinPV = 0
    LD = 0
    Longitud = 0
    LV = 0
    angulo = 0
    tipo = ""

    def __init__(self, tipo, angulo, longitdmd, longitdmv, iniciopd, iniciopv):
        self.tipo = tipo
        self.angulo = angulo
        self.InicioPD = iniciopd
        self.InicioPV = iniciopv
        self.LV = longitdmv
        self.LD = longitdmd
        self.FinPD = iniciopd + longitdmd
        self.FinPV = iniciopv + longitdmv

    def __str__(self):
        return """\
Tipo                            \t{}
Incio Profundidad desarrollada  \t{}
longitud desarrollada           \t{}
Fin Profundidad desarrollada    \t{}
Incio Profundidad vertical      \t{}
Longitud vertical               \t{}
Fin Profundidad vertical        \t{}
Angulo                          \t{}""".format(self.tipo, self.InicioPD, self.LD, self.FinPD, self.InicioPV, self.LV,
                                               self.FinPV, self.angulo)

    def get_tipo(self):
        return self.tipo

    def get_angulo(self):
        return self.angulo

    def get_inicio_pd(self):
        return self.InicioPD

    def get_inicio_pv(self):
        return self.InicioPV

    def get_lv(self):
        return self.LV

    def get_ld(self):
        return self.LD

    def get_fin_pd(self):
        return self.FinPD

    def get_fin_pv(self):
        return self.FinPV
