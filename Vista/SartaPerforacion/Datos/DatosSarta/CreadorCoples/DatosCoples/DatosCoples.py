from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from VentanaTuberiaHerramientas.Administradores.Datos.Datos import Datos


class DatosCoples(QDialog):

    def __init__(self, parent=None):
        super(DatosCoples, self).__init__(parent)
        self.row = None
        self.datos = Datos(13)
        self.label = QLabel("Selecciona una conexion.")
        self.btn_aceptar = QPushButton("Aceptar")
        self.btn_cancelar = QPushButton("Cancelar")

        self.btn_aceptar.clicked.connect(lambda *args: self.aceptar())
        self.btn_cancelar.clicked.connect(lambda *args: self.reject())
        self.acondiciona(self.btn_aceptar)
        self.acondiciona(self.btn_cancelar)

        self.layout_btn = QHBoxLayout()
        self.layout_btn.setAlignment(Qt.AlignLeft)
        self.layout_btn.addSpacing(25)
        self.layout_btn.addWidget(self.btn_aceptar)
        self.layout_btn.addSpacing(50)
        self.layout_btn.addWidget(self.btn_cancelar)

        self.layout_pantalla = QVBoxLayout()
        self.layout_pantalla.addWidget(self.label)
        self.layout_pantalla.addWidget(self.datos)
        self.layout_pantalla.addLayout(self.layout_btn)
        self.setLayout(self.layout_pantalla)

    def aceptar(self):
        try:
            self.row = self.datos.get_data()
        except ValueError:
            self.row = None
            QMessageBox.critical(self, "Aviso.", "Datos incompletos.")
        if self.row is not None:
            self.accept()
        else:
            self.row = None

    def get_data(self):
        return self.row

    @staticmethod
    def acondiciona(btn):
        if isinstance(btn, QPushButton):
            btn.setCursor(Qt.PointingHandCursor)
            btn.setStyleSheet("""
                               QPushButton {
                               background-color: rgb(0, 80, 85);
                               border-style: outset;
                               border-width: 1px;
                               border-radius: 5px;
                               font:  11px;
                               min-width: 6em;
                               padding: 6px;
                               color: white
                               }
                               QPushButton:pressed {
                                   background-color: rgb(154, 154, 154);
                                   border-style: inset;
                               }""")
        if isinstance(btn, QLineEdit):
            btn.setFixedWidth(85)
            btn.setCursor(Qt.IBeamCursor)
            btn.setPlaceholderText("0")
