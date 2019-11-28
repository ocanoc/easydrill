class ControladorBarrena:

    @staticmethod
    def set_parametros_hidraulicos(barrena, bomba, p, fluido):
        barrena.set_potencia_h(p * bomba.get_gasto() / 120.7)
        barrena.set_impacto_h(fluido.get_dl() * 8.345 * bomba.get_gasto() * barrena.get_vel_toberas() / 1930)

    @staticmethod
    def set_vel_toberas(barrena, bomba):
        barrena.set_velocidad_toberas(0.32 * bomba.get_gasto() / barrena.get_area_toberas())
