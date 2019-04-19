import math
class Tuberia ():
  DExt = 0
  DInt = 0
  longitud = 0
  def __init__(self,D,d,l):
     self.DExt = D
     self.DInt = d
     self.longitud = l
     print("Tuberia generica")
     if(isinstance(self,TInterna)):
        self.CInterior = 0.5067*(self.DInt**2)
        self.VolInterior = self.CInterior*self.longitud
        print(self. CInterior)
        print(self.VolInterior)
     if(isinstance(self, TExterior)):
        print("Soy de revestimiento")

  def __del__(self):
      print("bais")

class TExterior (Tuberia):
    Tipo=""
    BocaL = False
    CAnular = 0
    VolAnular = 0
    tinterior =""
    def Volumen (self):
        self.CAnular = 0.5067*(self.DExt**2 - self.tinterior.DExt**2)
        print (self.CAnular)
    def Interna (self,ti):
        self.tinterior=ti
        self.Volumen()

class TInterna (Tuberia):
        Tipo = ""
        VolInterior = 0
        CInterior = 0
class Direccional():
    InicioPD = 0
    InicioPV = 0
    LD = 0
    Longitud = 0
    LV = 0
    angulo = 0
    tipo = ""
    def __init__(self,tipo,angulo,longitdMD, longitdMV,INPD,INPV):
        self.tipo = tipo
        self.angulo = angulo
        self.InicioPD = INPD
        self.InicioPV = INPV
        self.LV = longitdMV
        self.LD = longitdMD
    def __str__ (self):
        return """\
Tipo\t{}
Profundidad desarrollada\t{}
longitud desarrollada\t{}
Longitud vertical\t{}
Profundidad vertical\t{}
Angulo \t{}""".format(self.tipo,self.InicioPD,self.LD,self.LV,self.InicioPV,self.angulo)

class seccion ():
    tipo = ""
    Interna = None
    Externa = None
    inicioMV = 0
    inicioMD =  0
    def __init__ (self,tipo):
        self.tipo = tipo
    def addInterna(i):
        self.Interna = i
    def addExterna(e):
        self.Externa = e

t = TInterna(5,4.5,10)
T = TExterior(10,9.5,50)
T.Interna(t)
del(t)
def creaJ(kop, severidad, angulomax, profmax):
    angulo = severidad
    profd = kop
    profv = kop
    otro = False
    sc = Direccional("Seccion vertical",0,kop,kop,0,0)
    listaDireccional = [sc]
    print(angulomax%severidad )
    if(angulomax%severidad == 0):

        pasos=int(angulomax/severidad)
    else:
        pasos=int(angulomax/severidad)
        otro = True
    for x in range(0,pasos):
        listaDireccional.append(Direccional("Curva",angulo,30,30*math.cos(math.radians(angulo)),profd,profv))
        angulo += severidad
        profd+=30
        profv += 30*math.cos(math.radians(angulo))
    if(otro):
        print("entre")
        listaDireccional.append(Direccional("Curva",angulomax-angulo,30,30*math.cos(math.radians(angulomax-angulo)),profd,profv))
        profd+=30
        profv += 30*((math.cos(math.radians(angulomax-angulo))))
    listaDireccional.append(Direccional("Tangente",angulomax,profmax-profd,(profmax-profd)*math.cos(math.radians(angulomax-angulo)),profd,profv))
    return listaDireccional
dir = creaJ(1500,1.2,30,5000)
for x in dir:
    print(x,"\n")
