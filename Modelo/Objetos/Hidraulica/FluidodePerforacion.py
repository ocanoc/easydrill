class Fluido:
    densidad = 0
    viscocidad_plastica = 0
    lec_fan_600 = 0
    lec_fan_300 = 0
    gel = 0
    punto_cendecia = 0
    factor_flotacion = 0
    n = 0
    k = 0

    def __init__(self, densidad, vp, lf6, lf3, pc):
        self.factor_flotacion = 1 - (densidad / 7.85)
        self.densidad = densidad
        self.lec_fan_600 = lf6
        self.lec_fan_300 = lf3
        if vp is 0:
            self.viscocidad_plastica = lf6 - lf3
        else:
            self.viscocidad_plastica = vp
        if pc is 0:
            self.punto_cendecia = lf3 - self.viscocidad_plastica
        else:
            self.punto_cendecia = pc

    def get_densidad(self):
        return self.densidad

    def get_punto_cedencia(self):
        return self.punto_cendecia

    def get_viscocidad_plastica(self):
        return self.viscocidad_plastica

    def get_lec_fan_300(self):
        return self.lec_fan_300

    def get_lec_fan_600(self):
        return self.lec_fan_600

    def get_gel(self):
        return self.gel

    def get_factor_flotacion(self):
        return self.factor_flotacion

    def get_k(self):
        return self.k

    def set_k(self, k):
        self.k = k

    def get_n(self):
        return self.n

    def set_n(self, n):
        self.n = n
