from tkinter import *
from PyQt5 import *

class Galleta():
    chocolate = False
    def __init__(self, sabor= None, forma = None):
        self.sabor = sabor
        self.forma = forma
        if sabor is not None and forma is not None:
            print("se acaba de crear una galleta {}  y {}".format (sabor , forma))
    def chocolatear(self):
        self.chocolate = True
        print ("hola")
    def tiene_chocolalte (self):
        if(self.chocolate):
            print("soy una galleta de chocolate")
        else:
            print("no tengo chocolate")
una_galleta = Galleta()
otra_galleta = Galleta()
g = Galleta()
otra_galleta.tiene_chocolalte()
g.tiene_chocolalte()
#panel
root = Tk ()
root.title ("Puto Jordan")
root.resizable(1,1)

#frame
frame = Frame (root, width = 480, height = 320 )
frame.pack(anchor = "w", fill = 'both', expand = 1)
frame.config (cursor = "pirate", bg = "lightblue", bd = 25, relief = "sunken" )
root.config (cursor = "man", bg = "blue", bd = 15, relief = "ridge" )
#componenetes
Label (frame, text= "Puto Jordan").pack(side = "left")
Label (frame, text= "Puto Jordanx2 pero en verde", bg = "green").pack()
Label (frame, text= "Puto Jordanx3").pack()
Label (frame, text= "Puto Jordanx4").pack(side = "right")
root.mainloop()
