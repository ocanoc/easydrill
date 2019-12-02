from fractions import Fraction


class Convertidor:
    @staticmethod
    def fracc_to_dec(str):
        separador = " "
        if "/" in str:
            if " " in str:
                separado_por_espacios = str.split(separador)
                x = Fraction(separado_por_espacios[1])
                y = float(x)
                return float(separado_por_espacios[0]) + y
            else:
                x = Fraction(str)
                y = float(x)
                return y
        elif "." in str:
            return float(str)
        else:
            return float(str)
