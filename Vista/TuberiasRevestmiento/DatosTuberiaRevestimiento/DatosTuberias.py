from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from Modelo.Objetos.Tuberia.Exterior import Exterior
from Recursos.Constantes.Convertidor import Convertidor


class DatosTuberia(QWidget):
    def __init__(self, parent=None):
        self.anterior = 0
        super(DatosTuberia, self).__init__(parent)
        self.campo_longitud = None
        self.campo_id = None
        self.campo_bl = None
        self.campo_od = None
        self.acondiciona_lineedits()

        self.tipo_tuberia = QComboBox()
        self.tipo_tuberia.insertItem(0, "TR")
        self.tipo_tuberia.insertItem(1, "Liner")
        self.tipo_tuberia.insertItem(2, "Agujero")
        self.tipo_tuberia.setCursor(Qt.PointingHandCursor)
        self.tipo_tuberia.currentIndexChanged.connect(self.selectionchange)

        self.layout_izquierda = QFormLayout()
        self.layout_izquierda.addRow("Tipo de seccion", self.tipo_tuberia)
        self.layout_izquierda.addRow("Longitud [m]", self.campo_longitud)
        self.layout_izquierda.setVerticalSpacing(20)
        self.layout_izquierda.setFormAlignment(Qt.AlignTop)

        self.layout_derecha = QFormLayout()
        self.layout_derecha.addRow("OD [pg]", self.campo_od)
        self.layout_derecha.addRow("ID [pg]", self.campo_id)
        self.layout_derecha.setVerticalSpacing(20)
        self.layout_derecha.setFormAlignment(Qt.AlignTop)

        self.layout_campos = QHBoxLayout()
        self.layout_campos.addLayout(self.layout_izquierda)
        self.layout_campos.addLayout(self.layout_derecha)

        self.layout_pantalla = QVBoxLayout()
        self.layout_pantalla.addLayout(self.layout_campos)
        self.setLayout(self.layout_pantalla)

        palette = QPalette()
        self.setAutoFillBackground(True)
        palette.setColor(self.backgroundRole(), QColor(208, 206, 206))
        self.setPalette(palette)
        self.setFont(QFont('Calibri (Cuerpo)', 12, QFont.Bold))

    def selectionchange(self, i):
        self.layout_izquierda.removeRow(1)
        self.layout_derecha.removeRow(0)
        if i is 0:
            if self.anterior is 1:
                self.layout_derecha.removeRow(1)
                self.layout_derecha.removeRow(0)
            self.acondiciona_lineedits()
            self.layout_derecha.addRow("OD [pg]", self.campo_od)
            self.layout_derecha.addRow("ID [pg]", self.campo_id)
            self.anterior = 0
        elif i is 1:
            if self.anterior is 0:
                self.layout_derecha.removeRow(0)
            self.acondiciona_lineedits()
            self.layout_derecha.addRow("OD [pg]", self.campo_od)
            self.layout_derecha.addRow("ID [pg]", self.campo_id)
            self.layout_derecha.addRow("B.L [md]", self.campo_bl)
            self.anterior = 1
        elif i is 2:
            if self.anterior is 0:
                self.layout_derecha.removeRow(0)
            if self.anterior is 1:
                self.layout_derecha.removeRow(1)
                self.layout_derecha.removeRow(0)
            self.acondiciona_lineedits()
            self.layout_derecha.addRow("OD [pg]", self.campo_od)
            self.anterior = 2
        self.layout_izquierda.addRow("Longitud [m]", self.campo_longitud)

    def is_fill(self):
        try:
            if self.tipo_tuberia.currentIndex() is 0:
                if Convertidor.fracc_to_dec(self.campo_longitud.text()) > 0 and \
                        Convertidor.fracc_to_dec(self.campo_id.text()) > 0 \
                        and Convertidor.fracc_to_dec(self.campo_od.text()) > 0:
                    if Convertidor.fracc_to_dec(self.campo_id.text()) < Convertidor.fracc_to_dec(self.campo_od.text()):
                        return True
                    else:
                        QMessageBox.critical(self, "Error", "Diametro interior igual o mayor que diametro exterior.")
                        return False
            if self.tipo_tuberia.currentIndex() is 1:
                if Convertidor.fracc_to_dec(self.campo_longitud.text()) > 0 and \
                        Convertidor.fracc_to_dec(self.campo_id.text()) > 0 \
                        and Convertidor.fracc_to_dec(self.campo_bl.text()) > 0 and \
                        Convertidor.fracc_to_dec(self.campo_od.text()) > 0:
                    if Convertidor.fracc_to_dec(self.campo_id.text()) < Convertidor.fracc_to_dec(self.campo_od.text()):
                        return True
                    else:
                        QMessageBox.critical(self, "Error", "Diametro interior igual o mayor que el diametro exterior.")
                        return False
            if self.tipo_tuberia.currentIndex() is 2:
                if Convertidor.fracc_to_dec(self.campo_longitud.text()) > 0 and \
                        Convertidor.fracc_to_dec(self.campo_od.text()) > 0:
                    return True
        except ValueError:
            QMessageBox.critical(self, "Error", "Datos erroneos o incompletos.")
            return False
        QMessageBox.critical(self, "Error", "Datos erroneos o incompletos.")
        return False

    def get_name(self):
        if self.tipo_tuberia.currentIndex() is 2:
            return "Agujero {} pg ".format(self.campo_od.text())
        if self.tipo_tuberia.currentIndex() is 0:
            return "Etapa Tr {} pg ".format(self.campo_od.text())
        if self.tipo_tuberia.currentIndex() is 1:
            return "Etapa Liner {} pg ".format(self.campo_od.text())

    def get_id(self):
        return Convertidor.fracc_to_dec(self.campo_id.text())

    def get_od(self):
        return Convertidor.fracc_to_dec(self.campo_od.text())

    def get_datos(self, direccional, anterior):
        if self.tipo_tuberia.currentIndex() is 0 or self.tipo_tuberia.currentIndex() is 1:
            exterior = Exterior(Convertidor.fracc_to_dec(self.campo_od.text()),
                                Convertidor.fracc_to_dec(self.campo_id.text()),
                                Convertidor.fracc_to_dec(self.campo_longitud.text()), direccional, anterior)
            if self.tipo_tuberia.currentIndex() is 0:
                exterior.set_tipo("TR")
            if self.tipo_tuberia.currentIndex() is 1:
                print("entre")
                exterior.set_tipo("Liner")
                exterior.set_boca_liner(Convertidor.fracc_to_dec(self.campo_bl.text()))
        elif self.tipo_tuberia.currentIndex() is 2:
            exterior = Exterior(Convertidor.fracc_to_dec(self.campo_od.text()),
                                Convertidor.fracc_to_dec(self.campo_od.text()),
                                Convertidor.fracc_to_dec(self.campo_longitud.text()), direccional, anterior)
            exterior.set_tipo("Agujero")
        return exterior

    def clean(self):
        self.tipo_tuberia.setCurrentIndex(1)
        self.tipo_tuberia.setCurrentIndex(0)

    def get_tipo(self):
        return self.tipo_tuberia.currentIndex()

    @staticmethod
    def acondiciona(btn):
        if isinstance(btn, QPushButton):
            btnancho = 30
            btn.setIconSize(QSize(btnancho, btnancho))
            btn.setFixedSize(btnancho, btnancho)
            btn.setCursor(Qt.PointingHandCursor)
        if isinstance(btn, QLineEdit):
            btn.setCursor(Qt.IBeamCursor)
            btn.setPlaceholderText("0")

    def acondiciona_lineedits(self):
        self.campo_longitud = QLineEdit()
        self.campo_od = QLineEdit()
        self.campo_id = QLineEdit()
        self.campo_bl = QLineEdit()
        self.acondiciona(self.campo_bl)
        self.acondiciona(self.campo_longitud)
        self.acondiciona(self.campo_od)
        self.acondiciona(self.campo_id)

    def get_long(self):
        try:
            return Convertidor.fracc_to_dec(self.campo_longitud.text())
        except ValueError:
            return 0

    def get_boca_liner(self):
        try:
            return Convertidor.fracc_to_dec(self.campo_bl.text())
        except ValueError:
            return 0

    def get_d_agujero(self):
        return Convertidor.fracc_to_dec(self.campo_od.text())
