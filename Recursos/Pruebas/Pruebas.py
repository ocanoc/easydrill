from ControladorDireccional import *
from Modelo.Objetos.Tuberia.Interior import *
from Modelo.Objetos.Tuberia.Exterior import *
from ControladorSeccionesAnulares import *







dir = ControladorDireccional.tipo_j(1500, 1.5, 30, 5000)
Tuberia_uno = Interior(10, 9, 500, dir, None)
Tuberia_dos = Interior(8, 7, 800, dir, Tuberia_uno)
Tuberia_tres = Interior(5, 4, 1000, dir, Tuberia_dos)
TR1 = Exterior(30, 27, 400, dir, None)
TR2 = Exterior(25, 24, 800, dir, TR1)
TR3 = Exterior(18, 15, 800, dir, TR2)
Agujero = Exterior(10, 8, 300, dir, TR3)
internas = [Tuberia_uno, Tuberia_dos, Tuberia_tres]
externas = [TR1, TR2, TR3, Agujero]
lista_secciones = creasecciones(externas, internas, dir)






"""print("")
print(Tuberia_dos)
print("")
print(Tuberia_tres)
# print(dir[-1])
#dir2 = Direccional.creaS(500,1.22,45,5000,3500,1.5)"""
for x in lista_secciones:
    print(x, "\n")
