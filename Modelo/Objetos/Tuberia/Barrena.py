class Barrena:
    Tipo = ""
    numero_toberas = 0
    diametro_toberas = 0
    area_toberas = 0
    cadida_de_presion = 0
    indice_limpieza = 0
    velocidad_toberas = 0
    impacto_h = 0
    potencia_h = 0

    def __init__(self, tfa):
        self.area_toberas = tfa

    def set_caida_presion(self, gasto, densidad_lodo):
        self.cadida_de_presion = (gasto ** 2) * densidad_lodo / (18511.7 * (self.area_toberas ** 2))

    def get_caidad_presion(self):
        return self.cadida_de_presion

    def set_indice_limpieza(self, il):
        self.indice_limpieza = il

    def get_indice_limpieza(self):
        return self.indice_limpieza

    def get_potencia_h(self):
        return self.potencia_h

    def get_imapcto_h(self):
        return self.impacto_h

    def get_vel_toberas(self):
        return self.velocidad_toberas

    def set_impacto_h(self, il):
        self.impacto_h = il

    def set_potencia_h(self, il):
        self.potencia_h = il

    def set_velocidad_toberas(self, data):
        self.velocidad_toberas = data

    def get_area_toberas(self):
        return self.area_toberas
