import math


class LeyDePotenciasModificado:
    @staticmethod
    def set_ley_potencias_modificado(tuberia_interna, secciones, fluido, bomba):
        for x in tuberia_interna:
            x.set_dp(LeyDePotenciasModificado.interior(fluido, fluido.get_lec_fan_300(), fluido.get_lec_fan_600(),
                                                       bomba.get_gasto(), x.get_dint(), fluido.get_dl(),
                                                       x.get_long(), fluido.get_vp(), fluido.get_pc(), fluido.get_gel()))
        for x in secciones:
            x.set_dp(LeyDePotenciasModificado.espacio_anular(fluido, fluido.get_lec_fan_300(), fluido.get_lec_fan_600(),
                                                             bomba.get_gasto(), x.get_dmayor(), x.get_dmenor(),
                                                             fluido.get_dl(), x.get_long(), fluido.get_vp(),
                                                             fluido.get_pc(), fluido.get_gel()))

    @staticmethod
    def set_ley_potencias_modificado_superficial(pozo):
        LeyDePotenciasModificado.interior(pozo.get_fluido(), pozo.get_fluido().get_lec_fan_300(),
                                          pozo.get_fluido().get_lec_fan_600(), pozo.get_bombas().get_gasto(),
                                          pozo.get_superficial().get_diametro(), pozo.get_fluido().get_dl(),
                                          pozo.get_superficial().get_longitud(), pozo.get_fluido().get_vp(),
                                          pozo.get_fluido().get_pc(), pozo.get_fluido().get_gel())

    @staticmethod
    def interior(fluido, lec_fan_300, lec_fan_600, gasto, diametro_interior, densidad_lodo, longitud,
                 visco_plastica, punto_cedencia, gel):
        dimetro_cuadrado = diametro_interior ** 2
        if visco_plastica is 0 and punto_cedencia is 0:
            n = 3.32 * math.log10((lec_fan_600 + gel) / lec_fan_300)
            indice_consistencia = (lec_fan_600 + gel) / 1022
        else:
            n = 3.32 * math.log10(((2 * visco_plastica) + punto_cedencia + gel) /
                                  (visco_plastica + punto_cedencia + gel))
            indice_consistencia = (visco_plastica + punto_cedencia + gel) / math.pow(511, n)
        fluido.set_k(indice_consistencia)
        fluido.set_n(n)
        vel_flujo = 24.51 * gasto / dimetro_cuadrado
        factor_geometrico = (((3*n) + 1) / (4*n)) * 8.13 * n * math.pow(0.123, 1/n)
        rotacion_equivalente = 0.939 * factor_geometrico * vel_flujo / diametro_interior
        lec_fan_equivalente = gel + (indice_consistencia * math.pow(rotacion_equivalente, n))
        nre = densidad_lodo * (vel_flujo ** 2) / (2.474 * lec_fan_equivalente)
        nre_tl = 3470 - (1370 * n)
        nre_tt = 4270 - (1370 * n)
        a = (math.log10(n) + 3.93) / 50
        b = (1.75 - math.log10(n)) / 7
        if nre <= nre_tl:
            return lec_fan_equivalente * longitud / (1218.8 * diametro_interior)
        elif nre >= nre_tt:
            f = a / math.pow(nre, b)
            return (f * densidad_lodo * (vel_flujo ** 2) * longitud) / (48251 * diametro_interior)
        else:
            f = (16 / nre_tl) + (((nre - nre_tl) / 800) * ((a / math.pow(nre_tt, b)) - (16 / nre_tl)))
            return (f * densidad_lodo * (vel_flujo ** 2) * longitud) / (48251 * diametro_interior)

    @staticmethod
    def espacio_anular(fluido, lec_fan_300, lec_fan_600, gasto, diametro_mayor, diametro_menor, densidad_lodo,
                       longitud, visco_plastica, punto_cedencia, gel):
        dif_cuadrados = (diametro_mayor ** 2) - (diametro_menor ** 2)
        ea = diametro_mayor - diametro_menor
        if visco_plastica is 0 and punto_cedencia is 0:
            n = 3.32 * math.log10((lec_fan_600 + gel) / lec_fan_300)
            indice_consistencia = (lec_fan_600 + gel) / 1022
        else:
            n = 3.32 * math.log10(((2 * visco_plastica) + punto_cedencia + gel) /
                                  (visco_plastica + punto_cedencia + gel))
            indice_consistencia = (visco_plastica + punto_cedencia + gel) / math.pow(511, n)
        fluido.set_k(indice_consistencia)
        fluido.set_n(n)
        vel_flujo = 24.51 * gasto / dif_cuadrados
        alpha = diametro_menor / diametro_mayor
        x = 0.37 * pow(n, -0.14)
        c = 1 - (1 - math.pow((1 - (alpha ** x)), 1 / x))
        factor_geometrico = (((3 - c) * n)-1 / ((4 - c) * n)) * (1 + (c / 2)) * (8.13 * n * math.pow(0.123, 1/n))
        rotacion_equivalente = 0.939 * factor_geometrico * vel_flujo / ea
        lec_fan_equivalente = gel + (indice_consistencia * math.pow(rotacion_equivalente, n))
        nre = densidad_lodo * (vel_flujo ** 2) / (2.319 * lec_fan_equivalente)
        nre_tl = 3470 - (1370 * n)
        nre_tt = 4270 - (1370 * n)
        a = (math.log10(n) + 3.93) / 50
        b = (1.75 - math.log10(n)) / 7
        if nre <= nre_tl:
            return lec_fan_equivalente * longitud / (1218.8 * ea)
        elif nre >= nre_tt:
            f = a / math.pow(nre, b)
            return (f * densidad_lodo * (vel_flujo ** 2) * longitud) / (48251 * ea)
        else:
            f = (24 / nre_tl) + (((nre - nre_tl) / 800) * ((a / math.pow(nre_tt, b)) - (24 / nre_tl)))
            return (f * densidad_lodo * (vel_flujo ** 2) * longitud) / (48251 * ea)
