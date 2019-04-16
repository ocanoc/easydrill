class Pozo:
    profundidad_total = 0
    diseio_direccional = None
    fluido = None
    arreglo_trs = None
    arreglo_sarta = None
    secciones_anulares = None
    equipo_superficial = None
    bombas = None
    dp_anular = 0
    dp_interior = 0

    def set_dp_anular(self):
        for x in self.secciones_anulares:
            self.dp_anular += x.get_caida_presion()

    def get_dp_anular(self):
        return self.dp_anular

    def get_profundidad(self):
        return self.profundidad_total

    def set_profundidad(self, p):
        self.profundidad_total = p

    def get_direccional(self):
        return self.diseio_direccional

    def set_direccional(self, d):
        self.diseio_direccional = d

    def get_fluido(self):
        return self.fluido

    def set_fluido(self, f):
        self.fluido = f

    def get_trs(self):
        return self.arreglo_trs

    def set_trs(self, trs):
        self.arreglo_trs = trs

    def get_sarta(self):
        return self.arreglo_sarta

    def set_sarta(self, s):
        self.arreglo_sarta = s

    def get_anualres(self):
        return self.secciones_anulares

    def set_anulares(self, a):
        self.secciones_anulares = a

    def get_superficial(self):
        return self.equipo_superficial

    def set_superficial(self, equipo):
        self.equipo_superficial = equipo

    def get_bombas(self):
        return self.bombas

    def set_bombas(self, b):
        self.bombas = b
