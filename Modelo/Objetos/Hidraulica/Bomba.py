class Bomba:
    diametro_camisa = 0
    longitud_carrera = 0
    eficiencia = 0
    gasto = 0
    p_bombeo = 0

    def __init__(self, gasto, p_bombeo):
        self.gasto = gasto
        self.p_bombeo = p_bombeo

    def set_gasto_bomba_triplex(self):
        self.gasto = (self.diametro_camisa ** 2) * self.longitud_carrera * self.eficiencia / 98

    def set_gasto(self, data):
        self.gasto = data

    def get_gasto(self):
        return self.gasto

    def set_camisa(self, camisa):
        self.diametro_camisa = camisa
        self.set_gasto_bomba_triplex()

    def get_diametro_camisa(self):
        return self.diametro_camisa

    def get_longitud_carrera(self):
        return self.longitud_carrera

    def get_eficiencia(self):
        return self.eficiencia

    def __str__(self):
        return """\
       Gasto            \t{}
       Presion bombeo   \t{}""".format(self.gasto, self.p_bombeo)
