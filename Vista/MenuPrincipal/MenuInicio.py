import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from win32api import GetSystemMetrics
import qtmodern

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
        self.setStyleSheet("""


        
        
        
        """)

        weas = QVBoxLayout()
        btn1 = QPushButton("Nuevo")
        btn2 = QPushButton("Cargar")
        btn3 = QPushButton("Tuberias y Herramientas")


        botones = QWidget()

        weas.addWidget(btn1)
        weas.addWidget(btn2)
        weas.addWidget(btn3)
        botones.setLayout(weas)
        self.setCentralWidget(botones)


if __name__ == '__main__':
    print("Width =", GetSystemMetrics(0))
    print("Height =", GetSystemMetrics(1))
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())


