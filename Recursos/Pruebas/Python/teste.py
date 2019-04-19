import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from win32api import GetSystemMetrics

class MainWindow (QMainWindow):
    """docstring for Main Window."""
    def __init__(self):
        super(MainWindow, self).__init__()
        width = 1920
        height = 1080
        self.setWindowTitle("Easy Drill")

        self.setGeometry((GetSystemMetrics(0)-width)/2, (GetSystemMetrics(1)-height)/2,width,height)
        self.setWindowIcon(QIcon('petro.png'))
        self.initUI()


    def initUI (self):

        ##Status bar
        self.statusBar = self.statusBar()
        self.statusBar.showMessage('Bienvenido')
        ##
        central_widget = QWidget()
        self.setCentralWidget(central_widget) # new central widget
        ## Creacion de botones
        btn1 = QPushButton ("Puto Jordanx2")
        btn2 = QPushButton("Puto Jordanx3")
        btn3 = QPushButton ("Puto Jordanx4")
        btn4 = QPushButton("Puto Jordanx5")
        btn5 = QPushButton ("Puto Jordanx6")
        btn6 = QPushButton("Puto Jordanx7")
        ##
        ##Creacion del central
        hbox = QHBoxLayout(central_widget)
        self.setCentralWidget(central_widget) # new central widget
        central_widget.setAutoFillBackground(True) #Que se pinte el fondo
        p = central_widget.palette()
        p.setColor(central_widget.backgroundRole(),QColor(240,240,240)) #asignacion de colores
        central_widget.setPalette(p) # Asiganacion de ll pallete
        ##
        #layout en el central
        """
        hbox.addStretch(1)
        hbox.addWidget(btn1)
        hbox.addWidget(btn2)
        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)
        central_widget.setLayout(vbox)
        """
        ##
        ##Para la creacion de Splitters se necesita crear frames


        F_Columna_Geologica = QFrame() #creacion de frame
        Ly_Columna_Geologica = QHBoxLayout()
        F_Columna_Geologica.setFrameShape(QFrame.WinPanel) #forma exterior del frame
        F_Columna_Geologica.setFrameShadow(QFrame.Sunken)#forma interior del frame
        F_Columna_Geologica.setLineWidth(3)# ancho de borde
        F_Columna_Geologica.setMidLineWidth(3)# ancho borde interior
        F_Columna_Geologica.setAutoFillBackground(True)
        p = F_Columna_Geologica.palette()
        p.setColor(F_Columna_Geologica.backgroundRole(),Qt.white) #asignacion de colores
        F_Columna_Geologica.setPalette(p)
        ##Layout De Componenetes
        ##Lista de componenetes
        L_Columna_Geologica = QLabel()
        ##
        L_Columna_Geologica.setPixmap(QPixmap("Columna_Geologica.png"))## Label con Imagen
        LC_Columna_Geologica = QHBoxLayout()# Creacion del layout de componentes
        LC_Columna_Geologica.addWidget(L_Columna_Geologica)
        ##
        ##Grupo de Componentes
        G_Columna_Geologica = QGroupBox()
        G_Columna_Geologica.setTitle("Columna Geologica")
        G_Columna_Geologica.setFont(QFont('Consolas', 10))
        G_Columna_Geologica.setLayout(LC_Columna_Geologica)
        G_Columna_Geologica.setFlat(False)
        ##
        ##scroll
        S_Columna_Geologica = QScrollArea()
        S_Columna_Geologica.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        S_Columna_Geologica.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        S_Columna_Geologica.setWidgetResizable(True)
        S_Columna_Geologica.setWidget(G_Columna_Geologica)
        Ly_Columna_Geologica.addWidget(S_Columna_Geologica)
        F_Columna_Geologica.setLayout(Ly_Columna_Geologica)
        ##
        ##Sarta
        ##
        F_Sarta = QFrame()
        Ly_Sarta = QHBoxLayout()
        F_Sarta.setFrameShape(QFrame.WinPanel) #formato del frame
        F_Sarta.setFrameShadow(QFrame.Sunken)
        F_Sarta.setLineWidth(3)
        F_Sarta.setMidLineWidth(3)
        F_Sarta.setAutoFillBackground(True)
        p = F_Sarta.palette()
        p.setColor(F_Sarta.backgroundRole(),Qt.white) #asignacion de colores
        F_Sarta.setPalette(p)
        ##Layout De Componenetes
        ##Lista de componenetes
        L_Sarta = QLabel()
        ##
        L_Sarta.setPixmap(QPixmap("sarta.png"))## Label con Imagen
        ##
        LC_Sarta = QHBoxLayout()# Creacion del layout de componentes
        LC_Sarta.addWidget(L_Sarta)
        ##
        ##Grupo de Componentes
        G_Sarta = QGroupBox()
        G_Sarta.setTitle("Sarta de Perforacion")
        G_Sarta.setFont(QFont('Consolas', 10))
        G_Sarta.setLayout(LC_Sarta)
        G_Sarta.setFlat(False)
        ##
        ##scroll
        S_Sarta = QScrollArea()
        S_Sarta.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        S_Sarta.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        S_Sarta.setWidgetResizable(True)
        S_Sarta.setWidget(G_Sarta)
        ##
        Ly_Sarta.addWidget(S_Sarta)
        F_Sarta.setLayout(Ly_Sarta)
        ##
        ##Ventana_Operativa
        ##
        F_Ventana_Operativa = QFrame()
        Ly_Ventana_Operativa = QHBoxLayout()
        F_Ventana_Operativa.setFrameShape(QFrame.WinPanel) #formato del frame
        F_Ventana_Operativa.setFrameShadow(QFrame.Sunken)
        F_Ventana_Operativa.setLineWidth(3)
        F_Ventana_Operativa.setMidLineWidth(3)
        F_Ventana_Operativa.setAutoFillBackground(True)
        p = F_Ventana_Operativa.palette()
        p.setColor(F_Ventana_Operativa.backgroundRole(),Qt.white) #asignacion de colores
        F_Ventana_Operativa.setPalette(p)
        ##Layout De Componenetes
        ##Lista de componenetes
        L_Ventana_Operativa = QLabel()
        ##
        L_Ventana_Operativa.setPixmap(QPixmap("Ventana_Operativa.png"))## Label con Imagen
        ##
        LC_Ventana_Operativa = QHBoxLayout()# Creacion del layout de componentes
        LC_Ventana_Operativa.addWidget(L_Ventana_Operativa)
        ##
        ##Grupo de Componentes
        G_Ventana_Operativa = QGroupBox()
        G_Ventana_Operativa.setTitle("Vetana Operativa")
        G_Ventana_Operativa.setFont(QFont('Consolas', 10))
        G_Ventana_Operativa.setLayout(LC_Ventana_Operativa)
        G_Ventana_Operativa.setFlat(False)
        ##
        ##scroll
        S_Ventana_Operativa = QScrollArea()
        S_Ventana_Operativa.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        S_Ventana_Operativa.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        S_Ventana_Operativa.setWidgetResizable(True)
        S_Ventana_Operativa.setWidget(G_Ventana_Operativa)
        ##
        Ly_Ventana_Operativa.addWidget(S_Ventana_Operativa)
        F_Ventana_Operativa.setLayout(Ly_Ventana_Operativa)
        ##
        ##Estado Mecanico
        ##
        F_Estado_Mecanico = QFrame()
        Ly_Estado_Mecanico = QHBoxLayout()
        F_Estado_Mecanico .setFrameShape(QFrame.WinPanel) #formato del frame
        F_Estado_Mecanico .setFrameShadow(QFrame.Sunken)
        F_Estado_Mecanico .setLineWidth(3)
        F_Estado_Mecanico .setMidLineWidth(3)
        F_Estado_Mecanico .setAutoFillBackground(True)
        p = F_Estado_Mecanico .palette()
        p.setColor(F_Estado_Mecanico .backgroundRole(),Qt.white) #asignacion de colores
        F_Estado_Mecanico .setPalette(p)
        ##Layout De Componenetes
        ##Lista de componenetes
        L_Estado_Mecanico= QLabel()
        ##
        L_Estado_Mecanico.setPixmap(QPixmap("Estado Mecanico.png"))## Label con Imagen
        ##
        LC_Esatdo_Mecanico = QHBoxLayout()# Creacion del layout de componentes
        LC_Esatdo_Mecanico.addWidget(L_Estado_Mecanico)
        ##
        ##Grupo de Componentes
        G_Estado_Mecanico= QGroupBox()
        G_Estado_Mecanico.setTitle("Esatdo Mecanico")
        G_Estado_Mecanico.setFont(QFont('Consolas', 10))
        G_Estado_Mecanico.setLayout(LC_Esatdo_Mecanico)
        G_Estado_Mecanico.setFlat(False)
        ##
        ##scroll
        S_Estado_Mecanico = QScrollArea()
        S_Estado_Mecanico.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        S_Estado_Mecanico.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        S_Estado_Mecanico.setWidgetResizable(True)
        S_Estado_Mecanico.setWidget(G_Estado_Mecanico)
        ##
        Ly_Estado_Mecanico.addWidget(S_Estado_Mecanico)
        F_Estado_Mecanico.setLayout(Ly_Estado_Mecanico)
        ##
        ##
        ##Fluido
        ##
        F_Fluido = QFrame()
        Ly_Fluido = QHBoxLayout()
        F_Fluido.setFrameShape(QFrame.WinPanel) #formato del frame
        F_Fluido.setFrameShadow(QFrame.Sunken)
        F_Fluido.setLineWidth(3)
        F_Fluido.setMidLineWidth(3)
        F_Fluido.setAutoFillBackground(True)
        p = F_Fluido.palette()
        p.setColor(F_Fluido.backgroundRole(),Qt.white) #asignacion de colores
        F_Fluido.setPalette(p)
        ##Layout De Componenetes
        ##Lista de componenetes

        Le_Densidad = QLineEdit()
        Le_Densidad.setToolTip("Densidad del FLuido")
        Le_Viscocidad = QLineEdit()
        Le_Viscocidad.setToolTip("Viscocidad del Fluido")
        LC_Fluido = QFormLayout()# Creacion del layout de componentes
        LC_Fluido.addRow("ρ",Le_Densidad)
        LC_Fluido.addRow("μ",Le_Viscocidad)
        ##
        ##Grupo de Componentes
        G_Fluido= QGroupBox()
        G_Fluido.setTitle("Fluido de Perforacion")
        G_Fluido.setFont(QFont('Consolas', 10))
        G_Fluido.setLayout(LC_Fluido)
        G_Fluido.setFlat(False)
        ##
        ##scroll
        S_FLuido = QScrollArea()
        S_FLuido.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        S_FLuido.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        S_FLuido.setWidgetResizable(True)
        S_FLuido.setWidget(G_Fluido)
        ##
        Ly_Fluido.addWidget(S_FLuido)
        F_Fluido.setLayout(Ly_Fluido)
        ##
        ##
        ##Diseño Hidraulico
        ##
        F_DHidraulico = QFrame()
        Ly_DHidraulico = QHBoxLayout()
        F_DHidraulico.setFrameShape(QFrame.WinPanel) #formato del frame
        F_DHidraulico.setFrameShadow(QFrame.Sunken)
        F_DHidraulico.setLineWidth(3)
        F_DHidraulico.setMidLineWidth(3)
        F_DHidraulico.setAutoFillBackground(True)
        p = F_DHidraulico.palette()
        p.setColor(F_DHidraulico.backgroundRole(),Qt.white) #asignacion de colores
        F_DHidraulico.setPalette(p)
        ##Layout De Componenetes
        ##Lista de componenetes
        Le_LimpAgujero = QLineEdit()
        Le_LimpAgujero.setToolTip("Limpieza de agujero")
        Le_VelAnularOp = QLineEdit()
        Le_VelAnularOp.setToolTip("Velocidad Anular Óptima")
        Le_CapAccarreo= QLineEdit()
        Le_CapAccarreo.setToolTip("Capacidad de acarreo")
        Le_DEC = QLineEdit()
        Le_DEC.setToolTip("Densidad Equivalente de Circulación")
        Le_DPTotal = QLineEdit()
        Le_DPTotal.setToolTip("Caída de presión total")
        Le_VolTotal= QLineEdit()
        Le_VolTotal.setToolTip("Volumen Total")
        LC_DHidraulico = QFormLayout()# Creacion del layout de componentes
        LC_DHidraulico.addRow("Limpieza de agujero",Le_LimpAgujero)
        LC_DHidraulico.addRow("Velocidad Anular Óptima",Le_VelAnularOp)
        LC_DHidraulico.addRow("Capacidad de acarreo",Le_CapAccarreo)
        LC_DHidraulico.addRow("DEC",Le_DEC)
        LC_DHidraulico.addRow("Caída de presión total",Le_DPTotal)
        LC_DHidraulico.addRow("Volumen Total",Le_VolTotal)
        ##
        ##Grupo de Componentes
        G_DHidraulico= QGroupBox()
        G_DHidraulico.setTitle("Diseño Hidraulico")
        G_DHidraulico.setFont(QFont('Consolas', 10))
        G_DHidraulico.setLayout(LC_DHidraulico)
        G_DHidraulico.setFlat(False)
        ##
        ##scroll
        S_DHidraulico = QScrollArea()
        S_DHidraulico.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        S_DHidraulico.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        S_DHidraulico.setWidgetResizable(True)
        S_DHidraulico.setWidget(G_DHidraulico)
        ##
        Ly_DHidraulico.addWidget(S_DHidraulico)
        F_DHidraulico.setLayout(Ly_DHidraulico)
        ##
        ##
        ##
        ##Diseño Mecanico
        ##
        F_DMecanico= QFrame()
        Ly_DMecanico = QHBoxLayout()
        F_DMecanico.setFrameShape(QFrame.WinPanel) #formato del frame
        F_DMecanico.setFrameShadow(QFrame.Sunken)
        F_DMecanico.setLineWidth(3)
        F_DMecanico.setMidLineWidth(3)
        F_DMecanico.setAutoFillBackground(True)
        p = F_DMecanico.palette()
        p.setColor(F_DMecanico.backgroundRole(),Qt.white) #asignacion de colores
        F_DMecanico.setPalette(p)
        ##Layout De Componenetes
        ##Lista de componenetes
        ##Creacion de tabla
        model = QStandardItemModel()
        model2 = QStandardItemModel()
        model2.setHorizontalHeaderLabels(['Name', 'Age', 'Sex', 'Add'])
        model.setHorizontalHeaderLabels(['Secc', 'OD \n [in]', 'ID\n [in]', 'Peso Nom\n [Lb/ft]', "Peso\nAjustado\n [Kg/m]","Long.\n[m]","Peso\nFlotado\n[Kg]","Peso\nAcumulado\n[Kg]","Resistencia\nTension\n[Kg]","MOP\n[Ton]"])
        table = QTableView()
        for i in range (0,11):
            model.insertRow(i)

        model.setData(model.index(0,0),"1")


        table.setModel(model)
        LC_DMecanico = QHBoxLayout()
        LC_DMecanico.addWidget(table)
        ##
        ##Grupo de Componentes
        G_DMecanico= QGroupBox()
        G_DMecanico.setTitle("Diseño Mecanico")
        G_DMecanico.setFont(QFont('Consolas', 10))
        G_DMecanico.setLayout(LC_DMecanico)
        G_DMecanico.setFlat(False)
        ##
        ##scroll
        S_DMecanico = QScrollArea()
        S_DMecanico.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        S_DMecanico.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        S_DMecanico.setWidgetResizable(True)
        S_DMecanico.setWidget(G_DMecanico)
        ##
        Ly_DMecanico.addWidget(S_DMecanico)
        F_DMecanico.setLayout(Ly_DMecanico)
        ##


        VentanasVerticales = QSplitter(Qt.Horizontal)
        VetnanasHorizontales = QSplitter(Qt.Vertical)
        VentanasVerticales.addWidget(F_Columna_Geologica)
        VentanasVerticales.addWidget(F_Sarta)
        VentanasVerticales.addWidget(F_Estado_Mecanico)
        VentanasVerticales.addWidget(VetnanasHorizontales)
        VentanasVerticales.addWidget(F_Ventana_Operativa)
        VetnanasHorizontales.addWidget(F_Fluido)
        VetnanasHorizontales.addWidget(F_DHidraulico)
        VetnanasHorizontales.addWidget(F_DMecanico)
        hbox.addWidget(VentanasVerticales)
        central_widget.setLayout(hbox)


        ##tooltip
        QToolTip.setFont(QFont('Consolas', 10))
        btn1.setToolTip("<b>No ma si que eres bien putote</b>")

        ##btn1.setToolTip('This is a <b>QPushButton</b> widget')
        ##self.setToolTip('This is a <b>QWidget</b> widget')
         ##
        ##accion para el submenu salir
        exitAct = QAction(QIcon('exit.png'), '&Exit', self)
        ##
        ##acceso rapido y descripcion en el statusTip
        exitAct.setShortcut("Ctrl+Q")
        exitAct.setStatusTip('Exit application')
        exitAct.triggered.connect(self.exit_program)
        ##
        ##agrega una barra de menu
        menubar = self.menuBar()
        ##
        ##Elemento para la barra de menu
        fileMenu = menubar.addMenu("File")
        fileMenu1 = menubar.addMenu("Edit")
        fileMenu2 = menubar.addMenu("Help")
        ##Icono en lugar de texto para la brrra de menus  fileMenu.setIcon(QIcon("file.png"))
        ##
        ##agregar un submenu
        impMenu = QMenu('Import', self)
        impMenu.setIcon(QIcon("import.png"))
        impAct = QAction(QIcon("importemail.png"),'Import mail', self)
        impMenu.addAction(impAct)
        newAct = QAction(QIcon("newfile.png"),'New', self)
        save = QAction(QIcon("save.png"),'Save', self)
        save_as = QAction(QIcon("saveas.png"),'Save As..', self)
        ##agreegas la accion a el elemento
        fileMenu.addAction(newAct)
        fileMenu.addAction(save)
        fileMenu.addAction(save_as)
        fileMenu.addMenu(impMenu)
        fileMenu.addAction(exitAct)
        ##
        ##check menuBar
        viewStatAct = QAction('View statusbar', self, checkable=True)
        viewStatAct.setStatusTip('View statusbar')
        viewStatAct.setChecked(False)
        viewStatAct.triggered.connect(self.toggleMenu)
        fileMenu1.addAction(viewStatAct)
        btn1.clicked.connect(self.exit_program)
        ##Toolbar
        toolbar = QToolBar()
        self.addToolBar(Qt.RightToolBarArea,toolbar)
        toolbar.addAction(newAct)
        toolbar.addAction(exitAct)

##menu contextual
    def contextMenuEvent(self, event):

        cmenu = QMenu(self)
        addAct = cmenu.addAction("Agregar")
        cmenu.setIcon(QIcon("add,png"))
        deteleAct = cmenu.addAction("Eliminar")
        modifyAct = cmenu.addAction("Modificar")
        action = cmenu.exec_(self.mapToGlobal(event.pos()))
        if action == modifyAct:
            reply = QMessageBox.question(self, 'Confirmacion',
                "Estas seguro de salir?", QMessageBox.Yes |
                QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes:
                qApp.quit()

##
## Funciones
    def closeEvent(self, event):

        reply = QMessageBox.question(self, 'Message',
            "Are you sure to quit?", QMessageBox.Yes |
            QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
    def exit_program(self):
        reply = QMessageBox.question(self, 'Message',
            "Are you sure to quit?", QMessageBox.Yes |
            QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            sys.exit()


    def toggleMenu(self, state):

        if state:
            self.statusBar.show()
        else:
            self.statusBar.hide()


if __name__ == '__main__':
    print("Width =", GetSystemMetrics(0))
    print("Height =", GetSystemMetrics(1))

    app = QApplication(sys.argv)
    w = MainWindow()

    w.show()
    sys.exit(app.exec_())
