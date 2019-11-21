import math

from Modelo.Objetos.Direccional.Direccional import *

SECCION_VERTICAL = "Seccion Vertical"
INCREMENTO = "Incremento"
TANGENTE = "Tangente"
DECREMENTO = "Decremento"


class ControladorDireccional:
    @staticmethod
    def get_coseno(angulo):
        return math.cos(math.radians(angulo))

    @staticmethod
    def get_coseno_estaciones(angulo):
        return 30 * (math.cos(math.radians(angulo)))

    @staticmethod
    def tipo_j(kop, severidad, angulomax, profmax):
        angulo = 0
        profd = kop
        profv = kop
        otro = False
        long_estaciones = 30
        sc = Direccional(SECCION_VERTICAL, 0, kop, kop, 0, 0)
        lista_direccional = [sc]
        if (abs((angulomax / severidad) - round(angulomax / severidad))) > 0:
            otro = True
        esatciones = int(angulomax / severidad)
        for x in range(0, esatciones):
            angulo += severidad
            lista_direccional.append(Direccional(INCREMENTO, angulo, long_estaciones,
                                                 ControladorDireccional.get_coseno_estaciones(angulo), profd, profv))
            profd += long_estaciones
            profv += long_estaciones * ControladorDireccional.get_coseno(angulo)
        if otro:
            angulo -= severidad
            angulo += angulomax - angulo
            lista_direccional.append(Direccional(INCREMENTO, angulo, long_estaciones,
                                                 ControladorDireccional.get_coseno_estaciones(angulo), profd, profv))
            profv += long_estaciones * ControladorDireccional.get_coseno(angulo)
        lista_direccional.append(Direccional(TANGENTE, angulomax, profmax - profd,
                                             ((profmax - profd) * ControladorDireccional.get_coseno(angulo)),
                                             profd, profv))
        return lista_direccional

    @staticmethod
    def tipos(kop, severidad, angulomax, profmax, dop, dor):
        lista_direccional = ControladorDireccional.tipo_j(kop, severidad, angulomax, dop)
        ultima = lista_direccional.pop()
        lista_direccional.append(ultima)
        angulo = angulomax
        profd = dop
        profv = ultima.get_fin_pv()
        otro = False
        long_estaciones = 30
        if (round(angulomax / dor) - (angulomax / dor)) > 0:
            esatciones = int(angulomax / dor)
            otro = True
        else:
            esatciones = int(angulomax / dor)
        for x in range(0, esatciones):
            angulo -= dor
            lista_direccional.append(Direccional(DECREMENTO, angulo, long_estaciones,
                                                 ControladorDireccional.get_coseno_estaciones(angulo), profd, profv))
            profd += long_estaciones
            profv += long_estaciones * ControladorDireccional.get_coseno(angulo)

        if otro:
            angulo += severidad
            angulo -= angulomax - angulo
            lista_direccional.append(Direccional(DECREMENTO, angulo, long_estaciones,
                                                 ControladorDireccional.get_coseno_estaciones(angulo), profd, profv))
            profv += long_estaciones * ControladorDireccional.get_coseno(angulo)

        lista_direccional.append(Direccional(SECCION_VERTICAL, angulo, profmax - profd,
                                             ((profmax - profd) * ControladorDireccional.get_coseno(angulo)),
                                             profd, profv))
        return lista_direccional

    @staticmethod
    def tipov(profundidad):
        unica = Direccional(SECCION_VERTICAL, 0, profundidad, profundidad, 0, 0)
        lista_direcional = [unica]
        return lista_direcional
