from Tubo import *


class Interior (General):
    caidaPresion = 0
    entr = False
    peso_unitario = 0
    peso_aire = 0
    peso_flotado = 0
    resistencia_tension = 0
    vel_interior = 0

    def set_resistension(self, rt):
        self.resistencia_tension = rt

    def set_peso_flotado(self, ff):
        self.peso_flotado = self.peso_aire*ff

    def set_peso_aire(self, pu):
        self.peso_unitario = pu
        self.peso_aire = pu * self.long_md

    def getentr(self):
        return self.entr

    def setentr(self):
        self.entr = True

    def set_dp(self, dp):
        self.caidaPresion = dp

    def get_dp(self):
        return self.caidaPresion

    def set_vel_interior(self, data):
        self.vel_interior = data

    def get_vel_interior(self):
        return self.vel_interior

    def __str__(self):
        return """\
Diametro exterior       \t{}
Diametro interior      \t{}
Inicio PD               \t{}
Longitud PD             \t{}
Fin PD                  \t{}
Longitud PV             \t{}
Capacidad               \t{}
Volumen                 \t{}
Caida de presion        \t{}""".format(self.d_ext, self.d_int, self.inicio_pd, self.long_md, self.fin_pd,
                                       self.long_mv, self.capacidad, self.vol_interior, self.caidaPresion)
