import math


class LeyDePotencias:
    @staticmethod
    def set_ley_potencias(tuberia_interna, secciones, fluido, bomba):
        for x in tuberia_interna:
            x.setdp(LeyDePotencias.interior(fluido, fluido.get_lec_fan_300(), fluido.get_lec_fan_600(),
                                            bomba.get_gasto(), x.get_dint(), fluido.get_dl(), x.get_long(),
                                            fluido.get_vp(), fluido.get_pc()))
        for x in secciones:
            x.setdp(LeyDePotencias.espacion_anular(fluido, fluido.get_lec_fan_300(), fluido.get_lec_fan_600(),
                                                   bomba.get_gasto(), x.get_dmayor(), x.get_dmenor(), fluido.get_dl(),
                                                   x.get_long(), fluido.get_vp(), fluido.get_pc()))

    @staticmethod
    def set_ley_potencias_modificado_superficial(pozo):
        LeyDePotencias.interior(pozo.get_fluido(), pozo.get_fluido().get_lec_fan_300(),
                                pozo.get_fluido().get_lec_fan_600(), pozo.get_bombas().get_gasto(),
                                pozo.get_superficial().get_diametro(), pozo.get_fluido().get_dl(),
                                pozo.get_superficial().get_longitud(), pozo.get_fluido().get_vp(),
                                pozo.get_fluido().get_pc())

    @staticmethod
    def interior(fluido, lec_fan_300, lec_fan_600, gasto, diametro_interior, densidad_lodo, longitud, visco_plastica,
                 punto_cedencia):
        dimetro_cuadrado = diametro_interior ** 2
        if visco_plastica is 0 and punto_cedencia is 0:
            n = 3.32 * math.log10(lec_fan_600 / lec_fan_300)
            indice_consistencia = lec_fan_600 / 1022
        else:
            n = 3.32 * math.log10(((2 * visco_plastica) + punto_cedencia) / (visco_plastica + punto_cedencia))
            indice_consistencia = (visco_plastica + punto_cedencia) / 511
        vel_flujo = 24.51 * gasto / dimetro_cuadrado
        nre = (densidad_lodo * (vel_flujo ** 2) / (2.319 * indice_consistencia)) * ((2.5 * diametro_interior * n) /
                                                                                    (vel_flujo * ((3 * n) + 1)))
        fluido.set_k(indice_consistencia)
        fluido.set_n(n)
        nre_tl = 3470 - (1370 * n)
        nre_tt = 4270 - (1370 * n)
        a = (math.log10(n) + 3.93) / 50
        b = (1.75 - math.log10(n)) / 7
        if nre <= nre_tl:
            return (indice_consistencia * longitud / (1300.5 * diametro_interior)) * \
                   math.pow(((((3 * n) + 1) * vel_flujo) / (2.5 * diametro_interior * n)), n)
        elif nre >= nre_tt:
            f = a / math.pow(nre, b)
            return (f * densidad_lodo * (vel_flujo ** 2) * longitud) / (48251 * diametro_interior)
        else:
            f = (16 / nre_tl) + (((nre - nre_tl) / 800) * ((a / math.pow(nre_tt, b)) - (16 / nre_tl)))
            return (f * densidad_lodo * (vel_flujo ** 2) * longitud) / (48251 * diametro_interior)

    @staticmethod
    def espacion_anular(fluido, lec_fan_300, lec_fan_600, gasto, diametro_mayor, diametro_menor, densidad_lodo,
                        longitud, visco_plastica, punto_cedencia):
        dif_cuadrados = (diametro_mayor ** 2) - (diametro_menor ** 2)
        ea = diametro_mayor - diametro_menor
        if visco_plastica is 0 and punto_cedencia is 0:
            n = 3.32 * math.log10(lec_fan_600 / lec_fan_300)
            indice_consistencia = lec_fan_600 / 1022
        else:
            n = 3.32 * math.log10(((2 * visco_plastica) + punto_cedencia) / (visco_plastica + punto_cedencia))
            indice_consistencia = (visco_plastica + punto_cedencia) / 511
        vel_flujo = 24.51 * gasto / dif_cuadrados
        nre = (densidad_lodo * (vel_flujo ** 2) / (1.65 * indice_consistencia)) * \
              ((1.25 * ea * n) / (vel_flujo * ((2 * n) + 1)))
        fluido.set_k(indice_consistencia)
        fluido.set_n(n)
        nre_tl = 3470 - (1370 * n)
        nre_tt = 4270 - (1370 * n)
        a = (math.log10(n) + 3.93) / 50
        b = (1.75 - math.log10(n)) / 7
        if nre <= nre_tl:
            return (indice_consistencia * longitud / (1300.5 * ea)) * \
                   math.pow(((((2 * n) + 1) * vel_flujo) / (1.25 * ea * n)), n)
        elif nre >= nre_tt:
            f = a / math.pow(nre, b)
            return (f * densidad_lodo * (vel_flujo ** 2) * longitud) / (48251 * ea)
        else:
            f = (24 / nre_tl) + (((nre - nre_tl) / 800) * ((a / math.pow(nre_tt, b)) - (24 / nre_tl)))
            return (f * densidad_lodo * (vel_flujo ** 2) * longitud) / (48251 * ea)
