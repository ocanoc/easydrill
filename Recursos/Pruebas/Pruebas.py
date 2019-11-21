from Controlador.Tuberia.ControladorTuberia import ControladorTuberia
from ControladorDireccional import *
from ControladorSeccionesAnulares import *
from Modelo.Objetos.Tuberia.Exterior import *
from Modelo.Objetos.Tuberia.Interior import *

"""
vertical = ControladorDireccional.tipov(2200)

Tuberia_uno = Interior(5, 4.276, 2200, vertical, None)
TR1 = Exterior(13.375, 12.565, 780, vertical, None)
Agujero = Exterior(12.25, 12.25, 1420, vertical, TR1)
internas = [Tuberia_uno]
externas = [TR1, Agujero]
lista_secciones = ControladorSecciones.creasecciones(externas, internas, vertical)
f = Fluido(1.06, 12, 12)
b = Bomba(1, 1, 1)
b.set_gasto(700)

LeyDePotenciasModificado.set_ley_potencias_modificado(internas, lista_secciones, f, b)
#LeyDePotencias.set_ley_potencias(internas,lista_secciones, f, b)
#PlacticoBingham.set_plastico_bingham(internas, lista_secciones, f, b)
for x in lista_secciones:
    print(x, "\n")
print("")
print(Tuberia_dos)
print("")
print(Tuberia_tres)
# print(dir[-1])
for x in lista_secciones:
    print(x, "\n")



"""

# dir = ControladorDireccional.tipo_j(1500, 1.5, 30, 5000)\
dir = ControladorDireccional.tipos(500, 1.22, 45, 5000, 3500, 1.5)
Tuberia_uno = Interior(10, 9, 500, dir, None)
Tuberia_dos = Interior(8, 7, 800, dir, Tuberia_uno)
Tuberia_tres = Interior(5, 4, 1000, dir, Tuberia_dos)
TR1 = Exterior(30, 27, 400, dir, None)
TR2 = Exterior(25, 24, 800, dir, TR1)
TR3 = Exterior(18, 15, 800, dir, TR2)
Agujero = Exterior(10, 8, 300, dir, TR3)
internas = [Tuberia_uno, Tuberia_dos, Tuberia_tres]
ControladorTuberia.profundidad_vertical(internas, dir)
externas = [TR1, TR2, TR3, Agujero]
lista_secciones = ControladorSecciones.creasecciones(externas, internas, dir)





