class ControladorBarrena:

    @staticmethod
    def set_parametros_hidraulicos(barrena, bomba, p, fluido):
        barrena.set_potencia_h(p * bomba.get_gasto() / 1714)
        barrena.set_impacto_h(0.000516 * fluido.get_dl() * bomba.get_gasto() * barrena.get_vel_toberas())

    @staticmethod
    def set_vel_toberas(barrena, bomba):
        barrena.set_velocidad_toberas(0.32 * bomba.get_gasto() / barrena.get_area_toberas())
