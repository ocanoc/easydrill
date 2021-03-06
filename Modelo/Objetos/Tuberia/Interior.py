from Tubo import *


class Interior (General):
    Tipo = ""
    caidaPresion = 0
    entr = False
    peso_unitario = 0
    peso_aire = 0
    peso_flotado = 0
    resistencia_tension = 0

    def set_resistension(self, rt):
        self.resistencia_tension = rt

    def set_peso_flotado(self, ff):
        self.peso_flotado = self.peso_aire*ff

    def set_peso_aire(self, pu):
        self.peso_unitario = pu
        self.peso_aire = pu * self.longMD

    def getentr(self):
        return self.entr

    def setentr(self):
        self.entr = True

    def setdp(self, dp):
        self.caidaPresion = dp

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
Caida de presion        \t{}""".format(self.dExt, self.dInt, self.inicioPD, self.longMD, self.finPD,
                                       self.longMV, self.capacidad, self.VolInterior, self.caidaPresion)
