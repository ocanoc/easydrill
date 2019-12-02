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
    caida_presion = 0
    texterno = None
    titnerna = None
    vel_anular = 0
    indice_acarreo = 0
    dec = 0
    fin_pv = 0
    inicio_pv = 0

    def __init__(self, iniciopd, finpd, longmd, texterna, tinterna):
        self.inicioPD = iniciopd
        self.finPD = finpd
        self.longitudD = longmd
        self.texterna = texterna
        self.titnerna = tinterna
        self.diametroMenor = float(tinterna.get_dext())
        self.diametroMayor = float(texterna.get_dint())
        self.capacidad = 0.5067 * ((self.diametroMayor ** 2) - (self.diametroMenor ** 2))
        self.volumen = self.capacidad * self.longitudD
        self.deltaP = 0

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
    Caida de presion        \t{}
    Indice acarreo          \t{}
    Velocidad Anular        \t{}
    dec                     \t{}
    """.format(self.diametroMayor, self.diametroMenor, self.inicioPD, self.longitudD,
               self.finPD, self.longitudV, self.capacidad, self.volumen, self.deltaP,
               self.indice_acarreo, self.vel_anular, self.dec)

    def set_caida_presion(self, caida_presion):
        self.caida_presion = caida_presion

    def get_longitudD(self):
        return self.longitudD

    def get_long(self):
        return self.longitudV

    def get_dmayor(self):
        return self.diametroMayor

    def get_dmenor(self):
        return self.diametroMenor

    def get_vel_anular(self):
        return self.vel_anular

    def set_vel_anular(self, anular):
        self.vel_anular = anular

    def get_indice_acarreo(self):
        return self.indice_acarreo

    def set_indice_acarreo(self, acarreo):
        self.indice_acarreo = acarreo

    def get_dp(self):
        return self.deltaP

    def set_dp(self, dp):
        self.deltaP = dp

    def get_fin_pd(self):
        return self.finPD

    def get_inicio_pd(self):
        return self.inicioPD

    def get_dec(self):
        return self.dec

    def set_dec(self, data):
        self.dec = data

    def set_fin_pv(self, data):
        self.fin_pv = data

    def get_fin_pv(self):
        return self.fin_pv

    def get_inicio_pv(self):
        return self.inicio_pv

    def set_inicio_pv(self, data):
        self.inicio_pv = data

    def set_lv(self):
        self.longitudV = self.fin_pv - self.inicio_pv
