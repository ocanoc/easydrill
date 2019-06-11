import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from DatosTrayectoria.DatosTrayectoria import DatosTrayectoria
from Fluidos.DatosFluidos.DatosFluidos import DatosFluidos
from MenuTuberiasPerforacion import TuberiaPerforacion
from TrayectoriaDireccional.MenuTrayectoria import Trayectoria
from TuberiasRevestmiento.MenuTuberiasRevestimiento import TuberiasRevestimiento


# noinspection PyArgumentList
class Nuevo(QWidget):
    seleccion = 0
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    pos = 0
    stop = False

    btn_aceptar = QPushButton("Aceptar")
    btn_cancelar = QPushButton("Cancelar")
    btn_regresar = QPushButton("Regresar")
    btn_regresar.hide()

    Trayectoria = Trayectoria()

    DatosTrayectoria = DatosTrayectoria()
    DatosTrayectoria.hide()

    DatosFluidos = DatosFluidos()
    DatosFluidos.hide()

    Tuberiras_revetimietno = TuberiasRevestimiento()
    Tuberiras_revetimietno.hide()

    frame_tp = TuberiaPerforacion()
    frame_tp.hide()

    layout_btn = QHBoxLayout()
    layout_btn.addSpacing(50)
    layout_btn.addWidget(btn_cancelar, 1, Qt.AlignLeft)
    layout_btn.addWidget(btn_regresar, 1)
    layout_btn.addSpacing(20)
    layout_btn.addWidget(btn_aceptar, 1)
    layout_btn.addSpacing(50)

    layout_pantalla = QVBoxLayout()
    layout_pantalla.addWidget(Trayectoria)
    layout_pantalla.addWidget(DatosTrayectoria)
    layout_pantalla.addWidget(DatosFluidos)
    layout_pantalla.addWidget(Tuberiras_revetimietno)
    layout_pantalla.addWidget(frame_tp)
    layout_pantalla.addLayout(layout_btn)

    def __init__(self):
        super(Nuevo, self).__init__()

        self.acodiciona(self.btn_aceptar)
        self.acodiciona(self.btn_cancelar)
        self.acodiciona(self.btn_regresar)
        self.setLayout(self.layout_pantalla)
        palette = QPalette()
        palette.setBrush(10, QBrush(QImage("Imagenes/Fondo/Fondo.png")))
        self.setPalette(palette)

        self.Trayectoria.imagen_vertical.installEventFilter(self)
        self.Trayectoria.imagen_tipo_s.installEventFilter(self)
        self.Trayectoria.imagen_tipo_j.installEventFilter(self)
        self.Trayectoria.imagen_horizontal.installEventFilter(self)
        self.DatosFluidos.tipo_datos.installEventFilter(self)
        self.DatosFluidos.MenuFluidos.grafica_bingham.installEventFilter(self)
        self.DatosFluidos.MenuFluidos.grafica_potencias.installEventFilter(self)
        self.DatosFluidos.MenuFluidos.grafica_potencias_m.installEventFilter(self)
        self.DatosFluidos.MenuFluidos.dibujo_smith.installEventFilter(self)

        self.cambiar_central()
        self.btn_aceptar.clicked.connect(self.aceptar)
        self.btn_regresar.clicked.connect(self.regresar)

    def cambiar_central(self):
        if self.pos is 0:
            self.Trayectoria.show()
            self.DatosTrayectoria.hide()
        if self.pos is 1:
            self.Trayectoria.hide()
            self.DatosTrayectoria.cambia_trayectoria(self.Trayectoria.get_clicked())
            self.DatosTrayectoria.show()
            self.DatosFluidos.hide()
        if self.pos is 2:
            self.DatosTrayectoria.hide()
            self.DatosFluidos.show()
            self.Tuberiras_revetimietno.hide()
        if self.pos is 3:
            self.DatosFluidos.hide()
            self.Tuberiras_revetimietno.show()
            self.frame_tp.hide()
        if self.pos is 4:
            self.Tuberiras_revetimietno.hide()
            self.frame_tp.show()

    @pyqtSlot()
    def regresar(self):
        if self.pos is 0:
            self.btn_regresar.hide()
            self.cambiar_central()
        elif self.pos is 1:
            self.pos = 0
            self.btn_regresar.hide()
            self.cambiar_central()
        elif self.pos is 2:
            self.pos = 1
            self.cambiar_central()
        elif self.pos is 3:
            self.pos = 2
            self.cambiar_central()
        elif self.pos is 4:
            self.pos = 3
            self.cambiar_central()

    @pyqtSlot()
    def aceptar(self):
        if self.pos is 0:
            if self.Trayectoria.get_clicked() is not 0:
                self.pos = 1
                self.btn_regresar.show()
                self.cambiar_central()
            else:
                QMessageBox.critical(self, "Error", "Datos erroneos o incompletos")
        elif self.pos is 1:
            if self.DatosTrayectoria.check():
                self.pos = 2
                self.cambiar_central()
            else:
                QMessageBox.critical(self, "Error", "Datos erroneos o incompletos")
        elif self.pos is 2:
            if self.DatosFluidos.check() and self.DatosFluidos.MenuFluidos.get_clicked():
                self.pos = 3
                self.cambiar_central()
            else:
                QMessageBox.critical(self, "Error", "Datos erroneos o incompletos")
        elif self.pos is 3:
            self.pos = 4
            self.cambiar_central()

    def eventFilter(self, source, event):
        if source is self.DatosFluidos.tipo_datos:
            if event.type() == QEvent.MouseButtonPress:
                if self.DatosFluidos.flag:
                    self.DatosFluidos.cambia_datos(False)
                else:
                    self.DatosFluidos.cambia_datos(True)
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
            self.Trayectoria.cambiar_imagen(source, flag)
        elif self.pos is 2:
            self.DatosFluidos.MenuFluidos.intercambiar_imagen(source, flag)

    def ponimagen(self, source):
        if self.pos is 0:
            self.Trayectoria.isclicked(source)
            self.aceptar()
        if self.pos is 2:
            if source is self.DatosFluidos.MenuFluidos.grafica_potencias_m:
                if self.DatosFluidos.check_gel() and self.DatosFluidos.check():
                    self.DatosFluidos.MenuFluidos.isclicked(source)
                else:
                    QMessageBox.critical(self, "Error", "Este modelo reologico necesita el campo Gel.")
            elif self.DatosFluidos.check():
                self.DatosFluidos.MenuFluidos.isclicked(source)
            else:
                QMessageBox.critical(self, "Error", "Datos erroneos o incompletos")

    @staticmethod
    def acodiciona(btn):
        btn.setCursor(Qt.PointingHandCursor)
        btn.setFixedSize(100, 30)
        btn.setStyleSheet("""
            QPushButton {
            background-color: rgb(0, 80, 85);
            border-style: outset;
            border-width: 1px;
            border-radius: 5px;
            font:  12px;
            min-width: 8em;
            padding: 6px;
            color: white
            }
            QPushButton:pressed {
                background-color: rgb(154, 154, 154);
                border-style: inset;
            }""")
