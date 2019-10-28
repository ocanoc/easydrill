from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class DatosTuberia(QWidget):
    def __init__(self, parent=None):
        self.anterior = 0
        super(DatosTuberia, self).__init__(parent)
        self.campo_longitud = QLineEdit()
        self.campo_od = QLineEdit()
        self.campo_id = QLineEdit()
        self.campo_bl = QLineEdit()
        self.acodiciona(self.campo_bl)
        self.acodiciona(self.campo_longitud)
        self.acodiciona(self.campo_od)
        self.acodiciona(self.campo_id)

        self.tipo_tuberia = QComboBox()
        self.tipo_tuberia.insertItem(0, "TR")
        self.tipo_tuberia.insertItem(1, "Liner")
        self.tipo_tuberia.insertItem(2, "Agujero")
        self.tipo_tuberia.setCursor(Qt.PointingHandCursor)
        self.tipo_tuberia.currentIndexChanged.connect(self.selectionchange)

        self.layout_izquierda = QFormLayout()
        self.layout_izquierda.addRow("Tipo de Etapa", self.tipo_tuberia)
        self.layout_izquierda.addRow("Longitud [m]", self.campo_longitud)
        self.layout_izquierda.setVerticalSpacing(20)
        self.layout_izquierda.setFormAlignment(Qt.AlignTop)

        self.layout_derecha = QFormLayout()
        self.layout_derecha.addRow("ID [pg]", self.campo_id)
        self.layout_derecha.addRow("OD [pg]", self.campo_od)
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
        if i is 0:
            if self.anterior is 1:
                self.layout_derecha.removeRow(2)
            elif self.anterior is 2:
                self.campo_longitud = QLineEdit()
                self.campo_od = QLineEdit()
                self.campo_id = QLineEdit()
                self.acodiciona(self.campo_od)
                self.acodiciona(self.campo_id)
                self.layout_derecha.removeRow(0)
                self.layout_derecha.addRow("ID [pg]", self.campo_id)
                self.layout_derecha.addRow("OD [pg]", self.campo_od)
            self.anterior = 0
        elif i is 1:
            self.campo_bl = QLineEdit()
            self.acodiciona(self.campo_bl)
            if self.anterior is 2:
                self.campo_od = QLineEdit()
                self.campo_id = QLineEdit()
                self.layout_derecha.removeRow(0)
                self.layout_derecha.addRow("ID [pg]", self.campo_id)
                self.layout_derecha.addRow("OD [pg]", self.campo_od)
                self.campo_longitud = QLineEdit()
                self.acodiciona(self.campo_longitud)
                self.acodiciona(self.campo_od)
                self.acodiciona(self.campo_id)
                self.layout_izquierda.removeRow(1)
                self.layout_izquierda.addRow("Longitud [md]", self.campo_longitud)
            self.layout_derecha.addRow("B.L [md]", self.campo_bl)
            self.anterior = 1
        elif i is 2:
            self.campo_od = QLineEdit()
            self.campo_longitud = QLineEdit()
            self.acodiciona(self.campo_longitud)
            self.acodiciona(self.campo_od)
            if self.anterior is 0:
                self.layout_derecha.removeRow(1)
                self.layout_derecha.removeRow(0)
                self.layout_izquierda.removeRow(1)
            if self.anterior is 1:
                self.layout_derecha.removeRow(2)
                self.layout_derecha.removeRow(1)
                self.layout_derecha.removeRow(0)
                self.layout_izquierda.removeRow(1)
            self.layout_izquierda.addRow("Longitud [md]", self.campo_longitud)
            self.layout_derecha.addRow("OD [pg]", self.campo_od)
            self.anterior = 2

    def is_fill(self):
        try:
            if self.tipo_tuberia.currentIndex() is 0:
                if float(self.campo_longitud.text()) > 0 and float(self.campo_id.text()) > 0 \
                        and float(self.campo_od.text()):
                    if float(self.campo_id.text()) < float(self.campo_od.text()):
                        return True
                    else:
                        QMessageBox.critical(self, "Error", "Diametro interior igual o mayor que el exterior")
                        return False
            if self.tipo_tuberia.currentIndex() is 1:
                if float(self.campo_longitud.text()) > 0 and float(self.campo_id.text()) > 0 \
                        and float(self.campo_bl.text()) > 0 and float(self.campo_od.text()):
                    if float(self.campo_id.text()) < float(self.campo_od.text()):
                        return True
                    else:
                        QMessageBox.critical(self, "Error", "Diametro interior igual o mayor que el exterior")
                        return False
            if self.tipo_tuberia.currentIndex() is 2:
                if float(self.campo_longitud.text()) > 0 and float(self.campo_od.text()) > 0:
                    return True

        except ValueError:
            QMessageBox.critical(self, "Error", "Datos erroneos o incompletos")
            return False
        QMessageBox.critical(self, "Error", "Datos erroneos o incompletos")
        return False
    
    def get_name(self):
        if self.tipo_tuberia.currentIndex() is 2:
            return "Agujero {} pg ".format(self.campo_od.text())
        if self.tipo_tuberia.currentIndex() is 0:
            return "Etapa Tr {} pg ".format(self.campo_od.text())
        if self.tipo_tuberia.currentIndex() is 1:
            return "Etapa Liner {} pg ".format(self.campo_od.text())

    def get_id(self):
        return float(self.campo_id.text())

    def get_od(self):
        return float(self.campo_od.text())

    def get_datos(self):
        datos = [float(self.campo_longitud.text())]
        if self.tipo_tuberia.currentIndex() is 0:
            datos.append(float(self.campo_id.text()))
            datos.append(float(self.campo_od.text()))
            return datos
        if self.tipo_tuberia.currentIndex() is 1:
            datos.append(float(self.campo_id.text()))
            datos.append(float(self.campo_od.text()))
            datos.append(float(self.campo_bl.text()))
            return datos
        if self.tipo_tuberia.currentIndex() is 2:
            datos.append(float(self.campo_od.text()))
            return datos

    def clean(self):
        self.campo_longitud.setText("0")
        self.campo_od.setText("0")
        if self.tipo_tuberia.currentIndex() is 0:
            self.campo_id.setText("0")
        if self.tipo_tuberia.currentIndex() is 1:
            self.campo_id.setText("0")
            self.campo_bl.setText("0")

    def get_tipo(self):
        return self.tipo_tuberia.currentIndex()

    @staticmethod
    def acodiciona(btn):
        if isinstance(btn, QPushButton):
            btnancho = 30
            btn.setIconSize(QSize(btnancho, btnancho))
            btn.setFixedSize(btnancho, btnancho)
            btn.setCursor(Qt.PointingHandCursor)
        if isinstance(btn, QLineEdit):
            btn.setCursor(Qt.IBeamCursor)
            btn.setPlaceholderText("0")
