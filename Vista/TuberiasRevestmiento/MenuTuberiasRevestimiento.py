import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from Controlador.Tuberia.ControladorTuberia import ControladorTuberia
from TuberiasRevestmiento.DatosTuberiaRevestimiento.DatosTuberias import DatosTuberia


class TuberiasRevestimiento(QWidget):
    app = QApplication(sys.argv)
    app.setStyle('Fusion')

    texto_encabezado = QLabel()
    texto_encabezado.setScaledContents(True)
    texto_encabezado.setFixedSize(250, 50)
    texto_encabezado.setPixmap(QPixmap("Imagenes/Revestimieto/TextoDatosMecanicos.png"))

    imagen_mecanico = QLabel()
    imagen_mecanico.setPixmap(QPixmap("Imagenes/Revestimieto/ImagenEstadoMecanico.png"))
    imagen_mecanico.setScaledContents(True)
    imagen_mecanico.setFixedSize(196, 379)

    etapa = QToolBox()
    etapa.setFixedSize(550, 285)

    mas = QPushButton()
    mas.setIcon(QIcon("Imagenes/Iconos/mas.png"))
    mas.setToolTip("Agrega sección")

    menos = QPushButton()
    menos.setIcon(QIcon("Imagenes/Iconos/menos.png"))
    menos.setToolTip("Elimina sección")

    label_instrucciones = QLabel("Ingrese los datos de la etapa:")

    label_long_disp = QLabel("0")

    layout_long_disp = QFormLayout()
    layout_long_disp.addRow("Longitud disponible [md]: ", label_long_disp)

    layout_botones = QHBoxLayout()
    layout_botones.addSpacing(30)
    layout_botones.addLayout(layout_long_disp)
    layout_botones.addStretch(1)
    layout_botones.addWidget(mas)
    layout_botones.addSpacing(20)
    layout_botones.addWidget(menos)
    layout_botones.addStretch(1)

    layout_etapa = QVBoxLayout()
    layout_etapa.addSpacing(7)
    layout_etapa.addWidget(label_instrucciones)
    layout_etapa.addWidget(etapa)
    layout_etapa.addLayout(layout_botones)
    layout_etapa.addStretch(1)

    layout_contenido = QHBoxLayout()
    layout_contenido.addSpacing(40)
    layout_contenido.addWidget(imagen_mecanico)
    layout_contenido.addSpacing(58)
    layout_contenido.addLayout(layout_etapa)

    layout_pantalla = QVBoxLayout()
    layout_pantalla.addSpacing(0)
    layout_pantalla.addWidget(texto_encabezado)
    layout_pantalla.addSpacing(47)
    layout_pantalla.addLayout(layout_contenido)
    layout_pantalla.addStretch(1)

    datos = []

    lleno = False
    agujero = False
    ultimo = True
    prof_max = 0
    d_agujero = 0

    def __init__(self):
        super(TuberiasRevestimiento, self).__init__()
        self.etapa.addItem(DatosTuberia(self.etapa), "Agrega una sección.")
        self.mas.clicked.connect(lambda *args: self.agrega())
        self.menos.clicked.connect(lambda *args: self.elimina())
        self.acodiciona(self.mas)
        self.acodiciona(self.menos)
        self.setLayout(self.layout_pantalla)
        self.setFont(QFont('Calibri (Cuerpo)', 12, QFont.Bold))
        self.etapa.currentChanged.connect(self.selectionchange)

    def agrega(self):
        try:
            if self.etapa.count() < 10:
                if self.lleno is False and (
                        self.etapa.widget(self.etapa.count() - 1).get_tipo() is 2 or self.etapa.widget(
                    self.etapa.count() - 1).get_tipo() is 1):
                    QMessageBox.critical(self, "Error", "Se debe agregar al menos una tuberia de revestimiento.")
                elif self.agujero and self.lleno:
                    QMessageBox.critical(self, "Error", "Debes borrar la etapa agujero para agregar mas etapas.")
                elif self.etapa.widget(self.etapa.count() - 1).is_fill() and self.check_di() \
                        and self.check_long() and self.update_long_disp():
                    self.rename()
                    self.lleno = True
                    if self.etapa.widget(self.etapa.count() - 1).get_tipo() is not 2:
                        self.etapa.addItem(DatosTuberia(self.etapa),
                                           "Agrega una sección".format(self.etapa.count() + 1))
                        self.etapa.setCurrentIndex(self.etapa.count() - 1)
                    else:
                        self.d_agujero = self.etapa.widget(self.etapa.count() - 1).get_d_agujero()
                        self.agujero = True
            else:
                QMessageBox.critical(self, "Error", "Demasiadas secciones.")
        except ValueError:
            return False

    def elimina(self):
        if self.ultimo is True:
            if self.etapa.count() > 1:
                if self.etapa.widget(self.etapa.count() - 1).get_tipo() is 2:
                    self.agujero = False
                self.etapa.removeItem(self.etapa.currentIndex())
            else:
                self.agujero = False
                self.lleno = False
                self.etapa.widget(self.etapa.count() - 1).clean()
                self.etapa.setItemText(self.etapa.count() - 1, "Agrega una sección")
                QMessageBox.information(self, "Limpio", "No hay mas etapas")
            self.update_long_disp()
        else:
            result = QMessageBox.question(self, "Confirmacion.", "Se borrarán las secciones siguientes para"
                                                                 " evitar inconsistencias. \n¿Desea continuar?",
                                          QMessageBox.Yes | QMessageBox.No)
            if result == QMessageBox.Yes:
                actual = self.etapa.currentIndex()
                count = self.etapa.count()
                eliminar = count - actual - 1
                if self.agujero:
                    eliminar = eliminar
                    self.agujero = False
                for x in range(eliminar):
                    self.etapa.removeItem(self.etapa.count() - 1)
                self.mas.setEnabled(True)
                self.etapa.widget(self.etapa.count() - 1).clean()
                self.ultimo = True
                self.etapa.setItemText(self.etapa.count() - 1, "Agrega una sección")
                self.update_long_disp()

    def rename(self):
        self.etapa.setItemText(self.etapa.count() - 1, self.etapa.widget(self.etapa.count() - 1).get_name())

    def check_di(self):
        if self.etapa.count() is 1:
            return True
        elif self.etapa.widget(self.etapa.count() - 1).get_od() < self.etapa.widget(self.etapa.count() - 2).get_id():
            return True
        else:
            QMessageBox.critical(self, "Error", "El diámetro es mayor o igual al de la tubería anterior.")
            return False

    def is_fill(self):
        if self.lleno and self.agujero:
            return True
        elif self.lleno is False:
            QMessageBox.critical(self, "Error", "No hay secciones guardadas.")
            return False
        elif self.agujero is False:
            QMessageBox.critical(self, "Error", "No hay agujero descubierto.")
            return False
        if float(self.label_long_disp.text()) is not 0:
            QMessageBox.critical(self, "Error", "Longitud disponible.")
            return False

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

    def selectionchange(self, i):
        if i is not (self.etapa.count() - 1):
            self.mas.setEnabled(False)
            self.ultimo = False
        else:
            self.ultimo = True
            self.mas.setEnabled(True)

    def get_datos(self, direccional):
        externas = []
        anterior = None
        if self.lleno and self.agujero:
            for x in range(self.etapa.count()):
                nueva = self.etapa.widget(x).get_datos(direccional, anterior)
                externas.append(nueva)
                if nueva.get_tipo() == "Liner":
                    anterior.set_fin_pd(nueva.get_boca_liner())
                    anterior.set_long(anterior.get_fin_pd() - anterior.get_inicio_pd())
                    nueva.set_inicio_pd(nueva.get_boca_liner())
                    nueva.set_fin_pd(nueva.get_inicio_pd() + nueva.get_long())
                anterior = nueva
        ControladorTuberia.profundidad_vertical(externas, direccional)
        return externas

    def set_long_disp(self, prof_maxima):
        self.prof_max = prof_maxima
        self.update_long_disp()

    def update_long_disp(self):
        long = 0
        for x in range(self.etapa.count()):
            if self.etapa.widget(x).get_tipo() is 1:
                long = self.etapa.widget(x).get_boca_liner()
                long += self.etapa.widget(x).get_long()
            else:
                long += self.etapa.widget(x).get_long()
        if long > self.prof_max:
            QMessageBox.critical(self, "Error", "Longitud mayor a la profundidad desarrollada.")
            return False
        else:
            self.label_long_disp.setText(str(self.prof_max - long))
            return True

    def check_long(self):
        if float(self.label_long_disp.text()) > 0:
            return True
        else:
            QMessageBox.critical(self, "Error", "No hay longitud desarrollada disponible.")
            return False

    def get_d_agujero(self):
        return self.d_agujero
