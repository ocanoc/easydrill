import math


class PlacticoBingham:
    @staticmethod
    def set_plastico_bingham(tuberia_interna, secciones, fluido, bomba):
        for x in tuberia_interna:
            x.set_dp(PlacticoBingham.interior(bomba.get_gasto(), x.get_dint(), fluido.get_dl(),
                                              x.get_long(), fluido.get_pc(), fluido.get_vp()))

        for x in secciones:
            x.set_dp(PlacticoBingham.espacio_anular(bomba.get_gasto(), x.get_dmayor(), x.get_dmenor(), fluido.get_dl(),
                                                    x.get_long(), fluido.get_pc(), fluido.get_vp()))

    @staticmethod
    def set_ley_potencias_modificado_superficial(pozo):
        PlacticoBingham.interior(pozo.get_bombas().get_gasto(), pozo.get_superficial().get_diametro(),
                                 pozo.get_fluido().get_dl(), pozo.get_superficial().get_longiotud(),
                                 pozo.get_fluido().get_pc(),
                                 pozo.get_fluido().get_vp())

    @staticmethod
    def interior(gasto, diametro_interior, densidad_lodo, longitud, punto_cedencia, visc_plastica):
        dimetro_cuadrado = diametro_interior ** 2
        vel_flujo = 24.51 * gasto / dimetro_cuadrado

        vel_critica = ((7.75 * visc_plastica) + 7.75 * math.sqrt((visc_plastica ** 2) +
                                                                 (109.83 * punto_cedencia * dimetro_cuadrado
                                                                  * densidad_lodo))) /\
                      (densidad_lodo * diametro_interior)

        if vel_flujo < vel_critica:
            """Laminar"""
            return ((visc_plastica * longitud * vel_flujo) /
                    (389081 * dimetro_cuadrado)) + ((punto_cedencia * longitud) /
                                                    (913 * diametro_interior))
        else:
            nre = 129 * diametro_interior * vel_flujo * densidad_lodo / visc_plastica
            f = 0.079 / math.pow(nre, 0.25)
            return (f * densidad_lodo * (vel_flujo ** 2) * longitud) / (48251 * diametro_interior)

    @staticmethod
    def espacio_anular(gasto, diametro_mayor, diametro_menor, densidad_lodo, longitud, punto_cedencia, visc_plastica):
        dif_cuadrados = (diametro_mayor ** 2) - (diametro_menor ** 2)
        ea = diametro_mayor - diametro_menor
        vel_flujo = 24.51 * gasto / dif_cuadrados

        vel_critica = ((7.75 * visc_plastica) +
                       7.75 * math.sqrt((visc_plastica ** 2) + (82.37 * punto_cedencia * dif_cuadrados
                                                                * densidad_lodo))) / (densidad_lodo * ea)

        if vel_flujo < vel_critica:

            """Laminar"""

            return ((visc_plastica * longitud * vel_flujo) / (259387 * (ea ** 2))) + ((punto_cedencia * longitud) /
                                                                                      (812.6 * ea))
        else:
            nre = 129 * ea * vel_flujo * densidad_lodo / visc_plastica
            f = 0.0079 / math.pow(nre, 0.25)

            return (f * densidad_lodo * (vel_flujo ** 2) * longitud) / (48251 * ea)
