import math


class General:
    d_ext = 0
    d_int = 0
    long_md = 0
    long_mv = 0
    inicio_pd = 0
    inicio_pv = 0
    fin_pd = 0
    fin_pv = 0
    capacidad = 0
    vol_interior = 0
    long_disp = 0
    direccional = None

    def profundidad(self, dd):
        long = self.long_md
        inicio = self.inicio_pd
        for x in dd:
            disponible = x.get_fin_pd() - inicio
            if disponible >= long:
                self.fin_pv += get_long_pv(long, x)
                return 0
            elif disponible > long > disponible:
                long -= disponible
                self.fin_pv += get_long_pv(disponible, x)
                inicio += disponible
            else:
                self.fin_pv += get_long_pv(long, x)
                return 0

    def __init__(self, d_e, d, l, d_direccional, previa):
        self.long_disp = l
        self.d_ext = d_e
        self.d_int = d
        self.long_md = l
        self.capacidad = 0.5067 * (self.d_int ** 2)
        self.direccional = d_direccional
        if previa is not None:
            self.inicio_pd = previa.get_fin_pd()
            self.inicio_pv = previa.get_fin_pv()
            self.fin_pd = previa.get_fin_pd() + l
        else:
            self.inicio_pd = 0
            self.inicio_pv = 0
            self.fin_pd = l

        self.fin_pv = self.inicio_pv
        self.profundidad(d_direccional)
        self.long_mv = self.fin_pv - self.inicio_pv
        self.vol_interior = self.capacidad * self.long_md

    def __str__(self):
        return """\
Diametro exterior       \t{}
Diametro interior      \t{}
Inicio PD               \t{}
Longitud PD             \t{}
Fin PD                  \t{}
Inicio PV               \t{}
Longitud PV             \t{}
Fin PV                  \t{}""".format(self.d_ext, self.d_int, self.inicio_pd, self.long_md, self.fin_pd,
                                       self.inicio_pv,
                                       self.long_mv, self.fin_pv)

    def get_inicio_pd(self):
        return self.inicio_pd

    def get_inicio_pv(self):
        return self.inicio_pv

    def get_lv(self):
        return self.long_mv

    def get_fin_pd(self):
        return self.fin_pd

    def get_fin_pv(self):
        return self.fin_pv

    def get_dext(self):
        return self.d_ext

    def get_dint(self):
        return self.d_int

    def get_long(self):
        return self.long_md

    def set_long(self, data):
        self.long_md = data

    def set_fin_pv(self, data):
        self.fin_pv = data

    def set_lv(self):

        self.long_mv = self.fin_pv - self.inicio_pv

    def set_inicio_pv(self, data):
        self.inicio_pv = data

    def get_long_disp(self):
        return self.long_disp

    def set_disp(self, data):
        self.long_disp = data

    def update_vertical(self):
        self.profundidad(self.direccional)

def get_long_pv(long_pd, x):
    return long_pd * (math.cos(math.radians(x.get_angulo())))