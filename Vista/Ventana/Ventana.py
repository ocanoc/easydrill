from win32api import GetSystemMetrics

from DatosTrayectoria.DatosTrayectoria import *
from Fluidos.DatosFluidos.DatosFluidos import *
from Fluidos.MenuFluidos import *
from TrayectoriaDireccional.MenuTrayectoria import Trayectoria


# noinspection PyArgumentList
class MainWindow (QMainWindow):
    seleccion = 0
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    pos = 0
    stop = False
    btn_aceptar = QPushButton("Aceptar")
    btn_aceptar.setFixedSize(100, 30)
    btn_cancelar = QPushButton("Cancelar")
    btn_cancelar.setFixedSize(100, 30)
    btn_regresar = QPushButton("Regresar")
    btn_regresar.setFixedSize(100, 30)
    btn_regresar.hide()
    trayectoria = Trayectoria()
    frame_trayectoria = trayectoria.get_frame()
    frame_trayectoria.hide()
    DatosTrayectoria = DatosTrayectoria()
    frame_datos_trayectoria = DatosTrayectoria.get_frame()
    frame_datos_trayectoria.hide()
    DatosFluidos = DatosFluidos()
    frame_datos_fluidos = DatosFluidos.get_frame()
    frame_datos_fluidos.hide()
    layout_btn = QHBoxLayout()
    layout_btn.addSpacing(50)
    layout_btn.addWidget(btn_cancelar, 1, Qt.AlignLeft)
    layout_btn.addWidget(btn_regresar, 1)
    layout_btn.addSpacing(20)
    layout_btn.addWidget(btn_aceptar, 1)
    layout_btn.addSpacing(50)
    layout_pantalla = QVBoxLayout()
    central_widget = QWidget()
    layout_pantalla.addWidget(frame_trayectoria)
    layout_pantalla.addWidget(frame_datos_trayectoria)
    layout_pantalla.addWidget(frame_datos_fluidos)
    layout_pantalla.addLayout(layout_btn)
    layout_pantalla.addSpacing(25)
    central_widget.setLayout(layout_pantalla)
    error_dialog = QErrorMessage()



    def __init__(self):
        super(MainWindow, self).__init__()
        width = 1000
        height = 600
        palette = QPalette()
        palette.setBrush(10, QBrush(QImage("Imagenes/Fondo.png")))
        self.setPalette(palette)
        self.trayectoria.imagen_vertical.installEventFilter(self)
        self.trayectoria.imagen_tipo_s.installEventFilter(self)
        self.trayectoria.imagen_tipo_j.installEventFilter(self)
        self.trayectoria.imagen_horizontal.installEventFilter(self)
        self.DatosFluidos.tipo_datos.installEventFilter(self)
        self.DatosFluidos.MenuFluidos.grafica_bingham.installEventFilter(self)
        self.DatosFluidos.MenuFluidos.grafica_potencias.installEventFilter(self)
        self.DatosFluidos.MenuFluidos.grafica_potencias_m.installEventFilter(self)
        self.DatosFluidos.MenuFluidos.dibujo_smith.installEventFilter(self)
        self.setWindowTitle("Easy Drill")
        self.setGeometry((GetSystemMetrics(0)-width)/2, (GetSystemMetrics(1)-height)/2, width, height)
        self.setWindowIcon(QIcon("Imagenes/Gota.png"))
        self.cambiar_central()
        self.setCentralWidget(self.central_widget)
        self.btn_aceptar.clicked.connect(self.aceptar)
        self.btn_regresar.clicked.connect(self.regresar)
        self.btn_cancelar.clicked.connect(self.cancelar)

    def cambiar_central(self):
        if self.pos is 0:
            self.frame_trayectoria.show()
            self.frame_datos_trayectoria.hide()
        if self.pos is 1:
            self.frame_trayectoria.hide()
            self.DatosTrayectoria.cambia_trayectoria(self.trayectoria.get_clicked())
            self.frame_datos_trayectoria.show()
            self.frame_datos_fluidos.hide()
        if self.pos is 2:
            self.frame_datos_trayectoria.hide()
            self.frame_datos_fluidos.show()

    @pyqtSlot()
    def regresar(self):
        if self.pos is 0:
            self.btn_regresar.hide()
            self.cambia_pantalla()
        elif self.pos is 1:
            self.pos = 0
            self.btn_regresar.hide()
            self.cambia_pantalla()
        elif self.pos is 2:
            self.pos = 1
            self.cambia_pantalla()
        elif self.pos is 3:
            self.pos = 2
            self.cambia_pantalla()

    @pyqtSlot()
    def aceptar(self):
        if self.pos is 0:
            if self.trayectoria.get_clicked() is not 0:
                self.pos = 1
                self.btn_regresar.show()
                self.cambia_pantalla()
            else:
                self.error_dialog.showMessage('Debes seleccionar el tipo de trayectoria')
        elif self.pos is 1:
            if self.DatosTrayectoria.check():
                self.pos = 2
                self.cambia_pantalla()
            else:
                self.error_dialog.showMessage('Datos Errorneos o incompletos')

        elif self.pos is 2:
            self.pos = 3
            self.cambia_pantalla()


    @pyqtSlot()
    def cancelar(self):
        pass

    def eventFilter(self, source, event):
        if source is self.DatosFluidos.tipo_datos:
            if event.type() == QEvent.MouseButtonPress:
                if self.DatosFluidos.flag:
                    self.DatosFluidos.cambia_datos(False)
                    print("Laboratorio")
                else:
                    self.DatosFluidos.cambia_datos(True)
                    print("Campo")
        else:
            if event.type() == QEvent.Enter:
                self.intercambiar_imagen(source, True)
                self.stop = True
                return True
            elif event.type() == QEvent.Leave:
                self.intercambiar_imagen(source, False)
                self.stop = False
            elif event.type() == QEvent.MouseButtonPress:
                self.ponimagen(source)
            return False
        return False

    def intercambiar_imagen(self, source, flag):
        if self.pos is 0:
            self.trayectoria.cambiar_imagen(source, flag)
        elif self.pos is 2:
            self.DatosFluidos.MenuFluidos.intercambiar_imagen(source, flag)

    def ponimagen(self, source):
        if self.pos is 0:
            self.trayectoria.isclicked(source)
            self.aceptar()
        if self.pos is 2:
            if self.DatosFluidos.checkdatos():
                self.DatosFluidos.MenuFluidos.isclicked(source)
            else:
                self.error_dialog.showMessage('Oh no!')

    def cambiarfondo(self):
        if self.pos is 1 or self.pos is 3:
            palette = QPalette()
            palette.setBrush(10, QBrush(QImage("Imagenes/Fondo 2.png")))
            self.setPalette(palette)
        else:
            palette = QPalette()
            palette.setBrush(10, QBrush(QImage("Imagenes/Fondo.png")))
            self.setPalette(palette)

    def cambia_pantalla(self):
        self.cambiar_central()
        self.cambiarfondo()

if __name__ == '__main__':
    w = MainWindow()
    w.setFixedSize(1000, 605)
    w.show()
    sys.exit(w.app.exec_())
