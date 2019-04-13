def gasto_bomba_triplex(dc, lc, ef):
    return (dc ** 2) * lc * ef / 98


"""
Q = Gasto de la bomba [gal/emb]
DC = Diámetro de la camisa [pg]
LC = Longitud de la carrera [pg]
Ef = Eficiencia de la bomba, Adim.
"""


def factor_flotacion(dl):
    return 1 - (dl / 7.85)


"""
dl = Densidad del lodo [gr/cm3]
FF = Factor de flotación [adim]
7.85= Densidad de acero [gr/cm3]
"""
