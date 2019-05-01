import sys
from win32api import GetSystemMetrics
from Vista.TrayectoriaDireccional.MenuTrayectoria import *
from Vista.Fluidos.DatosFluidos import *
from Vista.Fluidos.MenuFluidos import *


class MainWindow (QMainWindow):
    app = QApplication(sys.argv)
    pos = 0
    btn_aceptar = QPushButton("Aceptar")
    btn_aceptar.setFixedHeight(30)
    btn_aceptar.setFixedWidth(100)
    btn_cancelar = QPushButton("Cancelar")
    btn_cancelar.setFixedHeight(30)
    btn_cancelar.setFixedWidth(100)
    btn_regresar = QPushButton("Regresar")
    btn_regresar.setFixedHeight(30)
    btn_regresar.setFixedWidth(100)
    btn_regresar.hide()
    texto_encabezado = QLabel()
    layout_trayectoria = trayectoria()
    layout_menu_fluiods = tipo_fluidos()
    layout_datos_fluiods = datos_fluido()
    easy_drill_logo = QLabel()
    easy_drill_logo.setPixmap(QPixmap("Imagenes/EasyDrllLogo.png").scaledToHeight(30))
    layout_pantalla = QVBoxLayout()
    layout_pantalla.addWidget(easy_drill_logo, Qt.StretchTile, Qt.AlignRight)
    layout_pantalla.addWidget(texto_encabezado)
    layout_btn = QHBoxLayout()
    layout_btn.addWidget(btn_aceptar, Qt.StretchTile, Qt.AlignRight)
    layout_btn.addWidget(btn_cancelar)
    layout_btn.addWidget(btn_regresar)
    layout_pantalla = QVBoxLayout()
    central_widget = QWidget()


    def __init__(self):
        super(MainWindow, self).__init__()
        width = 800
        height = 600
        self.setWindowTitle("Easy Drill")
        self.setGeometry((GetSystemMetrics(0)-width)/2, (GetSystemMetrics(1)-height)/2, width, height)
        self.setWindowIcon(QIcon("Imagenes/EasyDrllLogo.png"))
        self.setMaximumHeight(800)
        self.setMinimumHeight(600)
        self.cambiar_encabezado()
        self.limpiar()
        self.layout_pantalla.addLayout(self.layout_trayectoria)
        self.agregarbototnes()
        self.btn_aceptar.clicked.connect(self.aceptar)
        self.btn_regresar.clicked.connect(self.regresar)

    def cambiar_encabezado(self):
        print(self.pos)
        if self.pos is 0:
            self.texto_encabezado.setPixmap(QPixmap("Imagenes/TextoTrayectoria.png").scaledToHeight(50))
        if self.pos is 1:
            self.texto_encabezado.setPixmap(QPixmap("Imagenes/TextoModelo.png").scaledToHeight(50))
        if self.pos is 2:
            self.texto_encabezado.setPixmap(QPixmap("Imagenes/TextoHidraulica.png").scaledToHeight(50))

    def cambiar_central(self):
        print(self.pos)
        if self.pos is 0:
            self.layout_pantalla.insertLayout(2, self.layout_trayectoria)
        if self.pos is 1:
            self.layout_pantalla.insertLayout(2, self.layout_menu_fluiods)
        if self.pos is 2:
            self.layout_pantalla.insertLayout(2, self.layout_datos_fluiods)



    def limpiar(self):
        self.layout_pantalla = QVBoxLayout()
        self.layout_pantalla.addWidget(self.easy_drill_logo, Qt.StretchTile, Qt.AlignRight)
        self.layout_pantalla.addWidget(self.texto_encabezado)
        self.layout_btn = QHBoxLayout()
        self.layout_btn.addWidget(self.btn_aceptar, Qt.StretchTile, Qt.AlignRight)
        self.layout_btn.addWidget(self.btn_cancelar)
        self.layout_btn.addWidget(self.btn_regresar)

    @pyqtSlot()
    def agregarbototnes(self):
        self.layout_pantalla.addSpacing(20)
        self.layout_pantalla.removeItem(self.layout_btn)
        self.layout_pantalla.addLayout(self.layout_btn)
        self.layout_pantalla.addSpacing(20)
        self.central_widget = QWidget()
        self.central_widget.setLayout(self.layout_pantalla)
        self.setCentralWidget(self.central_widget)


    @pyqtSlot()
    def regresar(self):
        if self.pos is 0:
            self.btn_regresar.hide()
        elif self.pos is 1:
            self.pos = 0
            self.cambiar_encabezado()
            self.cambiar_central()
        elif self.pos is 2:
            self.pos = 1
            self.cambiar_encabezado()
            self.cambiar_central()
    @pyqtSlot()
    def aceptar(self):
        if self.pos is 0:
            self.pos = 1
            self.btn_regresar.show()
            self.cambiar_encabezado()
            self.cambiar_central()
            self.update()
        elif self.pos is 1:
            self.pos = 2
            self.cambiar_encabezado()
            self.cambiar_central()
            self.update()



if __name__ == '__main__':
    w = MainWindow()
    w.show()
    sys.exit(w.app.exec_())
