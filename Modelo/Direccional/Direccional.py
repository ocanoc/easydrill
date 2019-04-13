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

    def getTipo(self):
        return self.tipo

    def getAngulo(self):
        return self.angulo

    def getInicioPD(self):
        return self.InicioPD

    def getInicioPV(self):
        return self.InicioPV

    def getLV(self):
        return self.LV

    def getLD(self):
        return self.LD

    def getFinPD(self):
        return self.FinPD

    def getFinPV(self):
        return self.FinPV

    def getCoseno(angulo):
        return math.cos(math.radians(angulo))

    def getCosenoEstaciones(angulo):
        return 30 * (math.cos(math.radians(angulo)))

    def creaJ(kop, severidad, angulomax, profmax):
        angulo = 0
        profd = kop
        profv = kop
        otro = False
        longEstaciones = 30
        SECCIONVERTICAL = "Seccion Vertical"
        INCREMENTO = "Incremento"
        TANGENTE = "Tangente"
        DECREMENTO = "Decremento"
        sc = Direccional(SECCIONVERTICAL, 0, kop, kop, 0, 0)
        listaDireccional = [sc]
        if (abs((angulomax / severidad) - round(angulomax / severidad))) > 0:
            otro = True
        esatciones = int(angulomax / severidad)
        for x in range(0, esatciones):
            angulo += severidad
            listaDireccional.append(Direccional(INCREMENTO, angulo, longEstaciones,
                                                Direccional.getCosenoEstaciones(angulo), profd, profv))
            profd += longEstaciones
            profv += Direccional.getCoseno(angulo)
        if (otro):
            profv -= Direccional.getCoseno(angulo)
            angulo -= severidad
            angulo += angulomax - angulo
            profv += Direccional.getCoseno(angulo)
            listaDireccional.append(Direccional(INCREMENTO, angulo, longEstaciones,
                                                Direccional.getCosenoEstaciones(angulo), profd, profv))
            profv += Direccional.getCoseno(angulo)
        listaDireccional.append(Direccional(TANGENTE, angulomax, profmax - profd,
                                            ((profmax - profd) * Direccional.getCoseno(angulo)), profd, profv))

        return listaDireccional

    def creaS(kop, severidad, angulomax, profmax, dop, dor):
        listaDireccional = Direccional.creaJ(kop, severidad, angulomax, dop)
        ultima = listaDireccional.pop()
        listaDireccional.append(ultima)
        angulo = angulomax
        profd = dop
        profv = ultima.getFinPV()
        otro = False
        longEstaciones = 30
        SECCIONVERTICAL = "Seccion Vertical"
        INCREMENTO = "Incremento"
        TANGENTE = "Tangente"
        DECREMENTO = "Decremento"
        print(angulomax / dor)
        if (round(angulomax / dor) - (angulomax / dor)) > 0:
            esatciones = int(angulomax / dor)
            otro = True
        else:
            esatciones = int(angulomax / dor)
        for x in range(0, esatciones):
            angulo -= dor
            listaDireccional.append(Direccional(DECREMENTO, angulo, longEstaciones,
                                                Direccional.getCosenoEstaciones(angulo), profd, profv))
            profd += longEstaciones
            profv += Direccional.getCoseno(angulo)

        if otro:
            profv -= Direccional.getCoseno(angulo)
            angulo += severidad
            angulo -= angulomax - angulo
            profv += Direccional.getCoseno(angulo)
            listaDireccional.append(Direccional(DECREMENTO, angulo, longEstaciones,
                                                Direccional.getCosenoEstaciones(angulo), profd, profv))
            profv += Direccional.getCoseno(angulo)

        listaDireccional.append(Direccional(SECCIONVERTICAL, angulo, profmax -
                                            profd, ((profmax - profd) * Direccional.getCoseno(angulo)), profd, profv))
        return listaDireccional
