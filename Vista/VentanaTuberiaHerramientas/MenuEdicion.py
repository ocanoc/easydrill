from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from VentanaTuberiaHerramientas.Administradores.Administrador import Administrador


class MenuEdicion(QWidget):
    def __init__(self, parent=None):
        super(MenuEdicion, self).__init__(parent)
        self.setFont(QFont('Calibri (Cuerpo)', 12, QFont.Bold))

        self.texto_encabezado = QLabel()
        self.texto_encabezado.setScaledContents(True)
        self.texto_encabezado.setFixedSize(350, 50)
        self.texto_encabezado.setPixmap(QPixmap("Imagenes/Titulos/TextoAdmin.png"))

        self.tab = QTabWidget()
        self.tab.setFixedSize(950, 475)
        self.tab.setObjectName("Tab");
        self.tab.setIconSize(QSize(187, 90))
        self.tab.setStyleSheet("""
            QTabWidget::pane {
            font:  24px;
            border: 3px  inset rgb(0, 80, 85);
            border-style: inset inset inset none ;
            border-bottom-right-radius: 5px 5px;
            border-top-right-radius: 5px 5px;
            background: rgb(208, 206, 206);
            } 
            
            QTabBar::tab {
              border-bottom-left-radius: 5px 5px;
              border-top-left-radius: 5px 5px;
              background: rgb(154, 154, 154);
              color: white;
              padding: 10px;
              border: 3px  inset rgb(0, 80, 85);
            } 
            
            QTabBar::tab:selected { 
            
             background: rgb(208, 206, 206);
             border-style: inset none inset inset ;
            }
        """)
        self.tab.setTabPosition(QTabWidget.West)
        self.tab.addTab(Administrador(1), QIcon("Imagenes/TextosTuberias/TextoTP.png"), "")
        self.tab.addTab(Administrador(2), QIcon("Imagenes/TextosTuberias/TextoHW.png"), "")
        self.tab.addTab(Administrador(3), QIcon("Imagenes/TextosTuberias/TextoDC.png"), "")
        self.tab.addTab(Administrador(4), QIcon("Imagenes/TextosTuberias/TextoConexiones.png"), "")
        self.tab.addTab(Administrador(5), QIcon("Imagenes/TextosTuberias/TextoEstabilizadores.png"), "")
        self.tab.addTab(Administrador(6), QIcon("Imagenes/TextosTuberias/TextoHerramientas.png"), "")
        self.tab.addTab(Administrador(7), QIcon("Imagenes/TextosTuberias/TextoPorta.png"), "")
        self.tab.addTab(Administrador(8), QIcon("Imagenes/TextosTuberias/TextoMartillos.png"), "")
        self.tab.addTab(Administrador(9), QIcon("Imagenes/TextosTuberias/TextoBarrenas.png"), "")
        self.tab.addTab(Administrador(10), QIcon("Imagenes/TextosTuberias/TextoMotor.png"), "")

        self.btn_finalizar = QPushButton("Finalizar")
        self.acodiciona(self.btn_finalizar)

        self.layout_widget = QVBoxLayout()
        self.layout_widget.addWidget(self.texto_encabezado, 1, Qt.AlignLeft)
        self.layout_widget.addWidget(self.tab, 1, Qt.AlignHCenter)
        self.layout_widget.addWidget(self.btn_finalizar, 1, Qt.AlignRight)
        self.setLayout(self.layout_widget)

    def termianr(self):
        pass

    @staticmethod
    def acodiciona(btn):
        if isinstance(btn, QPushButton):
            btn.setFixedSize(100, 30)
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
