from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from VentanaTuberiaHerramientas.Administradores.Datos.Datos import Datos


class VistaLongitud(QWidget):
    def __init__(self, tipo, parent=None):
        super(VistaLongitud, self).__init__(parent)
        self.table = Datos(tipo)
        self.table.set_table_height(320, 770)

        self.campo_longitud = QLineEdit()
        self.campo_longitud.setFixedWidth(85)
        self.campo_longitud.setCursor(Qt.IBeamCursor)
        self.campo_longitud.setPlaceholderText("0")

        self.layout_campo = QFormLayout()
        self.layout_campo.addRow("Longitud [m]:", self.campo_longitud)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.table)
        self.layout.addLayout(self.layout_campo)
        self.layout.addStretch(1)

        self.setLayout(self.layout)

    def get_data(self):
        data = self.table.get_data()
        if data is not None:
            print("entre")
            try:
                if float(self.campo_longitud.text()) > 0:
                    long = self.campo_longitud.text()
                    return data, long
                else:
                    QMessageBox.critical(self, "Error", "Ingresa una longitud valida.")
                    return None, None
            except ValueError:
                QMessageBox.critical(self, "Error", "Ingresa una longitud.")
                return None, None
        else:
            return None, None

    def get_tipo(self):
        return self.table.get_tipo()
