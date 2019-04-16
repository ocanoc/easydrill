import math


class SeccionesAnulares:
    id = ""
    inicioPD = 0
    finPD = 0
    capacidad = 0
    diametroMayor = 0
    diametroMenor = 0
    volumen = 0
    longitudV = 0
    longitudD = 0
    deltaP = 0
    texterno = None
    titnerna = None
    vel_anular = 0
    indice_acarreo = 0

    def __init__(self, iniciopd, finpd, longmd, texterna, tinterna, dd):
        self.inicioPD = iniciopd
        self.finPD = finpd
        self.longitudD = longmd
        self.texterna = texterna
        self.titnerna = tinterna
        self.diametroMenor = float(tinterna.get_dext())
        self.diametroMayor = float(texterna.get_dint())
        self.capacidad = 0.5067 * ((self.diametroMayor ** 2) - (self.diametroMenor ** 2))
        self.volumen = self.capacidad * self.longitudD
        self.profundidad(dd)

    def profundidad(self, dd):
        inicio = self.inicioPD
        long = self.longitudD
        for x in dd:
            disponible = x.get_fin_pd()
            if inicio > x.get_inicio_pd() and self.finPD < x.get_fin_pd():
                self.longitudV = get_long_pv(self.longitudD, x)
                return 0
            if inicio > x.get_inicio_pd() and self.finPD > x.get_fin_pd():
                long -= disponible
                self.longitudV += get_long_pv(disponible, x)
                inicio += disponible
            else:
                self.longitudV += get_long_pv(long, x)
                return 0

    def __str__(self):
        return """\
    Diametro Mayor          \t{}
    Diametro menor          \t{}
    Inicio PD               \t{}
    Longitud PD             \t{}
    Fin PD                  \t{}
    Longitud PV             \t{}
    Capacidad               \t{}
    Volumen                 \t{}
    Caida de presion        \t{}""".format(self.diametroMayor, self.diametroMenor, self.inicioPD, self.longitudD,
                                           self.finPD, self.longitudV, self.capacidad, self.volumen, self.deltaP)

    def set_caida_presion(self, dp):
        self.deltaP = dp

    def get_longitud_d(self):
        return self.longitudD

    def get_longitud_v(self):
        return self.longitudV

    def get_dmayor(self):
        return self.diametroMayor

    def get_dmenor(self):
        return self.diametroMenor

    def get_velocidad(self):
        return self.vel_anular

    def set_velocidad(self, anular):
        self.vel_anular = anular

    def get_indice(self):
        return self.indice_acarreo

    def set_indice(self, acarreo):
        self.indice_acarreo = acarreo

    def get_caida_presion(self):
        return self.deltaP


def get_long_pv(long_pd, x):
    return long_pd * (math.cos(math.radians(x.get_angulo())))
