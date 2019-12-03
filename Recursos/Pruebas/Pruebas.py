from Controlador.Hidraulica.Metodos.SmithTool import SmithTool
from Controlador.Tuberia.ControladorTuberia import ControladorTuberia
from ControladorDireccional import *
from ControladorSeccionesAnulares import *
from Modelo.Objetos.Hidraulica.Bomba import Bomba
from Modelo.Objetos.Hidraulica.Fluido import Fluido
from Modelo.Objetos.Tuberia.Exterior import *
from Modelo.Objetos.Tuberia.Interior import *

"""

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

for x in internas:
    print(x, "\n")

pip install pyqtgraph

dir = ControladorDireccional.tipo_j(1500, 1.5, 30, 5000)\
#dir = ControladorDireccional.tipos(500, 1.22, 45, 5000, 3500, 1.5)
Tuberia_uno = Interior(10, 9, 500, dir, None)
Tuberia_dos = Interior(8, 7, 800, dir, Tuberia_uno)
Tuberia_tres = Interior(5, 4, 1000, dir, Tuberia_dos)
TR1 = Exterior(30, 27, 400, dir, None)
TR2 = Exterior(25, 24, 800, dir, TR1)
TR3 = Exterior(18, 15, 800, dir, TR2)
Agujero = Exterior(10, 8, 300, dir, TR3)
internas = [Tuberia_uno, Tuberia_dos, Tuberia_tres]

externas = [TR1, TR2, TR3, Agujero]
lista_secciones = ControladorSecciones.creasecciones(externas, internas, dir)
"""
jota = ControladorDireccional.tipo_j(1000, 1.5, 30, 2500)
vertical = ControladorDireccional.tipos(1000, 1.5, 30, 3600, 2500, 1.5, 0)
for x in vertical:
    print(x, "\n")
tuberia1 = Interior(5, 4.276, 2000, jota, None)
tuberia2 = Interior(8, 2.875, 500, jota, tuberia1)
TR1 = Exterior(13.375, 12.565, 1300, jota, None)
Agujero = Exterior(12.25, 12.25, 1200, jota, TR1)
internas = [tuberia1, tuberia2]
externas = [TR1, Agujero]
ControladorTuberia.profundidad_vertical(externas, jota)
ControladorTuberia.profundidad_vertical(internas, jota)
lista_secciones = ControladorSecciones.creasecciones(externas, internas)
ControladorTuberia.profundidad_vertical(lista_secciones, jota)
fluido = Fluido(1.2, 15, 12)
fluido.set_gel(6)
bomba = Bomba(1000, 1)
SmithTool.set_smith_tool(internas, lista_secciones, fluido, bomba)
datos_equipo_sup = [3.826, 103.7]
equiposup = SmithTool.interior(fluido.get_vp(), datos_equipo_sup[0], bomba.get_gasto(),
                               datos_equipo_sup[1], fluido.get_dl(), )

for x in internas:
    print(x, "\n")
for x in lista_secciones:
    print(x, "\n")
