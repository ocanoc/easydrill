class ConexionesSuperficiales:
    longitud_conexion_s = 0
    diametro_conexion_s = 0
    capacidad_conexion_s = 0
    volumen_conexion_s = 0
    dp_conexiones_s = 0

    def get_longitud(self):
        return self.longitud_conexion_s

    def set_longitud(self, l):
        self.longitud_conexion_s = l

    def get_diametro(self):
        return self.diametro_conexion_s

    def set_diametro(self, d):
        self.diametro_conexion_s = d

    def get_capacidad(self):
        return self.capacidad_conexion_s

    def set_capacidad(self, c):
        self.capacidad_conexion_s = c

    def get_volumen(self):
        return self.volumen_conexion_s

    def set_volumen(self, v):
        self.volumen_conexion_s = v

    def get_dp(self):
        return self.dp_conexiones_s

    def set_dp(self, dp):
        self.dp_conexiones_s = dp
