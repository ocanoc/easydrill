import math


def set_smith_tool(tuberia_interna, secciones, fluido, bomba):
    for x in tuberia_interna:
        x.setdp(smith_tool_int(fluido.get_vp(), x.getDint(), bomba.get_gasto(),
                               x.getLong(), fluido.get_dl()))
    for x in secciones:
        x.setdp(smit_tool_ea(fluido.get_vp(), x.get_dmayor(), x.get_dmenor(), bomba.get_gasto(),
                             x.getLong(), fluido.get_dl()))


def smith_tool_int(viscocidad_plastica, diametro_interior, gasto, longitud, densidad_lodo):
    return (viscocidad_plastica ** 0.18) * (gasto ** 0.82) * (densidad_lodo ** 1.82) * longitud / \
           (700.3 * (diametro_interior ** 4.82))


def smit_tool_ea(viscocidad_plastica, diametro_mayor, diametro_menor, gasto, longitud, densidad_lodo):
    return (viscocidad_plastica ** 0.18) * (gasto ** 0.82) * (densidad_lodo ** 1.82) * longitud / \
           (700.3 * math.pow((diametro_menor - diametro_menor), 3) * math.pow((diametro_mayor + diametro_menor), 1.82))
