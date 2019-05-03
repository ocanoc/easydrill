import sys
from win32api import GetSystemMetrics
from Vista.TrayectoriaDireccional.MenuTrayectoria import Trayectoria
from Vista.Fluidos.DatosFluidos import *
from Vista.Fluidos.MenuFluidos import *


class MainWindow (QMainWindow):
    seleccion = 0
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    pos = 0
    stop = False
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
    texto_encabezado.setScaledContents(True)
    texto_encabezado.setFixedWidth(250)
    texto_encabezado.setFixedHeight(50)
    trayectoria = Trayectoria()
    frame_trayectoria = trayectoria.get_frame()
    frame_menu_fluiods = QFrame()
    frame_menu_fluiods.setLayout(tipo_fluidos())
    frame_datos_fluidos = QFrame()
    frame_datos_fluidos.setLayout(datos_fluido())
    layout_btn = QHBoxLayout()
    layout_btn.addWidget(btn_cancelar)
    layout_btn.addWidget(btn_aceptar, Qt.StretchTile, Qt.AlignRight)
    layout_btn.addWidget(btn_regresar)
    layout_pantalla = QVBoxLayout()
    central_widget = QWidget()
    layout_pantalla.addSpacing(10)
    layout_pantalla.addWidget(texto_encabezado, Qt.AlignTop)
    layout_pantalla.addWidget(frame_trayectoria)
    layout_pantalla.addWidget(frame_datos_fluidos)
    layout_pantalla.addWidget(frame_menu_fluiods)
    layout_pantalla.addSpacing(10)
    layout_pantalla.addLayout(layout_btn)
    layout_pantalla.addSpacing(15)
    central_widget.setLayout(layout_pantalla)

    def __init__(self):
        super(MainWindow, self).__init__()
        fondo = QImage("Imagenes/Fondo.png")
        palette = QPalette()
        palette.setBrush(10, QBrush(fondo))  # 10 = Windowrole
        self.setPalette(palette)
        self.trayectoria.imagen_vertical.installEventFilter(self)
        self.trayectoria.imagen_tipo_s.installEventFilter(self)
        self.trayectoria.imagen_tipo_j.installEventFilter(self)
        self.trayectoria.imagen_horizontal.installEventFilter(self)
        width = 1000
        height = 600
        self.setWindowTitle("Easy Drill")
        self.setGeometry((GetSystemMetrics(0)-width)/2, (GetSystemMetrics(1)-height)/2, width, height)
        self.setWindowIcon(QIcon("Imagenes/Gota.png"))
        self.cambiar_encabezado()
        self.cambiar_central()
        self.setCentralWidget(self.central_widget)
        self.btn_aceptar.clicked.connect(self.aceptar)
        self.btn_regresar.clicked.connect(self.regresar)
        self.btn_cancelar.clicked.connect(self.cancelar)

    def cambiar_encabezado(self):
        if self.pos is 0:
            self.texto_encabezado.setPixmap(QPixmap("Imagenes/TextoTrayectoria.png"))
        if self.pos is 1:
            self.texto_encabezado.setPixmap(QPixmap("Imagenes/TextoModelo.png").scaledToHeight(50))
        if self.pos is 2:
            self.texto_encabezado.setPixmap(QPixmap("Imagenes/TextoHidraulica.png").scaledToHeight(50))

    def cambiar_central(self):
        if self.pos is 0:
            self.frame_trayectoria.show()
            self.frame_menu_fluiods.hide()
            self.frame_datos_fluidos.hide()
        if self.pos is 1:
            self.frame_trayectoria.hide()
            self.frame_menu_fluiods.show()
            self.frame_datos_fluidos.hide()
        if self.pos is 2:
            self.frame_trayectoria.hide()
            self.frame_menu_fluiods.hide()
            self.frame_datos_fluidos.show()

    @pyqtSlot()
    def regresar(self):
        if self.pos is 0:
            self.btn_regresar.hide()
            self.cambiar_encabezado()
            self.cambiar_central()
        elif self.pos is 1:
            self.pos = 0
            self.btn_regresar.hide()
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
        elif self.pos is 1:
            self.pos = 2
            self.cambiar_encabezado()
            self.cambiar_central()

    @pyqtSlot()
    def cancelar(self):
        pass

    def eventFilter(self, source, event):
        if event.type() == QEvent.Enter:
            self.cambiar_imagen(source, True)
            self.stop = True
            return True
        elif event.type() == QEvent.Leave:
            self.cambiar_imagen(source, False)
            self.stop = False

        elif event.type() == QEvent.MouseButtonPress:
            print("Holi")
        return False

    def cambiar_imagen(self, source, flag):
        if self.frame_trayectoria.show:
            self.trayectoria.cambiar_imagen(source,flag)




if __name__ == '__main__':
    w = MainWindow()
    w.setFixedSize(1000, 605)
    w.show()
    sys.exit(w.app.exec_())
