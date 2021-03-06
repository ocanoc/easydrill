from Tubo import *


class Barrena(General):
    Tipo = ""
    numero_toberas = 0
    diametro_toberas = 0
    area_toberas = 0
    cadida_de_presion = 0
    indice_limpieza = 0

    def set_toberas(self, numero, diametro):
        sumatoria = 0
        self.numero_toberas = numero
        for x in range(1, numero):
            sumatoria += (diametro ** 2)
        self.area_toberas = sumatoria / 1303.8

    def set_caida_presion(self, gasto, densidad_lodo):
        self.cadida_de_presion = (gasto ** 2) * densidad_lodo / (18511.7 * (self.area_toberas ** 2))

    def get_caidad_presion(self):
        return self.cadida_de_presion

    def set_indice_limpieza(self, il):
        self.indice_limpieza = il

    def get_indice_limpieza(self):
        return self.indice_limpieza
