import sys
import os
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import uic
path = os.path.dirname(__file__)
qtCreatorFile = "some_dialog.ui"

Ui_Dialog, _ = uic.loadUiType(os.path.join(path,qtCreatorFile))


class CustomDialog(QDialog, Ui_Dialog):
    def __init__(self):
        super(CustomDialog, self).__init__()
        self.setupUi(self)
        # set initials values to widgets

    def getResults(self):
        if self.exec_() == QDialog.Accepted:
            # get all values
            val = self.some_widget.some_function()
            val2 = self.some_widget2.some_another_function()
            return
        else:
            return None
