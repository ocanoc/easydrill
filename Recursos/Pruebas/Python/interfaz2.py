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
        self.ui2()

    def ui2(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)  # new central widget
        hbox = QGridLayout()
        central_widget.setLayout(hbox)
        ## Creacion de botones
        btn1 = QPushButton("Puto Jordanx2")
        btn2 = QPushButton("Puto Jordanx3")
        btn3 = QPushButton("Puto Jordanx4")
        btn4 = QPushButton("Puto Jordanx5")
        btn5 = QPushButton("Puto Jordanx6")
        hbox.addWidget(btn1)
        hbox.addWidget(btn2)
        hbox.addWidget(btn3)
        hbox.addWidget(btn4)
        hbox.addWidget(btn5)

    def initUI (self):

        ##Status bar
        self.statusBar = self.statusBar()
        self.statusBar.showMessage('Bienvenido')
        ##
        central_widget = QWidget()
        self.setCentralWidget(central_widget) # new central widget
        ## Creacion de botones
        btn1 = QPushButton("Puto Jordanx2")
        btn2 = QPushButton("Puto Jordanx3")
        btn3 = QPushButton ("Puto Jordanx4")
        btn4 = QPushButton("Puto Jordanx5")
        btn5 = QPushButton ("Puto Jordanx6")
        ##
        ##Creacion del central
        hbox = QHBoxLayout(central_widget)
        self.setCentralWidget(central_widget) # new central widget
        central_widget.setAutoFillBackground(True) #Que se pinte el fondo
        p = central_widget.palette()
        p.setColor(central_widget.backgroundRole(),QColor(240,240,240)) #asignacion de colores
        central_widget.setPalette(p) # Asiganacion de ll pallete
        ##Para la creacion de Splitters se necesita crear frames
        ##Columna geologica, ventana Operativa y datos de fluid
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
        ##Layout De Componenetes de los datos del fluido
        Le_Densidad = QLineEdit()
        Le_Densidad.setToolTip("Densidad del FLuido")
        Le_Densidad.setMinimumWidth(50)
        Le_Densidad.setMaximumWidth(100)
        Le_Viscocidad = QLineEdit()
        Le_Viscocidad.setMinimumWidth(50)
        Le_Viscocidad.setMaximumWidth(100)
        Le_Viscocidad.setToolTip("Viscocidad del Fluido")
        densi = QFormLayout()
        densi.addRow("ρ[lb/gal]",Le_Densidad)
        densi.setSpacing(10)
        Visc= QFormLayout()
        Visc.addRow("μ[cP]",Le_Viscocidad)
        Visc.setSpacing(10)
        LC_Fluido = QHBoxLayout()
        LC_Fluido.addLayout(densi)
        LC_Fluido.addLayout(Visc)
        ##
        ##Grupo de Componentes
        G_Fluido= QGroupBox()
        G_Fluido.setTitle("Fluido de Perforacion")
        G_Fluido.setFont(QFont('Consolas', 10))
        G_Fluido.setLayout(LC_Fluido)
        G_Fluido.setFlat(False)
        G_Fluido.setFixedHeight(50)
        ##
        ##Lista de componenetes para la columna geologica y ventana Operativa
        L_Columna_Geologica = QLabel()
        ##
        L_Columna_Geologica.setPixmap(QPixmap("direccional.png"))## Label con Imagen
        LC_Columna_Geologica = QHBoxLayout()# Creacion del layout de componentes
        LC_Columna_Geologica.addWidget(L_Columna_Geologica)
        ##
        ##Grupo de Componentes
        G_Columna_Geologica = QGroupBox()
        G_Columna_Geologica.setTitle("Plan Direccional")
        G_Columna_Geologica.setFont(QFont('Consolas', 10))
        L_Columna_Geologica.setAlignment(Qt.AlignHCenter)
        G_Columna_Geologica.setLayout(LC_Columna_Geologica)
        G_Columna_Geologica.setFlat(False)
        ##
        ##layout de scroll
        Ls_Columna_Geologica = QVBoxLayout()
        Ls_Columna_Geologica.addWidget(G_Columna_Geologica)
        Ls_Columna_Geologica.addWidget(G_Fluido)
        ##scroll
        S_Columna_Geologica = QScrollArea()
        S_Columna_Geologica.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        S_Columna_Geologica.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        S_Columna_Geologica.setWidgetResizable(True)
        S_Columna_Geologica.setLayout(Ls_Columna_Geologica)
        Ly_Columna_Geologica.addWidget(S_Columna_Geologica)
        F_Columna_Geologica.setLayout(Ly_Columna_Geologica)
        F_Columna_Geologica.setMinimumWidth(350)
        ##
        ##Estado Mecanico, Sarta, Diseño Mecanico, Diseño Hidraulico
        ##
        ##Layout De Componenetes de la Sarta
        L_Sarta = QLabel()
        L_Sarta.setPixmap(QPixmap("sarta.png"))## Label con Imagen
        LC_Sarta = QHBoxLayout()# Creacion del layout de componentes
        LC_Sarta.addWidget(L_Sarta)
        ##
        ##Grupo de Componentes de la sarta
        G_Sarta = QGroupBox()
        G_Sarta.setTitle("Sarta de Perforacion")
        G_Sarta.setFont(QFont('Consolas', 10))
        LC_Sarta.setAlignment(Qt.AlignCenter)
        G_Sarta.setLayout(LC_Sarta)
        G_Sarta.setFlat(False)
        ##Layout De Componenetes de el Diseño Mecanico
        model = QStandardItemModel()
        model.setHorizontalHeaderLabels(['Secc', 'OD \n [in]', 'ID\n [in]', 'Peso Nom\n [Lb/ft]', "Peso\nAjustado\n [Kg/m]","Long.\n[m]","Peso\nFlotado\n[Kg]","Peso\nAcumulado\n[Kg]","Resistencia\nTension\n[Kg]","MOP\n[Ton]"])
        table = QTableView()
        for i in range (0,100):
            model.insertRow(i)
        model.setData(model.index(0,0),"1")
        table.setModel(model)
        table.setAlternatingRowColors(True)
        LC_DMecanico = QHBoxLayout()
        LC_DMecanico.addWidget(table)
        LC_DMecanico.setAlignment(Qt.AlignCenter)
        ##
        ##Grupo de Componentes del Diseño Mecanico
        G_DMecanico= QGroupBox()
        G_DMecanico.setTitle("Diseño Mecanico")
        G_DMecanico.setFont(QFont('Consolas', 10))
        G_DMecanico.setLayout(LC_DMecanico)
        G_DMecanico.setFlat(False)
        G_DMecanico.setMinimumHeight(150)
        ##Lista de componenetes del Estado Mecanico
        L_Estado_Mecanico= QLabel()
        L_Estado_Mecanico.setPixmap(QPixmap("Estado Mecanico.png"))## Label con Imagen
        ##
        LC_Esatdo_Mecanico = QHBoxLayout()# Creacion del layout de componentes
        LC_Esatdo_Mecanico.addWidget(L_Estado_Mecanico)
        ##
        ##Grupo de Componentes del estado Mecanico
        G_Estado_Mecanico= QGroupBox()
        G_Estado_Mecanico.setTitle("Esatdo Mecanico")
        G_Estado_Mecanico.setAutoFillBackground(False)
        G_Estado_Mecanico.setFont(QFont('Consolas', 10))
        LC_Esatdo_Mecanico.setAlignment(Qt.AlignCenter)
        G_Estado_Mecanico.setLayout(LC_Esatdo_Mecanico)
        G_Estado_Mecanico.setMinimumHeight(100)
        G_Estado_Mecanico.setFlat(False)
        ##
        ##Lista de componenetes del diseñp Hidraulico
        Le_LimpAgujero = QLineEdit("Holi")
        print(Le_LimpAgujero.text())
        Le_LimpAgujero.setMaximumWidth(100)
        Le_LimpAgujero.setMinimumWidth(50)
        Le_LimpAgujero.setToolTip("Limpieza de agujero")
        Le_VelAnularOp = QLineEdit()
        Le_VelAnularOp.setMaximumWidth(100)
        Le_VelAnularOp.setMinimumWidth(50)
        Le_VelAnularOp.setToolTip("Velocidad Anular Óptima")
        Le_CapAccarreo= QLineEdit()
        Le_CapAccarreo.setMaximumWidth(100)
        Le_CapAccarreo.setMinimumWidth(50)
        Le_CapAccarreo.setToolTip("Capacidad de acarreo")
        Le_DEC = QLineEdit()
        Le_DEC.setMaximumWidth(100)
        Le_DEC.setMinimumWidth(50)
        Le_DEC.setToolTip("Densidad Equivalente de Circulación")
        Le_DPTotal = QLineEdit()
        Le_DPTotal.setMaximumWidth(100)
        Le_DPTotal.setMinimumWidth(50)
        Le_DPTotal.setToolTip("Caída de presión total")
        Le_VolTotal= QLineEdit()
        Le_VolTotal.setMaximumWidth(100)
        Le_VolTotal.setMinimumWidth(50)
        Le_VolTotal.setToolTip("Volumen Total")
        Il = QFormLayout()
        Il.addRow("I.L [H.P./pg<sup>2</sup>] ",Le_LimpAgujero)
        Il.setSpacing(10)
        Vo= QFormLayout()
        Vo.addRow("Vo [ft/seg]",Le_VelAnularOp)
        Vo.setSpacing(10)
        ICA = QFormLayout()
        ICA.addRow("ICA",Le_CapAccarreo)
        ICA.setSpacing(10)
        DEC = QFormLayout()
        DEC.addRow("DEC [gr/cm<sup>3</sup>]",Le_DEC)
        DEC.setSpacing(10)
        dpt = QFormLayout()
        dpt.addRow("DPt [Psi]",Le_DPTotal)
        dpt.setSpacing(10)
        Vtotal = QFormLayout()
        Vtotal.addRow("Vt [m<sup>3</sup>]",Le_VolTotal)
        Vtotal.setSpacing(10)
        LC_DHidraulico = QHBoxLayout()
        LC_DHidraulico.setSpacing(50)
        LC_DHidraulico.addLayout(Il)
        LC_DHidraulico.addLayout(Vo)
        LC_DHidraulico.addLayout(ICA)
        LC_DHidraulico.addLayout(DEC)
        LC_DHidraulico.addLayout(dpt)
        LC_DHidraulico.addLayout(Vtotal)
        ##
        ##Grupo de Componentes del Diseño Hidraulico
        G_DHidraulico= QGroupBox()
        G_DHidraulico.setTitle("Diseño Hidraulico")
        G_DHidraulico.setFont(QFont('Consolas', 10))
        G_DHidraulico.setLayout(LC_DHidraulico)
        G_DHidraulico.setFlat(False)
        G_DHidraulico.setMaximumHeight(50)
        ##
        ##layout del tab de Estado Mecanico y Diseño Hidraulico
        L_Tab_EMeacnico = QVBoxLayout()
        L_Tab_EMeacnico.addWidget(G_Estado_Mecanico)
        L_Tab_EMeacnico.addWidget(G_DHidraulico)
        W_Tab_EMeacnico = QWidget()
        W_Tab_EMeacnico.setLayout(L_Tab_EMeacnico)
        ##Layout del tan de la Sarta y Diseño Mecanico
        L_Tab_Sarta= QVBoxLayout()
        L_Tab_Sarta.addWidget(G_Sarta)
        L_Tab_Sarta.addWidget(G_DMecanico)
        W_Tab_Sarta = QWidget()
        W_Tab_Sarta.setLayout(L_Tab_Sarta)
        ##Tab central
        Tab_Central = QTabWidget()
        Tab_Central.addTab(W_Tab_EMeacnico,"Estado Mecanico")
        Tab_Central.addTab(W_Tab_Sarta,"Sarta de Perforacion")
        ##scroll del tab central
        S_Estado_Mecanico = QScrollArea()
        S_Estado_Mecanico.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        S_Estado_Mecanico.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        S_Estado_Mecanico.setWidgetResizable(True)
        S_Estado_Mecanico.setWidget(Tab_Central)
        ##
        ##Splitters
        ##
        VentanasVerticales = QSplitter(Qt.Horizontal)
        VentanasVerticales.addWidget(Tab_Central)
        VentanasVerticales.addWidget(F_Columna_Geologica)
        hbox.addWidget(VentanasVerticales)
        central_widget.setLayout(hbox)
        ##tooltip
        QToolTip.setFont(QFont('Consolas', 10))
        btn1.setToolTip("<b>No ma si que eres bien putote</b>")
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
        self.addToolBar(Qt.LeftToolBarArea,toolbar)
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
