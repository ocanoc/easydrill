import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from DatosTrayectoria.DatosTrayectoria import DatosTrayectoria
from Fluidos.DatosFluidos.DatosFluidos import DatosFluidos
from MenuSartaPerforacion import SartaPerforacion
from TrayectoriaDireccional.MenuTrayectoria import Trayectoria
from TuberiasRevestmiento.MenuTuberiasRevestimiento import TuberiasRevestimiento
from VentanaResultados.MenuResultados import MenuResultados


# noinspection PyArgumentList
class Nuevo(QWidget):

    seleccion = 0
    pos = 0
    stop = False
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    btn_aceptar = QPushButton("Aceptar")
    btn_cancelar = QPushButton("Cancelar")
    btn_regresar = QPushButton("Regresar")
    btn_regresar.hide()

    Trayectoria = Trayectoria()

    DatosTrayectoria = DatosTrayectoria()
    DatosTrayectoria.hide()

    DatosFluidos = DatosFluidos()
    DatosFluidos.hide()

    Tuberiras_revestimiento = TuberiasRevestimiento()
    Tuberiras_revestimiento.hide()

    Sarta_Perforacion = SartaPerforacion()
    Sarta_Perforacion.hide()

    menu_resultados = MenuResultados()
    menu_resultados.hide()

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
    layout_pantalla.addWidget(Tuberiras_revestimiento)
    layout_pantalla.addWidget(Sarta_Perforacion)
    layout_pantalla.addWidget(menu_resultados)
    layout_pantalla.addLayout(layout_btn)

    datos_trayectoria = []
    datos_fluido = []
    datos_tuberia_revestimiento = []
    datos_bomba = []
    datos_barrena = []

    def __init__(self):
        super(Nuevo, self).__init__()
        self.acodiciona(self.btn_aceptar)
        self.acodiciona(self.btn_cancelar)
        self.acodiciona(self.btn_regresar)
        self.setLayout(self.layout_pantalla)

        palette = QPalette()
        palette.setBrush(10, QBrush(QImage("Imagenes/Fondo/Fondo.png")))
        self.setFont(QFont('Calibri (Cuerpo)', 12, QFont.Bold))
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

        self.Sarta_Perforacion.barrena_triconica.installEventFilter(self)
        self.Sarta_Perforacion.barrena_pdc.installEventFilter(self)
        self.Sarta_Perforacion.barrena_triconica.installEventFilter(self)
        self.Sarta_Perforacion.barrena_pdc.installEventFilter(self)

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
            self.Tuberiras_revestimiento.hide()
        if self.pos is 3:
            self.DatosFluidos.hide()
            self.Tuberiras_revestimiento.set_long_disp(self.DatosTrayectoria.get_long_max())
            self.Tuberiras_revestimiento.show()
            self.Sarta_Perforacion.hide()
        if self.pos is 4:
            self.Tuberiras_revestimiento.hide()
            self.Sarta_Perforacion.set_diametro_agujero(self.Tuberiras_revestimiento.get_d_agujero())
            self.Sarta_Perforacion.show()
            self.menu_resultados.hide()
        if self.pos is 5:
            self.Sarta_Perforacion.hide()
            self.menu_resultados.show()

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
            self.btn_aceptar.setText("Aceptar")
            self.cambiar_central()
        elif self.pos is 5:
            self.pos = 4
            self.cambiar_central()
            self.btn_aceptar.show()

    @pyqtSlot()
    def aceptar(self):
        if self.pos is 0:
            if self.Trayectoria.get_clicked() is not 0:
                self.pos = 1
                self.btn_regresar.show()
                self.cambiar_central()
            else:
                QMessageBox.critical(self, "Error", "Selecciona una trayectoria.")
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
        elif self.pos is 3:
            if self.Tuberiras_revestimiento.is_fill():
                self.pos = 4
                self.cambiar_central()
                self.btn_aceptar.setText("Terminar")
        elif self.pos is 4:
            if self.Sarta_Perforacion.check():
                self.get_datos()
                self.pos = 5
                self.cambiar_central()
                self.btn_aceptar.hide()

    def eventFilter(self, source, event):
        if source is self.DatosFluidos.tipo_datos:
            if event.type() == QEvent.MouseButtonPress and self.isEnabled():
                self.setEnabled(False)
                if self.DatosFluidos.flag:
                    self.DatosFluidos.cambia_datos(False)
                else:
                    self.DatosFluidos.cambia_datos(True)
                self.setEnabled(True)
        elif (source is self.Sarta_Perforacion.barrena_triconica or source is self.Sarta_Perforacion.barrena_pdc) \
                and event.type() == QEvent.MouseButtonPress:
            if event.type() == QEvent.MouseButtonPress:
                self.Sarta_Perforacion.add_barrena(source)
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
        elif self.pos is 4:
            self.Sarta_Perforacion.intercambiar_imagen(source, flag)

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
        if self.pos is 4:
            self.Sarta_Perforacion.isclicked(source)

    def get_datos(self):
        datos_trayectoria = self.DatosTrayectoria.get_datos()
        datos_fluidos = self.DatosFluidos.get_datos(DatosFluidos.MenuFluidos.get_modelo())
        datos_revestimiento = self.Tuberiras_revestimiento.get_datos(datos_trayectoria)
        datos_sup, bomba, datos_sarta, barrena = self.Sarta_Perforacion.get_datos()
        self.menu_resultados.operate_data(datos_trayectoria, datos_fluidos, datos_revestimiento, datos_sup, bomba,
                                          datos_sarta, barrena)

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
