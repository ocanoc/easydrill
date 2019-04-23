import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from win32api import GetSystemMetrics
from Fluidos.MenuFluidos import *
from Fluidos.DatosFluidos import *

class MainWindow (QMainWindow):
    """docstring for Main Window."""
    def __init__(self):
        super(MainWindow, self).__init__()
        width = 800
        height = 600
        self.setWindowTitle("Easy Drill")
        self.setGeometry((GetSystemMetrics(0)-width)/2, (GetSystemMetrics(1)-height)/2,width,height)
        self.setWindowIcon(QIcon('petro.png'))
        self.setMaximumHeight(700)
        self.setMinimumHeight(600)
        #fluidos(self)
        #self.trayectoria()
        datos(self)


    def trayectoria (self):
        TextoTrayectoria = QLabel()
        TextoTrayectoria.setPixmap(QPixmap("TextoTrayectoria.png").scaledToHeight(50))
        Vertical = QLabel()
        Vertical.setPixmap(QPixmap("Vertical.png").scaledToHeight(60))
        ImagenVertical = QLabel()
        ImagenVertical.setPixmap(QPixmap("ImagenVertical.png").scaledToHeight(350))
        TipoJ = QLabel()
        TipoJ.setPixmap(QPixmap("TipoJ.png").scaledToHeight(60))
        ImagenTipoJ = QLabel()
        ImagenTipoJ.setPixmap(QPixmap("ImagenTipoJ.png").scaledToHeight(350))
        TipoS = QLabel()
        TipoS.setPixmap(QPixmap("TipoS.png").scaledToHeight(60))
        ImagenTipoS = QLabel()
        ImagenTipoS.setPixmap(QPixmap("ImagenTipoS.png").scaledToHeight(350))
        Horizontal = QLabel()
        Horizontal.setPixmap(QPixmap("Horizontal.png").scaledToHeight(60))
        ImagenHorizontal = QLabel()
        ImagenHorizontal.setPixmap(QPixmap("ImagenHorizontal.png").scaledToHeight(350))
        EasyDrillLogo = QLabel()
        EasyDrillLogo.setPixmap(QPixmap("EasyDrillLogo.png").scaledToHeight(30))
        BtnAceptar = QPushButton("Aceptar")
        BtnAceptar.setFixedHeight(30)
        BtnAceptar.setFixedWidth(100)
        BtnCancelar = QPushButton("Cancelar")
        BtnCancelar.setFixedHeight(30)
        BtnCancelar.setFixedWidth(100)
        BtnRegresar = QPushButton("Regresar")
        BtnRegresar.setFixedHeight(30)
        BtnRegresar.setFixedWidth(100)
        layoutTipoVertical = QVBoxLayout()
        layoutTipoVertical.addWidget(Vertical, Qt.StretchTile, Qt.AlignCenter)
        layoutTipoVertical.addWidget(ImagenVertical)
        layoutJ = QVBoxLayout()
        layoutJ.addWidget(TipoJ, Qt.StretchTile, Qt.AlignCenter)
        layoutJ.addWidget(ImagenTipoJ)
        layoutS = QVBoxLayout()
        layoutS.addWidget(TipoS, Qt.StretchTile, Qt.AlignCenter)
        layoutS.addWidget(ImagenTipoS)
        layoutHorizontal = QVBoxLayout()
        layoutHorizontal.addWidget(Horizontal, Qt.StretchTile, Qt.AlignCenter)
        layoutHorizontal.addWidget(ImagenHorizontal)
        layoutBtn = QHBoxLayout()
        layoutBtn.addWidget(BtnAceptar, Qt.StretchTile, Qt.AlignRight)
        layoutBtn.addWidget(BtnCancelar)
        layoutBtn.addWidget(BtnRegresar)
        layoutTipos = QHBoxLayout()
        layoutTipos.addLayout(layoutTipoVertical)
        layoutTipos.addLayout(layoutJ)
        layoutTipos.addLayout(layoutS)
        layoutTipos.addLayout(layoutHorizontal)
        layoutPantalla = QVBoxLayout()
        layoutPantalla.addWidget(EasyDrillLogo, Qt.StretchTile, Qt.AlignRight)
        layoutPantalla.addWidget(TextoTrayectoria)
        layoutPantalla.addLayout(layoutTipos)
        layoutPantalla.addSpacing(30)
        layoutPantalla.addLayout(layoutBtn)
        central_widget = QWidget()
        central_widget.setLayout(layoutPantalla)
        self.setCentralWidget(central_widget)






    def initUI (self):
        horizontal = QHBoxLayout()
        vertical = QVBoxLayout()
        btn1 = QPushButton("Nuevo")
        btn2 = QPushButton("Cargar")
        btn3 = QPushButton()
        btn1.setFont(QFont("Calibri(Cuerpo)", 15))
        btn2.setFont(QFont("Calibri(Cuerpo)", 15))
        btn3.setFont(QFont("Calibri(Cuerpo)", 15))
        btn3.setIcon(QIcon("BtnTuberias.png"))
        btn3.setIconSize(QSize(280,1800))
        btn1.setFixedHeight(40)
        btn1.setFixedWidth(280)
        btn2.setFixedHeight(40)
        btn3.setFixedHeight(40)
        central_widget = QWidget()
        vertical.addStretch()
        vertical.addWidget(btn1)
        vertical.addSpacing(10)
        vertical.addWidget(btn2)
        vertical.addSpacing(10)
        vertical.addWidget(btn3)
        vertical.addSpacing(10)
        vertical.addStretch()
        Logo = QLabel()
        Logo.setPixmap(QPixmap("EasyDrillLogo.png").scaledToHeight(90))
        Linea = QLabel()
        Linea.setPixmap(QPixmap("Linea.png").scaledToHeight(250))
        horizontal.addWidget(Logo)
        horizontal.addSpacing(8)
        horizontal.addWidget(Linea)
        horizontal.addSpacing(8)
        horizontal.addLayout(vertical)
        central_widget.setLayout(horizontal)
        self.setCentralWidget(central_widget)


if __name__ == '__main__':
    print("Width =", GetSystemMetrics(0))
    print("Height =", GetSystemMetrics(1))
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())


