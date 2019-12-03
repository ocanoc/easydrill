import math


class SmithTool:
    @staticmethod
    def set_smith_tool(tuberia_interna, secciones, fluido, bomba):
        for x in tuberia_interna:
            x.set_dp(SmithTool.interior(fluido.get_vp(), x.get_dint(), bomba.get_gasto(),
                                        x.get_long(), fluido.get_dl()))
        for x in secciones:
            x.set_dp(SmithTool.espacion_anular(fluido.get_vp(), x.get_dmayor(), x.get_dmenor(), bomba.get_gasto(),
                                               x.get_long(), fluido.get_dl()))

    @staticmethod
    def interior(viscocidad_plastica, diametro_interior, gasto, longitud, densidad_lodo):
        return (math.pow(viscocidad_plastica, 0.18) * math.pow(gasto, 1.82) * math.pow(densidad_lodo, 0.82) * longitud / \
                (700.3 * math.pow(diametro_interior, 4.82))) / 14.22

    @staticmethod
    def espacion_anular(viscocidad_plastica, diametro_mayor, diametro_menor, gasto, longitud, densidad_lodo):
        return (math.pow(viscocidad_plastica, 0.18) * math.pow(gasto, 1.82) * \
                math.pow(densidad_lodo, 0.82) * longitud / (700.3 * math.pow((diametro_mayor - diametro_menor), 3) *
                                                            math.pow((diametro_mayor + diametro_menor), 1.82))) / 14.22
