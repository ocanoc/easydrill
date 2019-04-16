class PamarametosPerforacion:

    @staticmethod
    def inidice_limpieza():
        pass

    @staticmethod
    def dec(pozo):
        return (pozo.get_dp_anular() * 0.703 / pozo.get_profundidad()) + pozo.get_fluido().get_dl()
