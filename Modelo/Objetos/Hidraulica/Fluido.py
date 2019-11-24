class Fluido:
    densidad = 0
    p_cedencia = 0
    l_300 = 0
    l_600 = 0
    gel = 0
    visco_p = 0
    k = 0
    n = 0

    def __init__(self, densidad, visco_p, p_cedencia):
        self.densidad = densidad
        self.visco_p = visco_p
        self.p_cedencia = p_cedencia

    def get_dl(self):
        return self.densidad

    def get_pc(self):
        return self.p_cedencia

    def get_vp(self):
        return self.visco_p

    def get_lec_fan_300(self):
        return self.l_300

    def get_lec_fan_600(self):
        return self.l_600

    def get_gel(self):
        return self.gel

    def set_dl(self, data):
        self.densidad = data

    def set_pc(self, data):
        self.p_cedencia = data

    def set_vp(self, data):
        self.visco_p = data

    def set_lec_fan_300(self, data):
        self.l_300 = data

    def set_lec_fan_600(self, data):
        self.l_600 = data

    def set_gel(self, gel):
        self.gel = gel

    def set_k(self, data):
        self.k = data

    def set_n(self, data):
        self.n = data

    def get_visco_plastica(self):
        return self.visco_p

    def get_p_cedencia(self):
        return self.p_cedencia

    def get_k(self):
        return self.k

    def get_n(self, ):
        return self.n
